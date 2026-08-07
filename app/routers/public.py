from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.submission import SubmissionCreate

from app.services.submission_service import SubmissionService
from app.services.geo_service import get_location
from app.services.spam_service import check_spam
from app.services.rate_limit import limiter

from app.models.widget import Widget

router = APIRouter(
    prefix="/public",
    tags=["Public"]
)


@router.get("/widget/{widget_id}")
def get_widget_config(
    widget_id: int,
    db: Session = Depends(get_db),
):

    widget = (
        db.query(Widget)
        .filter(
            Widget.id == widget_id
        )
        .first()
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    response = JSONResponse(
        content={
            "id": widget.id,
            "title": widget.title,
            "description": widget.description,
            "button_text": widget.button_text,
            "fields": widget.fields,
            "version": "1.0.0"
        }
    )

    response.headers["Cache-Control"] = "public, max-age=300"

    return response


@router.options("/submit/{widget_id}")
def cors_preflight():

    return {
        "message": "CORS OK"
    }


@router.post("/submit/{widget_id}")
@limiter.limit("5/minute")
def submit_widget(
    widget_id: int,
    submission: SubmissionCreate,
    request: Request,
    db: Session = Depends(get_db),
):

    widget = (
        db.query(Widget)
        .filter(
            Widget.id == widget_id
        )
        .first()
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    data = submission.model_dump()

    if check_spam(data):
        raise HTTPException(
            status_code=400,
            detail="Spam detected",
        )

    visitor_ip = (
        request.client.host
        if request.client
        else "unknown"
    )

    geo = get_location(visitor_ip)

    data["country"] = geo.get("country")
    data["city"] = geo.get("city")
    data["tenant_id"] = widget.tenant_id

    saved = SubmissionService.create_submission(
        db,
        widget_id,
        data,
    )

    return {
        "success": True,
        "message": "Submission received",
        "submission_id": saved.id,
    }
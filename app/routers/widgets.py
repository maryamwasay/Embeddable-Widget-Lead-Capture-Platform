from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.widget import Widget
from app.schemas.widget import (
    WidgetCreate,
    WidgetUpdate,
    WidgetResponse,
)
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/widgets",
    tags=["Widgets"],
)


@router.get("/")
def get_widgets(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    widgets = (
        db.query(Widget)
        .filter(
            Widget.tenant_id == current_user["tenant_id"]
        )
        .all()
    )

    return widgets


@router.get("/{widget_id}")
def get_widget(
    widget_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    widget = (
        db.query(Widget)
        .filter(
            Widget.id == widget_id,
            Widget.tenant_id == current_user["tenant_id"],
        )
        .first()
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    return widget


@router.post("/", response_model=WidgetResponse)
def create_widget(
    widget_data: WidgetCreate,
    db: Session =Depends(get_db),
    current_user=Depends(get_current_user),
):

    widget = Widget(
        tenant_id=current_user["tenant_id"],
        title=widget_data.title,
        description=widget_data.description,
        widget_type=widget_data.widget_type,
        button_text=widget_data.button_text,
        fields=[
            field.model_dump()
            for field in widget_data.fields
        ],
    )

    db.add(widget)
    db.commit()
    db.refresh(widget)

    return widget


@router.put("/{widget_id}")
def update_widget(
    widget_id: int,
    data: WidgetUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    widget = (
        db.query(Widget)
        .filter(
            Widget.id == widget_id,
            Widget.tenant_id == current_user["tenant_id"],
        )
        .first()
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(widget, key, value)

    db.commit()
    db.refresh(widget)

    return widget


@router.delete("/{widget_id}")
def delete_widget(
    widget_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    widget = (
        db.query(Widget)
        .filter(
            Widget.id == widget_id,
            Widget.tenant_id == current_user["tenant_id"],
        )
        .first()
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    db.delete(widget)
    db.commit()

    return {
        "message": "Widget deleted"
    }


# ======================================================
# NEW
# Generate Embed Snippet
# ======================================================

@router.get("/{widget_id}/embed")
def get_embed_code(
    widget_id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    widget = (
        db.query(Widget)
        .filter(
            Widget.id == widget_id,
            Widget.tenant_id == current_user["tenant_id"],
        )
        .first()
    )

    if not widget:
        raise HTTPException(
            status_code=404,
            detail="Widget not found",
        )

    base = str(request.base_url).rstrip("/")

    return {
        "widget_id": widget.id,
        "embed_code": (
            f'<script src="{base}/static/widget.js" '
            f'data-widget-id="{widget.id}"></script>'
        )
    }
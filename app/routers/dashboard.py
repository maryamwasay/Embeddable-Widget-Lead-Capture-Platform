from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db

from app.models.submission import Submission
from app.models.widget import Widget

from app.auth.dependencies import get_current_user



router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)




@router.get("/summary")
def dashboard_summary(

    db:Session=Depends(get_db),

    current_user=Depends(get_current_user)

):


    total_widgets=(

        db.query(Widget)

        .filter(

            Widget.tenant_id ==
            current_user["tenant_id"]

        )

        .count()

    )


    total_submissions=(

        db.query(Submission)

        .filter(

            Submission.tenant_id ==
            current_user["tenant_id"]

        )

        .count()

    )



    return {

        "widgets":total_widgets,

        "submissions":total_submissions

    }





@router.get("/widgets")
def widget_statistics(

    db:Session=Depends(get_db),

    current_user=Depends(get_current_user)

):


    result=(

        db.query(

            Widget.id,

            Widget.title,

            func.count(
                Submission.id
            )

        )

        .outerjoin(

            Submission,

            Widget.id ==
            Submission.widget_id

        )

        .filter(

            Widget.tenant_id ==
            current_user["tenant_id"]

        )

        .group_by(
            Widget.id
        )

        .all()

    )


    return [

        {

            "widget_id":row[0],

            "title":row[1],

            "submissions":row[2]

        }

        for row in result

    ]





@router.get("/countries")
def country_statistics(

    db:Session=Depends(get_db),

    current_user=Depends(get_current_user)

):


    result=(

        db.query(

            Submission.country,

            func.count(
                Submission.id
            )

        )

        .filter(

            Submission.tenant_id ==
            current_user["tenant_id"]

        )

        .group_by(

            Submission.country

        )

        .all()

    )


    return [

        {

            "country":row[0],

            "count":row[1]

        }

        for row in result

    ]
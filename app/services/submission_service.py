from sqlalchemy.orm import Session

from app.models.submission import Submission



class SubmissionService:


    @staticmethod
    def create_submission(

        db: Session,

        widget_id: int,

        data: dict

    ):


        submission = Submission(

            widget_id=widget_id,

            tenant_id=data.get(
                "tenant_id"
            ),

            name=data.get(
                "name"
            ),

            email=data.get(
                "email"
            ),

            phone=data.get(
                "phone"
            ),

            message=data.get(
                "message"
            ),

            country=data.get(
                "country"
            ),

            city=data.get(
                "city"
            )

        )


        db.add(submission)

        db.commit()

        db.refresh(submission)


        return submission
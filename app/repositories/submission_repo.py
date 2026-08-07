from sqlalchemy.orm import Session

from app.models.submission import Submission


class SubmissionRepository:

    @staticmethod
    def create(
        db: Session,
        submission: Submission
    ):
        db.add(submission)
        db.commit()
        db.refresh(submission)

        return submission

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(Submission).all()

    @staticmethod
    def get_by_widget(
        db: Session,
        widget_id: int
    ):
        return (
            db.query(Submission)
            .filter(Submission.widget_id == widget_id)
            .all()
        )

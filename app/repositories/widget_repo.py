from sqlalchemy.orm import Session

from app.models.widget import Widget


class WidgetRepository:

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(Widget).all()

    @staticmethod
    def get_by_id(
        db: Session,
        widget_id: int
    ):
        return (
            db.query(Widget)
            .filter(Widget.id == widget_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        widget: Widget
    ):
        db.add(widget)
        db.commit()
        db.refresh(widget)

        return widget

    @staticmethod
    def delete(
        db: Session,
        widget: Widget
    ):
        db.delete(widget)
        db.commit()
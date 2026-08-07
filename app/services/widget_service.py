from sqlalchemy.orm import Session

from app.models.widget import Widget
from app.repositories.widget_repo import WidgetRepository
from app.schemas.widget import WidgetCreate, WidgetUpdate


class WidgetService:

    @staticmethod
    def get_widgets(
        db: Session,
        tenant_id: int
    ):
        return (
            db.query(Widget)
            .filter(Widget.tenant_id == tenant_id)
            .all()
        )


    @staticmethod
    def get_widget(
        db: Session,
        widget_id: int,
        tenant_id: int
    ):

        widget = (
            db.query(Widget)
            .filter(
                Widget.id == widget_id,
                Widget.tenant_id == tenant_id
            )
            .first()
        )

        return widget


    @staticmethod
    def create_widget(
        db: Session,
        widget_data: WidgetCreate,
        tenant_id: int
    ):

        widget = Widget(
            tenant_id=tenant_id,
            title=widget_data.title,
            description=widget_data.description,
            widget_type=widget_data.widget_type,
            button_text=widget_data.button_text,
            fields=[
                field.model_dump()
                for field in widget_data.fields
            ]
        )

        return WidgetRepository.create(
            db,
            widget
        )


    @staticmethod
    def update_widget(
        db: Session,
        widget_id: int,
        tenant_id: int,
        update_data: WidgetUpdate
    ):

        widget = WidgetService.get_widget(
            db,
            widget_id,
            tenant_id
        )

        if not widget:
            return None


        data = update_data.model_dump(
            exclude_unset=True
        )


        if "fields" in data:
            data["fields"] = [
                field.model_dump()
                for field in data["fields"]
            ]


        for key,value in data.items():
            setattr(
                widget,
                key,
                value
            )


        db.commit()
        db.refresh(widget)

        return widget



    @staticmethod
    def delete_widget(
        db: Session,
        widget_id: int,
        tenant_id: int
    ):

        widget = WidgetService.get_widget(
            db,
            widget_id,
            tenant_id
        )

        if not widget:
            return False


        WidgetRepository.delete(
            db,
            widget
        )

        return True
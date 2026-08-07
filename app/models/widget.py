from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.database import Base



class Widget(Base):

    __tablename__ = "widgets"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    tenant_id = Column(
        Integer,
        ForeignKey("tenants.id"),
        nullable=False
    )


    title = Column(
        String(255),
        nullable=False
    )


    description = Column(
        String(500),
        nullable=True
    )


    widget_type = Column(
        String(100),
        nullable=False
    )


    button_text = Column(
        String(100),
        default="Submit"
    )


    fields = Column(
        JSON,
        nullable=False
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    tenant = relationship(
        "Tenant",
        back_populates="widgets"
    )


    submissions = relationship(
        "Submission",
        back_populates="widget"
    )
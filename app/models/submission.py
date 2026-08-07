from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    widget_id = Column(
        Integer,
        ForeignKey("widgets.id"),
        nullable=False
    )

    tenant_id = Column(
        Integer,
        ForeignKey("tenants.id"),
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        nullable=False
    )

    phone = Column(
        String(50),
        nullable=True
    )

    message = Column(
        String(1000),
        nullable=True
    )

    country = Column(
        String(100),
        nullable=True
    )

    city = Column(
        String(100),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    widget = relationship(
        "Widget",
        back_populates="submissions"
    )

    tenant = relationship(
        "Tenant",
        back_populates="submissions"
    )
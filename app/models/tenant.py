from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationships
    users = relationship(
        "User",
        back_populates="tenant",
        cascade="all, delete-orphan"
    )

    widgets = relationship(
        "Widget",
        back_populates="tenant",
        cascade="all, delete-orphan"
    )

    submissions = relationship(
        "Submission",
        back_populates="tenant",
        cascade="all, delete-orphan"
    )
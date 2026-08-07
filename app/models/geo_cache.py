from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func

from app.database import Base


class GeoCache(Base):
    __tablename__ = "geo_cache"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ip_address = Column(
        String(100),
        unique=True,
        nullable=False
    )

    country = Column(
        String(100),
        nullable=True
    )

    city = Column(
        String(100),
        nullable=True
    )

    cached_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

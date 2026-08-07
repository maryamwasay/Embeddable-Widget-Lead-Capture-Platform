from typing import Optional

from pydantic import BaseModel, EmailStr


class SubmissionCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: Optional[str] = None


class SubmissionResponse(BaseModel):
    id: int
    widget_id: int
    name: str
    email: EmailStr
    phone: Optional[str]
    message: Optional[str]
    country: Optional[str]
    city: Optional[str]

    class Config:
        from_attributes = True

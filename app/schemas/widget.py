from typing import List, Optional

from pydantic import BaseModel


class WidgetField(BaseModel):
    name: str
    type: str
    required: bool


class WidgetCreate(BaseModel):
    title: str
    description: Optional[str] = None
    widget_type: str
    button_text: str
    fields: List[WidgetField]


class WidgetUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    widget_type: Optional[str] = None
    button_text: Optional[str] = None
    fields: Optional[List[WidgetField]] = None


class WidgetResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    widget_type: str
    button_text: str
    fields: List[WidgetField]

    class Config:
        from_attributes = True
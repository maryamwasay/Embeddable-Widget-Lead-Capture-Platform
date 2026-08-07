from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_widgets: int
    total_submissions: int
    spam_submissions: int


class WidgetStats(BaseModel):
    widget_id: int
    widget_title: str
    submission_count: int


class CountryStats(BaseModel):
    country: str
    submissions: int
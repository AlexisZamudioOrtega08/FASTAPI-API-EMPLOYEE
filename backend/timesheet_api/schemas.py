import string
from pydantic import BaseModel, validator


class TimesheetEntry(BaseModel):
    """Timesheet entry schema."""

    hours: int
    description: str = None

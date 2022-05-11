from sqlalchemy import Column, Integer, String
from database import Base


class Timesheet(Base):
    __tablename__ = "timesheets"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    name = Column(String)
    date = Column(String, index=True)
    hours = Column(Integer, index=True)
    description = Column(String, index=True)

from datetime import date
from fastapi import FastAPI, HTTPException, Depends
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from schemas import TimesheetEntry
import aiohttp
from datetime import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    """
    Complete the full cycle of a db session (open, close).
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/api/timesheet/", status_code=200)
async def get_timesheets(db: Session = Depends(get_db)):
    """
    Get all timesheets registered in the database.
    """
    return db.query(models.Timesheet).all()


@app.post("/api/timesheet/{emp_id}", status_code=201)
async def create_timesheet(
    emp_id, timesheet_entry: TimesheetEntry, db: Session = Depends(get_db)
):
    """
    Create a new timesheet, it consumps the employees API to verify if the employee exists.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://127.0.0.1:8001/api/employee/{}".format(emp_id)
        ) as resp:
            data = await resp.json()
            try:
                new_timesheet = models.Timesheet(
                    employee_id=data["id"],
                    name=data["name"],
                    hours=timesheet_entry.hours,
                    description=timesheet_entry.description,
                    # add current time to the timesheet
                    date=datetime.now(),
                )
                db.add(new_timesheet)
                db.commit()
                return {"message": "Timesheet added"}
            except Exception as e:
                raise HTTPException(status_code=404, detail="Employee not found")

from fastapi import FastAPI, HTTPException, Depends
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

employees = []

models.Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    """
    Complete the full cycle of a session (open, close).
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/api/employees/", status_code=200)
async def get_employees(db: Session = Depends(get_db)):
    """
    Get all employees
    """
    return db.query(models.Employee).all()


@app.post("/api/employee", status_code=201)
async def add_employee(emp_id: int, emp_name: str, db: Session = Depends(get_db)):
    """
    Add a new employee to the database
    """
    try:
        new_employee = models.Employee(id=emp_id, name=emp_name)
        db.add(new_employee)
        db.commit()
        return {"message": "Employee added"}
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            raise HTTPException(
                status_code=400, detail="An employee with provided id already exists"
            )
        else:
            raise HTTPException(status_code=500, detail="Internal server error")

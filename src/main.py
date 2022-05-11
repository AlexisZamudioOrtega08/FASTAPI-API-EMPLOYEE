from fastapi import FastAPI, Response, status, HTTPException

app = FastAPI()

employees = [{"id": 1, "name": "John"}, {"id": 2, "name": "Doe"}, {"id": 3, "name": "Smith"}]

@app.get("/api/employees/", status_code=200)
async def get_employees() -> Response:
    '''
    Get all employees
    '''
    return [employee for employee in employees]

@app.post("/api/employee", status_code=201) 
async def add_employee(emp_id: int, emp_name: str) -> Response:
    '''
    Add an employee to the list
    '''
    employee = {"id": emp_id, "name": emp_name}
    if id not in [employee["id"] for employee in employees]:
        employees.append(employee)
        return employee
    else:
        raise HTTPException(status_code=400, detail="Employee already exists")


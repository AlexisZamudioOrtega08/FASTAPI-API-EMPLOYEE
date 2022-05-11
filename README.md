# FASTAPI Employee API

## This is a simple API for managing employees.

### This API support the following operations:
    READ: Return the list of employees.
    CREATE: Create a new employee.
#### GET all employees

```http
  method: GET
  localhost:8000/api/employees
```

#### POST employee

```http
  method: POST
  localhost:8000/api/employee
```

| Parameter  | Type     | Description                 |
| :--------  | :------- | :-------------------------  |
| `emp_name` | `string` | **Required**. Employee name |
| `emp_id`   | `int`    | **Required**. Employee id   |


### For installation, please create a python virtual environment and install requirements.txt.

    pip install -r requirements.txt

### Once installated and activated, go to src folder and run below command.

    uvicorn main:app --reload

#### If the step before was completed successfully, you must have running the server on your local host.
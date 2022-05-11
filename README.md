# FASTAPI API USAGE.

## This is a sample of API comsumption.

### The API (Employees) support the following operations:
    READ: Return a json with employees details.
    CREATE: Create a new employee.

#### GET a single employee:
```http
  method: GET
  localhost:8001/api/employee/{emp_id}
```

| Parameter  | Type     | Description                 |
| :--------  | :------- | :-------------------------  |
| `emp_id`   | `int`    | **Required**. Employee id   |

#### GET all employees

```http
  method: GET
  localhost:8001/api/employees
```

#### POST employee

```http
  method: POST
  localhost:8001/api/employee
```

| Parameter  | Type     | Description                 |
| :--------  | :------- | :-------------------------  |
| `emp_name` | `string` | **Required**. Employee name |
| `emp_id`   | `int`    | **Required**. Employee id   |


### The API (Timesheet) support the following operations:
    READ: Return a json with timesheet entries.
    CREATE: Create a new timesheet entry.
#### GET all timesheet entries

```http
  method: GET
  localhost:8000/api/timesheet
```

#### POST a timesheet entry

```http
  method: POST
  localhost:8000/api/timesheet
```

| Parameter     | Type     | Description                         |
| :------------ | :------- | :---------------------------------- |
| `emp_id`      | `int`    | **Required**. Employee id           |
| `hours`       | `int`    | **Required**. Hours worked by emp   |
| `description` | `string` | **Required**. Description           |

### The timesheet API comsumps employeed API data and verifies if the employee is in the database as well as if id provided is valid.

### For installation, please create a python virtual environment and install requirements.txt.

    pip install -r requirements.txt

### Once installated and activated, run 2 simultaneous terminal and execute below.
    On terminal 1:
       Go to backend/employees_api and run:
           uvicorn main:app --reload --port 8001
    
    On terminal 2:
        Go to backend/timesheet_api and run:
            uvicorn main:app --reload --port 8000


#### If the step before was completed successfully, you must have running the server on your local host.

    In order to test the API, you can use the following URL:
            localhost:8001/docs (for the API documentation)

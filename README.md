# FASTAPI Employee API

## This is a simple API for managing employees.

### This API support the following operations:
    READ: Return the list of employees.
    CREATE: Create a new employee.
#### GET all employees

```http
  GET /api/employees
```

#### POST employee

```http
  POST /api/employee
```

| Parameter  | Type     | Description                 |
| :--------  | :------- | :-------------------------  |
| `name`     | `string` | **Required**. Employee name |
| `id`       | `int`    | **Required**. Employee id   |

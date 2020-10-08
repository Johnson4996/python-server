EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Baker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Fred Johnson",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Paul Rudd",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Paul Blart",
      "locationId": 1
    },
    {
      "id": 5,
      "name": "Sam Smith",
      "locationId": 1,
      
    }
  ]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

def create_employee(employee):
  max_id = EMPLOYEES[-1]["id"]

  new_id = max_id + 1

  employee["id"] = new_id

  EMPLOYEES.append(employee)

  return employee
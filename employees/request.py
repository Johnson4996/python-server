import sqlite3
import json
from models import Employee, Location

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
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l
          ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all customer representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id']
                            )
            location = Location("",row['location_name'], row['location_address'])  

            employee.location = location.__dict__             

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data['id'], data['name'], data['address'], data['location_id']          
                        )

        return json.dumps(employee.__dict__)

def create_employee(employee):
  max_id = EMPLOYEES[-1]["id"]

  new_id = max_id + 1

  employee["id"] = new_id

  EMPLOYEES.append(employee)

  return employee

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      EMPLOYEES[index] = new_employee
      break

def get_employees_by_location(locId):
  with sqlite3.connect("./kennel.db") as conn:
    conn.row_factory= sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, ( locId, ))

    employees = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      employee = Employee(row['id'],row['name'],row['address'],row['location_id'])
      employees.append(employee)

  return json.dumps(employees)
CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "Jimmy Butler",
      "address": "1000 Cool Lane"
    },
    {
      "id": 3,
      "name": "Frank Ocean",
      "address": "2345 Sea St"
    }
  ]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

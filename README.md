# Vendor Management API

This project provides a RESTful API for managing vendors and purchase orders.

## Setup Instructions

1. Clone the repository:

git clone https://github.com/karthik-2307/internship-project.git

2. Navigate to the vendor_management_system directory:
cd vendor_management_system

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the development server:
python manage.py runserver

The API will be accessible at http://localhost:8000/.

## API Endpoints

- **Vendors:**
  - `GET /vendors/`: List all vendors
  - `POST /vendors/`: Create a new vendor
  - `GET /vendors/<id>/`: Retrieve details of a specific vendor
  - `PUT /vendors/<id>/`: Update details of a specific vendor
  - `DELETE /vendors/<id>/`: Delete a specific vendor

- **Purchase Orders:**
  - `GET /purchase-orders/`: List all purchase orders
  - `POST /purchase-orders/`: Create a new purchase order
  - `GET /purchase-orders/<id>/`: Retrieve details of a specific purchase order
  - `PUT /purchase-orders/<id>/`: Update details of a specific purchase order
  - `DELETE /purchase-orders/<id>/`: Delete a specific purchase order

## Sample Data for Vendors:
[
  {
    "id": 1,
    "name": "Vendor A",
    "contact_person": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "123-456-7890",
    "address": "123 Main Street, City, Country"
  },
  {
    "id": 2,
    "name": "Vendor B",
    "contact_person": "Jane Smith",
    "email": "jane.smith@example.com",
    "phone_number": "987-654-3210",
    "address": "456 Elm Street, City, Country"
  }
]

## Sample Data for Purchase Orders:
[
  {
    "id": 1,
    "vendor_id": 1,
    "order_date": "2024-05-13",
    "delivery_date": "2024-05-20",
    "total_amount": 500.00,
    "status": "pending",
    "items": [
      {
        "id": 1,
        "name": "Item 1",
        "quantity": 10,
        "unit_price": 25.00,
        "total_price": 250.00
      },
      {
        "id": 2,
        "name": "Item 2",
        "quantity": 5,
        "unit_price": 50.00,
        "total_price": 250.00
      }
    ]
  },
  {
    "id": 2,
    "vendor_id": 2,
    "order_date": "2024-05-15",
    "delivery_date": "2024-05-25",
    "total_amount": 750.00,
    "status": "completed",
    "items": [
      {
        "id": 3,
        "name": "Item 3",
        "quantity": 20,
        "unit_price": 30.00,
        "total_price": 600.00
      },
      {
        "id": 4,
        "name": "Item 4",
        "quantity": 5,
        "unit_price": 30.00,
        "total_price": 150.00
      }
    ]
  }
]


## Testing

python manage.py test




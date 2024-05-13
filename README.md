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
Description:For testing all the given code 
python manage.py test


## API Endpoints

### Vendors Endpoints:

1. **List Vendors**:
   - URL: `/vendors/`
   - Method: GET
   - Description: Retrieves a list of all vendors.

2. **Create Vendor**:
   - URL: `/vendors/`
   - Method: POST
   - Description: Creates a new vendor.

3. **Retrieve Vendor**:
   - URL: `/vendors/<vendor_id>/`
   - Method: GET
   - Description: Retrieves details of a specific vendor.

4. **Update Vendor**:
   - URL: `/vendors/<vendor_id>/`
   - Method: PUT
   - Description: Updates details of a specific vendor.

5. **Delete Vendor**:
   - URL: `/vendors/<vendor_id>/`
   - Method: DELETE
   - Description: Deletes a specific vendor.

### Purchase Orders Endpoints:

1. **List Purchase Orders**:
   - URL: `/purchase-orders/`
   - Method: GET
   - Description: Retrieves a list of all purchase orders.

2. **Create Purchase Order**:
   - URL: `/purchase-orders/`
   - Method: POST
   - Description: Creates a new purchase order.

3. **Retrieve Purchase Order**:
   - URL: `/purchase-orders/<order_id>/`
   - Method: GET
   - Description: Retrieves details of a specific purchase order.

4. **Update Purchase Order**:
   - URL: `/purchase-orders/<order_id>/`
   - Method: PUT
   - Description: Updates details of a specific purchase order.

5. **Delete Purchase Order**:
   - URL: `/purchase-orders/<order_id>/`
   - Method: DELETE
   - Description: Deletes a specific purchase order.

## Example Usage

- **List Vendors**: `GET /vendors/`
- **Create Vendor**: `POST /vendors/` with JSON data for a new vendor.
- **Retrieve Vendor**: `GET /vendors/<vendor_id>/`
- **Update Vendor**: `PUT /vendors/<vendor_id>/` with JSON data for updated vendor details.
- **Delete Vendor**: `DELETE /vendors/<vendor_id>/`

Repeat similar steps for purchase orders endpoints, replacing `<order_id>` with the ID of the purchase order.

Ensure that you include all required fields in your requests and handle responses appropriately based on HTTP status codes and response data.



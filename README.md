# Invoice Management System
This project is an Invoice Management System developed using Django and Django Rest Framework. It provides APIs to manage invoices and their details, allowing users to create, retrieve, update, and delete invoices.

## Installation
Clone the repository: git clone <repository-url>

Navigate to the project directory: cd invoice_management_system

Create and activate a virtual environment (optional but recommended):

For virtualenv: virtualenv venv && source venv/bin/activate

For pipenv: pipenv install && pipenv shell

Install the dependencies: pip install -r requirements.txt

Apply database migrations: python manage.py migrate

Start the development server: python manage.py runserver

## API Endpoints
The following API endpoints are available:

GET /invoices/: Retrieve a list of all invoices

GET /invoices/{id}/: Retrieve details of a specific invoice

POST /invoices/: Create a new invoice

PUT /invoices/{id}/: Update an existing invoice

DELETE /invoices/{id}/: Delete an existing invoice

Refer to the API documentation for more details on request payloads and responses.

## Example API Payload
To create a new invoice, send a POST request to /invoices/ with the following payload:

json

Copy code

{

  "date": "2023-01-01",
  
  "invoice_no": "INV-001",
  
  "customer_name": "John Doe",
  
  "invoice_detail": [
  
    {
    
      "description": "Product A",
      
      "quantity": 2,
      
      "unit_price": 10.0,
      
      "price": 20.0
      
    },
    
    {
    
      "description": "Product B",
      
      "quantity": 3,
      
      "unit_price": 15.0,
      
      "price": 45.0
      
    }
    
  ]
  
}

## Testing
To run the test cases, use the following command: python manage.py test

## Contributing
Contributions are welcome! If you find any issues or want to suggest enhancements, feel free to open an issue or submit a pull request.

## Acknowledgements
This project was developed as part of an internship assignment. Special thanks to the team for providing guidance and support during the development process.

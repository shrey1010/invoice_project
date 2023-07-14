from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice


class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        url = '/invoices/'
        data = {
            'date': '2023-01-01',
            'invoice_no': 'INV-001',
            'customer_name': 'John Doe',
            'invoice_detail': [
                {
                    'description': 'Product A',
                    'quantity': 2,
                    'unit_price': 10.0,
                    'price': 20.0
                },
                {
                    'description': 'Product B',
                    'quantity': 3,
                    'unit_price': 15.0,
                    'price': 45.0
                }
            ]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_get_invoice_list(self):
        url = '/invoices/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_invoice(self):
        invoice = Invoice.objects.create(
            date='2023-01-01',
            invoice_no='INV-001',
            customer_name='John Doe'
        )
        url = f'/invoices/{invoice.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['invoice_no'], 'INV-001')

    # Add more test cases for other API endpoints and edge cases

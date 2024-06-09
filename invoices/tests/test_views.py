import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from unittest.mock import patch
from invoices.views import UploadInvoiceView, SummaryView, HealthCheck
from invoices.models import Invoice

@pytest.mark.django_db
class TestViews:

    @pytest.fixture
    def api_client(self):
        api_client=APIClient()
        return api_client
    
    @pytest.fixture()
    def mock_process_invoice_file(self):
        pass

    @patch('invoices.views.process_invoice_file.delay')
    def test_upload_invoice_success(self, api_client, mock_process_invoice_file):
        # Prepare test data
        file_mock = {'file': ('test.csv', b'')}
        
        # Make the request
        response = api_client.post(reverse('upload-invoice'), file_mock, format='multipart')
        
        # Check response
        assert response.status_code == status.HTTP_202_ACCEPTED
        assert response.data == {"message": "File uploaded and is being processed"}
        mock_process_invoice_file.assert_called_once()

    def test_summary_view(self, api_client):
        # Prepare test data
        invoice_data = {
            'date': '2023-04-30',
            'invoice_number': '3531',
            'value': 519.5,
            'haircut_percent': 10,
            'daily_fee_percent': 0.125,
            'currency': 'USD',
            'revenue_source': 'Happy Playcrows',
            'customer': 'RunUp INC',
            'expected_payment_duration': 65
        }
        Invoice.objects.create(**invoice_data)

        # Make the request
        url = reverse('summary')
        response = api_client.get(url)

        # Check response
        assert response.status_code == status.HTTP_200_OK
        assert 'invoices/summary.html' in [template.name for template in response.templates]

    def test_health_check(self, api_client):
        # Make the request
        url = reverse('healthcheck')
        response = api_client.get(url)
        
        # Check response
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"ping": "pong"}
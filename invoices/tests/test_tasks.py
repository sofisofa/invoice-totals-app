from decimal import Decimal
import pytest
import pandas as pd
from io import BytesIO
from invoices.tasks import process_invoice_file
from invoices.models import Invoice

@pytest.mark.django_db
class TestTasks:
    def test_process_invoice_file(self):
        # Given
        test_data = b"""
date,invoice number,value,haircut percent,Daily fee percent,currency,Revenue source,customer,Expected payment duration
2023-04-30,3531,519.5,10,0.125,USD,Happy Playcrows,RunUp INC,65
2023-05-01,3532,143.96,10,0.125,USD,Happy Playcrows,RunUp INC,62
        """
        file_content = BytesIO(test_data)

        # When
        process_invoice_file(file_content.getvalue())

        # Then
        invoices = Invoice.objects.all()
        assert invoices.count() == 2

        invoice1 = invoices.get(invoice_number='3531')
        assert invoice1.date.strftime('%Y-%m-%d') == '2023-04-30'
        assert invoice1.value == Decimal('519.5')
        assert invoice1.haircut_percent == Decimal('10')
        assert invoice1.daily_fee_percent == Decimal('0.125')
        assert invoice1.currency == 'USD'
        assert invoice1.revenue_source == 'Happy Playcrows'
        assert invoice1.customer == 'RunUp INC'
        assert invoice1.expected_payment_duration == 65

        invoice2 = invoices.get(invoice_number='3532')
        assert invoice2.date.strftime('%Y-%m-%d') == '2023-05-01'
        assert invoice2.value == Decimal('143.96')
        assert invoice2.haircut_percent == Decimal('10')
        assert invoice2.daily_fee_percent == Decimal('0.125')
        assert invoice2.currency == 'USD'
        assert invoice2.revenue_source == 'Happy Playcrows'
        assert invoice2.customer == 'RunUp INC'
        assert invoice2.expected_payment_duration == 62
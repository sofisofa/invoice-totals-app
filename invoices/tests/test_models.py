import pytest
from invoices.models import Invoice

@pytest.mark.django_db
class TestInvoiceModel:
    @pytest.fixture()
    def stub_invoice(self):
        invoice = Invoice.objects.create(
            date="2023-04-30",
            invoice_number="3531",
            value=519.5,
            haircut_percent=10,
            daily_fee_percent=0.125,
            currency="USD",
            revenue_source="Happy Playcrows",
            customer="RunUp INC",
            expected_payment_duration=65
        )
        return invoice
    
    def test_invoice_creation(self, stub_invoice):
        invoice = stub_invoice
        assert invoice.invoice_number=="3531"
        
    def test_invoice_advance(self, stub_invoice):
        invoice = stub_invoice
        assert invoice.advance==467.55
        
    def test_invoice_expected_fee(self, stub_invoice):
        invoice = stub_invoice
        assert invoice.expected_fee == 42.209375
        
    def test_invoice_str(self, stub_invoice):
        invoice = stub_invoice
        assert invoice.__str__() == f"3531: Happy Playcrows, RunUp INC"
from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_number = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    haircut_percent = models.DecimalField(max_digits=5, decimal_places=2)
    daily_fee_percent = models.DecimalField(max_digits=5, decimal_places=3)
    currency = models.CharField(max_length=3)
    revenue_source = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    expected_payment_duration = models.IntegerField()

    @property
    def advance(self):
        return self.value * (1 - self.haircut_percent / 100)

    @property
    def expected_fee(self):
        return self.value * (self.daily_fee_percent / 100) * self.expected_payment_duration

    def __str__(self):
        return f"{self.invoice_number}: {self.revenue_source}, {self.customer}"

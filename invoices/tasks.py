import pandas as pd
from celery import shared_task
from io import BytesIO
from .models import Invoice

@shared_task
def process_invoice_file(file_content):
    df = pd.read_csv(BytesIO(file_content))
    for _, row in df.iterrows():
        Invoice.objects.create(
            date=row['date'],
            invoice_number=row['invoice number'],
            value=row['value'],
            haircut_percent=row['haircut percent'],
            daily_fee_percent=row['Daily fee percent'],
            currency=row['currency'],
            revenue_source=row['Revenue source'],
            customer=row['customer'],
            expected_payment_duration=row['Expected payment duration']
        )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .tasks import process_invoice_file
from .models import Invoice
from django.db.models import Sum, F, ExpressionWrapper, DecimalField

class UploadInvoiceView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_content = file.read()
        process_invoice_file.delay(file_content)
        return Response({"message": "File uploaded and is being processed"}, status=status.HTTP_202_ACCEPTED)

class SummaryView(APIView):
    def get(self, request, *args, **kwargs):
        summary = Invoice.objects.values('revenue_source').annotate(
            total_value=Sum('value'),
            total_advance=Sum(ExpressionWrapper(F('value') * (1 - F('haircut_percent') / 100), output_field=DecimalField())),
            total_expected_fee=Sum(ExpressionWrapper(F('value') * (F('daily_fee_percent') / 100) * F('expected_payment_duration'), output_field=DecimalField()))
        )
        return render(request, 'invoices/summary.html', {'summary': summary})

class HealthCheck(APIView):
    def get(self, *args, **kwargs):
        return Response({"ping": "pong"}, status=status.HTTP_200_OK)
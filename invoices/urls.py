from django.urls import path
from .views import UploadInvoiceView, SummaryView, HealthCheck

urlpatterns = [
    path('upload/', UploadInvoiceView.as_view(), name='upload-invoice'),
    path('summary/', SummaryView.as_view(), name='summary'),
    path('healthcheck/', HealthCheck.as_view(), name='healthcheck')
]

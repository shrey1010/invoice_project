from django.urls import include, path
from rest_framework import routers
from invoice_app.views import InvoiceViewSet

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

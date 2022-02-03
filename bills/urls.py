from django.urls import path
from .views import ShowBillView, BillRegisterView, ShowOneBillView, UpdateBillView, DeleteBillView


urlpatterns = [
    path('bills', ShowBillView.as_view()),
    path('bills/register', BillRegisterView.as_view()),
    path('bills/<int:bill_id>', ShowOneBillView.as_view()),
    path('bills/<int:bill_id>/update', UpdateBillView.as_view()),
    path('bills/<int:bill_id>/delete', DeleteBillView.as_view()),
]
from django.urls import path
from .views import ShowBillView, BillRegisterView, ShowOneBillView, UpdateBillView, DeleteBillView


urlpatterns = [
    path('bills', ShowBillView.as_view(), name="show_bills"),
    path('bills/register', BillRegisterView.as_view(), name="register_bill"),
    path('bills/<int:bill_id>', ShowOneBillView.as_view(), name="show_one_bill"),
    path('bills/<int:bill_id>/update', UpdateBillView.as_view(), name="update_bill"),
    path('bills/<int:bill_id>/delete', DeleteBillView.as_view(), name="delete_bill"),
]
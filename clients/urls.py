from django.urls import path
from .views import ShowClientView, ClientRegisterView, ShowOneClientView, UpdateClientView, DeleteClientView, ClientMassiveUploadView, ClientBillsDownloadView

urlpatterns = [
    path('clients', ShowClientView.as_view(), name='show_clients'),
    path('clients/register', ClientRegisterView.as_view(), name='register_client'),
    path('clients/<int:client_id>', ShowOneClientView.as_view(), name='show_one_client'),
    path('clients/<int:client_id>/update', UpdateClientView.as_view(), name='update_client'),
    path('clients/<int:client_id>/delete', DeleteClientView.as_view(), name='delete_client'),
    path('clients/massiveupload', ClientMassiveUploadView.as_view(), name='massive_upload_clients'),
    path('clients/billsdownload', ClientBillsDownloadView.as_view(), name='bills_download_clients'),
]
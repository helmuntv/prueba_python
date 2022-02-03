from django.urls import path
from .views import ShowClientView, ClientRegisterView, ShowOneClientView, UpdateClientView, DeleteClientView, ClientMassiveUploadView, ClientBillsDownloadView


urlpatterns = [
    #path('login', LoginView.as_view()),
    path('clients', ShowClientView.as_view()),
    path('clients/register', ClientRegisterView.as_view()),
    path('clients/<int:client_id>', ShowOneClientView.as_view()),
    path('clients/<int:client_id>/update', UpdateClientView.as_view()),
    path('clients/<int:client_id>/delete', DeleteClientView.as_view()),
    path('clients/massiveupload', ClientMassiveUploadView.as_view()),
    path('clients/billsdownload', ClientBillsDownloadView.as_view()),
]
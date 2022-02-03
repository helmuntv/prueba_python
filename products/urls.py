from django.urls import path
from .views import ShowProductView, ProductRegisterView, ShowOneProductView, UpdateProductView, DeleteProductView


urlpatterns = [
    path('products', ShowProductView.as_view()),
    path('products/register', ProductRegisterView.as_view()),
    path('products/<int:product_id>', ShowOneProductView.as_view()),
    path('products/<int:product_id>/update', UpdateProductView.as_view()),
    path('products/<int:product_id>/delete', DeleteProductView.as_view()),
]
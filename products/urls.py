from django.urls import path
from .views import ShowProductView, ProductRegisterView, ShowOneProductView, UpdateProductView, DeleteProductView


urlpatterns = [
    path('products', ShowProductView.as_view(), name="show_products"),
    path('products/register', ProductRegisterView.as_view(), name="register_product"),
    path('products/<int:product_id>', ShowOneProductView.as_view(), name="show_one_product"),
    path('products/<int:product_id>/update', UpdateProductView.as_view(), name="update_product"),
    path('products/<int:product_id>/delete', DeleteProductView.as_view(), name="delete_product"),
]
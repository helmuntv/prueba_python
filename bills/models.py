import django
from django.db import models
from clients.models import Client
from products.models import Product


class Bill(models.Model):

    client_id    = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    nit          = models.CharField(max_length=20)
    code         = models.IntegerField(unique=True)
    products     = models.ManyToManyField(Product, related_name="bill_products")
    is_active    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True, auto_now_add=False)

    REQUIRED_FIELDS = ['client_id','company_name','nit','code','products']
    
    class Meta:
        db_table = 'bills'
from django.db import models

# Create your models here.
class Product(models.Model):

    name        = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, auto_now_add=False)

    REQUIRED_FIELDS = ['name','description']
    
    class Meta:
        db_table = 'products'
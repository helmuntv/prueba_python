from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):

    document   = models.CharField(max_length=20)
    first_name = models.CharField(max_length=60)
    last_name  = models.CharField(max_length=60)
    email      = models.EmailField(max_length=255, unique=True)
    password   = models.CharField(max_length=255)
    is_active  = models.BooleanField(default=True)
    username   = None


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','password']

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table = 'clients'
    
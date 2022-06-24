from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid



# Create your models here.

class Workers(models.Model):
    first_name      = models.CharField(max_length = 150)
    last_name       = models.CharField(max_length = 150)
    email           = models.CharField(max_length = 150)
    phone_number    = models.CharField(max_length = 150)
    hire_date       = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    location        = models.CharField(max_length = 150,default='Israel')

    def __str__(self):
        return self.first_name

class


    
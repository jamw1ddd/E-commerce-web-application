from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class Products(BaseModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=200)
    decription = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    on_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Order(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # This ensures the model points to the custom user model
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
 

    def __str__(self):
        return self.name

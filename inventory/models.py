from django.db import models
from datetime import datetime
# Create your models here.


class Supplier (models.Model):

    name= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
class Product (models.Model):

    regdate = models.DateField(default =datetime.now())
    category = models.CharField(max_length=100)
    brand =models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    price= models.FloatField(max_length=11)
    stock= models.IntegerField()
    # supplier = models.ForeignKey(Supplier, null=False,blank= False, on_delete =  models.CASCADE, related_name="Supplier", default= 1)

class Meta:
    db_table = "Product"

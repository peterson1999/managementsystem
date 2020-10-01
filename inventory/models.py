from django.db import models
from django.utils import timezone
# Create your models here.


class Supplier (models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Product (models.Model):

    regdate = models.DateField(default=timezone.now)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=11)
    stock = models.IntegerField()
    # image = models.ImageField(upload_to='static/images/', default=None)

    # supplier = models.ForeignKey(Supplier, null=False,blank= False, on_delete =  models.CASCADE, related_name="Supplier", default= 1)


    class Meta:
        db_table = "Product"

class MultiImage(models.Model):
    product_id=models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='static/images/', default=None)

    class Meta: 
        db_table = "Product-Images"
    
    def delete(self,*args,**kwaargs):
        self.image.delete()
        super().delete(*args, **kwaargs)

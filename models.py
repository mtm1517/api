from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Catelogy(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=500)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='images/', default=None)
    id_catelogy = models.ForeignKey(Catelogy, on_delete=models.CASCADE, default=None)
    status = models.BooleanField(default=True)




class Shipping(models.Model):
    tracking_number = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.tracking_number

class Order(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id_product = models.ManyToManyField(Product)
    total_items = models.IntegerField()
    total_amount = models.FloatField(null=True, blank=True, default=None)
    id_shipping = models.ForeignKey(Shipping, default=None, on_delete=models.CASCADE)

class Rating(models.Model):
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('id_user','id_product'),)
        index_together = (('id_user','id_product'),)

    def __str__(self):
        return self.stars








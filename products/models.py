from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    imag_url = models.URLField(max_length=1024, null = True, blank = True)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.name
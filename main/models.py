from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    packaging = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    description = models.TextField()
    benefit = models.TextField( null=True, blank=True)
    application_field  = models.TextField( null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'slug')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        unique_together = ('name', 'slug')

    def __str__(self):
        return self.name


class County(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Location(models.Model):
    name= models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Dealers(models.Model):
    
    dealer_name = models.CharField(max_length=100, null=True, blank=True )
    hardware_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField()
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.hardware_name} - {self.dealer_name} "


class Subscribers_Email(models.Model):
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.email



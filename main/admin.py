from django.contrib import admin
from . models import Product, Category, Dealers, County, Location

# Register your models here.
admin.site.register(Product)

admin.site.register(Category)

admin.site.register(Dealers)

admin.site.register(County)

admin.site.register(Location)


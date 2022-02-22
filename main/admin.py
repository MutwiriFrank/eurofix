from django.contrib import admin
from . models import Product, Category, Dealers, Subscribers_Email,  County, Location
from import_export.admin import ExportActionMixin

# Register your models here.

class EmailAdmin(ExportActionMixin, admin.ModelAdmin):
    pass

admin.site.register(Product)

admin.site.register(Category)

admin.site.register(Dealers)

admin.site.register(County)

admin.site.register(Location)

admin.site.register(Subscribers_Email, EmailAdmin)


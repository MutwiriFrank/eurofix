# Generated by Django 3.2.3 on 2022-01-19 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_application_field_product_application_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='benefits',
            new_name='benefit',
        ),
    ]

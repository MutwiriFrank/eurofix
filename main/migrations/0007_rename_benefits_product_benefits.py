# Generated by Django 3.2.3 on 2022-01-18 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220117_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Benefits',
            new_name='benefits',
        ),
    ]

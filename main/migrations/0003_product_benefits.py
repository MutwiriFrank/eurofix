# Generated by Django 3.2.3 on 2022-01-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_dealers'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Benefits',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

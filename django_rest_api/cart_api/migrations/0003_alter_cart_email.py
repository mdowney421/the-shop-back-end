# Generated by Django 4.0.5 on 2022-06-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_api', '0002_cart_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='email',
            field=models.TextField(),
        ),
    ]

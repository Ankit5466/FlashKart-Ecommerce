# Generated by Django 4.2.2 on 2023-07-13 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=500),
        ),
    ]

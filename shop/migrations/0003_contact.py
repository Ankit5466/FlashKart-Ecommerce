# Generated by Django 4.2.2 on 2023-07-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_category_products_images_products_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=12)),
                ('desc', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]

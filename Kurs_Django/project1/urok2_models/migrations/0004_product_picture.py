# Generated by Django 5.0.4 on 2024-04-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urok2_models', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]

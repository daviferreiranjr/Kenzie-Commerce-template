# Generated by Django 4.2.3 on 2023-07-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_value',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]

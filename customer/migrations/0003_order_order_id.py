# Generated by Django 5.0.6 on 2024-08-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0044_review_reviewdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='offer_price',
            field=models.FloatField(null=True),
        ),
    ]
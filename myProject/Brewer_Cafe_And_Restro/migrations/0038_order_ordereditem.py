# Generated by Django 4.1.3 on 2023-01-25 19:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0037_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('idorder', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('order_delivery_date', models.DateField(default=datetime.date.today)),
                ('order_delivery_address', models.TextField()),
                ('city', models.CharField(max_length=150)),
                ('total_amount', models.FloatField()),
                ('order_payment_method', models.CharField(max_length=150)),
                ('payment_id', models.CharField(max_length=250, null=True)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Out for shipping', 'Out for shipping'), ('Completed', 'Completed')], default='Pending', max_length=150)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('area_pincode', models.ForeignKey(db_column='area_pincode', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.area')),
                ('user_iduser', models.ForeignKey(db_column='user_iduser', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.user')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('item_iditem', models.ForeignKey(db_column='item_iditem', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.item')),
                ('order_idorder', models.ForeignKey(db_column='order_idorder', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brewer_Cafe_And_Restro.order')),
            ],
            options={
                'db_table': 'ordered_item',
                'managed': True,
            },
        ),
    ]
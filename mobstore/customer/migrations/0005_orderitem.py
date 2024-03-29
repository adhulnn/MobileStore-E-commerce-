# Generated by Django 4.1.7 on 2023-04-02 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_profile_store_name'),
        ('customer', '0004_alter_cartitem_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.mobile')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.order')),
            ],
        ),
    ]

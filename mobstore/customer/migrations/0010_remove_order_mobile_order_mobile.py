# Generated by Django 4.1.7 on 2023-04-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_profile_store_name'),
        ('customer', '0009_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mobile',
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.ManyToManyField(null=True, to='store.mobile'),
        ),
    ]

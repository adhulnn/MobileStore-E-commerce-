# Generated by Django 4.1.7 on 2023-04-07 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_profile_store_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='datetime',
            new_name='createdat',
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='mobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='R_mobile', to='store.mobile'),
        ),
    ]

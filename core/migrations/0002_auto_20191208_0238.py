# Generated by Django 2.2.7 on 2019-12-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flor',
            name='descripcion',
            field=models.TextField(default='Sin Descripcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flor',
            name='estado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flor',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

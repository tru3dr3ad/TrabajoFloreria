# Generated by Django 2.2.7 on 2019-12-08 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191208_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='flor',
            name='imagen',
            field=models.ImageField(default='/core/static/img/1.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]

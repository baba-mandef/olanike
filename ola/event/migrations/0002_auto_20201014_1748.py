# Generated by Django 3.1.2 on 2020-10-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=models.ImageField(upload_to='events_pics'),
        ),
    ]

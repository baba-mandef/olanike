# Generated by Django 3.1.2 on 2020-10-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('banner', models.ImageField(upload_to='static/img/event')),
                ('start_at', models.DateTimeField()),
                ('finish_at', models.DateTimeField()),
                ('adress', models.CharField(max_length=255)),
            ],
        ),
    ]

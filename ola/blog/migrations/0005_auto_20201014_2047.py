# Generated by Django 3.1.2 on 2020-10-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201014_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_pic',
            field=models.ImageField(upload_to='comments_pics'),
        ),
    ]
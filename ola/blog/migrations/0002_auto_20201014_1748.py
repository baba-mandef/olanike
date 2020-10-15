# Generated by Django 3.1.2 on 2020-10-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(upload_to='author_pics'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_pic',
            field=models.ImageField(default='static/img/blog/comment/d.png', upload_to='comments_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(upload_to='blog_pics'),
        ),
    ]
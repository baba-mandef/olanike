# Generated by Django 3.1.2 on 2021-01-23 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cause', '0004_cause_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='don',
            name='quote',
        ),
        migrations.AddField(
            model_name='cause',
            name='slug',
            field=models.SlugField(default='nfnj', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='don',
            name='cause',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='cause.cause'),
            preserve_default=False,
        ),
    ]

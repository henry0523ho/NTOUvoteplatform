# Generated by Django 3.2.5 on 2021-07-05 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='author',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='published',
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-03 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_likeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='author',
        ),
        migrations.RemoveField(
            model_name='events',
            name='photo',
        ),
    ]

# Generated by Django 4.0.4 on 2023-05-02 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_events_author_alter_likeuser_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='events',
            name='like',
        ),
    ]
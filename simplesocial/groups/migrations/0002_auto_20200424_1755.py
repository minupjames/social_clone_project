# Generated by Django 3.0.5 on 2020-04-24 17:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together={('group', 'user')},
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-16 10:05

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190616_0959'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('number_of_childs', django.db.models.manager.Manager()),
            ],
        ),
    ]
# Generated by Django 2.2.7 on 2019-12-04 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20191121_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='link',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
    ]
# Generated by Django 4.2 on 2023-04-18 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Thread', '0002_thread_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='name',
        ),
    ]
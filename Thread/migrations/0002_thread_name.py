# Generated by Django 4.2 on 2023-04-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thread', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='name',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
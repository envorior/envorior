# Generated by Django 5.0.1 on 2024-05-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posteddate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
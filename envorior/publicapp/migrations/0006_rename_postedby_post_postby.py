# Generated by Django 5.0.1 on 2024-03-09 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0005_remove_profile_reward_post_reward'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postedby',
            new_name='postby',
        ),
    ]

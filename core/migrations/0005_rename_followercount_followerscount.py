# Generated by Django 4.0.4 on 2022-07-09 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followercount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FollowerCount',
            new_name='FollowersCount',
        ),
    ]

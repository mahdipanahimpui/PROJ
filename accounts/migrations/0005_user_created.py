# Generated by Django 4.2.4 on 2023-08-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_groups_user_is_superuser_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_alter_person_birthday_alter_person_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_complete_data',
            field=models.BooleanField(default=False),
        ),
    ]
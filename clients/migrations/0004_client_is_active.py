# Generated by Django 4.0.1 on 2022-01-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_managers_remove_client_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

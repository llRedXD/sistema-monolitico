# Generated by Django 4.0.4 on 2022-06-08 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0006_alter_teste_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b8f165c8-c0dc-4b58-8a37-939069bef6da'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
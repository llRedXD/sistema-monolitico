# Generated by Django 4.0.4 on 2022-06-08 12:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0004_alter_teste_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='id',
            field=models.UUIDField(default=uuid.UUID('87023c6e-6dcd-4ed5-8c7b-643069a4dc9b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]

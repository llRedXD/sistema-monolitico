# Generated by Django 4.0.4 on 2022-06-08 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_alter_teste_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='id',
            field=models.UUIDField(default=uuid.UUID('13e60e5f-2d5c-46b9-820c-df7cbb7e1b90'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
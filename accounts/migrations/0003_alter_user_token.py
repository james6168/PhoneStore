# Generated by Django 4.1.6 on 2023-02-07 13:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default=uuid.UUID('d17544a4-b683-4ce2-ae87-d8c9d6eb5f6a'), max_length=36),
        ),
    ]

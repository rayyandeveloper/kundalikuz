# Generated by Django 5.0.3 on 2024-03-23 06:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_content_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

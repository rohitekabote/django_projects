# Generated by Django 5.1.5 on 2025-01-29 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_comments_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='travello.comments'),
        ),
    ]

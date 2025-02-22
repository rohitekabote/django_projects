# Generated by Django 5.1.5 on 2025-02-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_comments_dislikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('visited_destinations', models.ManyToManyField(blank=True, to='travello.destination')),
            ],
        ),
    ]

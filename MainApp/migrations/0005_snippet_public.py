# Generated by Django 5.0.7 on 2024-07-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_snippet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]

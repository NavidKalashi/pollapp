# Generated by Django 5.0.1 on 2024-01-24 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_text',
            new_name='pub_date',
        ),
    ]

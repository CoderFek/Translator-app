# Generated by Django 5.0.1 on 2024-01-31 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator_app', '0003_alter_translation_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translation',
            old_name='target_text',
            new_name='translated_text',
        ),
    ]

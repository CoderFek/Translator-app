# Generated by Django 5.0.1 on 2024-01-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_text', models.TextField()),
                ('source_lang', models.CharField(max_length=30)),
                ('target_lang', models.CharField(max_length=30)),
                ('target_text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

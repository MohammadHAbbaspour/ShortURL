# Generated by Django 3.2.6 on 2021-08-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_address', models.URLField(blank=True)),
                ('short_url', models.URLField(blank=True)),
            ],
        ),
    ]

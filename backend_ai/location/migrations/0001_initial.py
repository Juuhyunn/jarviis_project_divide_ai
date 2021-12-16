# Generated by Django 3.2.5 on 2021-11-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('category', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'location',
            },
        ),
    ]

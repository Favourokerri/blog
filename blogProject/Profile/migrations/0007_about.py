# Generated by Django 5.0 on 2023-12-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_contact_whatsapp_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
            ],
        ),
    ]

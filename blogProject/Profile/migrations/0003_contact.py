# Generated by Django 5.0 on 2023-12-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('facebook_link', models.URLField()),
                ('instagram_lint', models.URLField()),
                ('twitter_link', models.URLField()),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-30 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=20, null=True)),
                ('Description', models.CharField(blank=True, max_length=20, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='dp')),
            ],
        ),
    ]

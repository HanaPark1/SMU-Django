# Generated by Django 4.2.21 on 2025-05-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('grade', models.ImageField(default=1, upload_to='')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]

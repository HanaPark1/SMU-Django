# Generated by Django 4.2.21 on 2025-05-27 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('grade', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]

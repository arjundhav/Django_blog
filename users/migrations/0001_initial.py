# Generated by Django 3.2.4 on 2021-09-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=300)),
                ('password2', models.CharField(max_length=300)),
                ('mobile', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]

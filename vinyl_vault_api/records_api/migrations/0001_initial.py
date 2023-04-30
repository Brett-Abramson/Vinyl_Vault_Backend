# Generated by Django 4.2 on 2023-04-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('year_released', models.IntegerField()),
            ],
        ),
    ]
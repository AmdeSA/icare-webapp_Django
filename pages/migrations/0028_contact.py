# Generated by Django 3.0.5 on 2020-04-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_auto_20200426_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=100)),
                ('phone', models.IntegerField(verbose_name=15)),
                ('email', models.TextField(max_length=25)),
            ],
        ),
    ]
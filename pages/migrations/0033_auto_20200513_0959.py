# Generated by Django 3.0.5 on 2020-05-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_auto_20200513_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=25),
        ),
    ]
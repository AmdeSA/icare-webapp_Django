# Generated by Django 3.0.5 on 2020-04-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.SmallIntegerField(),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_portfolio_content_service_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_content',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='service_content',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

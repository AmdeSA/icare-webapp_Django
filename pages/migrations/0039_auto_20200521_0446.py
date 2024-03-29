# Generated by Django 3.0.5 on 2020-05-21 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='file',
            field=models.FileField(upload_to='static/references'),
        ),
    ]

# Generated by Django 4.2.6 on 2024-02-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]

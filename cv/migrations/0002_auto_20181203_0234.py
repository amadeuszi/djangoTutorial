# Generated by Django 2.1.3 on 2018-12-03 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='penalty',
            name='diet_strike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='penalty',
            name='name',
            field=models.TextField(default='user'),
        ),
        migrations.AddField(
            model_name='penalty',
            name='non_smoking_strike',
            field=models.IntegerField(default=0),
        ),
    ]

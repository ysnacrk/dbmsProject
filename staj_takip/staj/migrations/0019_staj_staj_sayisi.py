# Generated by Django 2.0.3 on 2018-12-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staj', '0018_remove_konular_deneme'),
    ]

    operations = [
        migrations.AddField(
            model_name='staj',
            name='staj_sayisi',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

# Generated by Django 2.0.3 on 2018-12-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staj', '0008_auto_20181211_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='o_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

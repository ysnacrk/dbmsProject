# Generated by Django 2.0.3 on 2018-11-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staj', '0002_auto_20181110_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='o_ogretim',
            field=models.CharField(choices=[('1.', '1'), ('2.', '2')], max_length=20),
        ),
    ]
# Generated by Django 2.1.3 on 2019-01-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staj', '0038_auto_20190101_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='staj',
            name='gorusme_eklendi_mi',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
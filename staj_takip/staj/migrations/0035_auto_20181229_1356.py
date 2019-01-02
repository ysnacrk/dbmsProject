# Generated by Django 2.1.3 on 2018-12-29 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staj', '0034_auto_20181229_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staj',
            name='baslama_tarihi',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staj',
            name='bitis_tarihi',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staj',
            name='konu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staj.Konular'),
        ),
        migrations.AlterField(
            model_name='staj',
            name='sinif_durumu',
            field=models.CharField(blank=True, choices=[('1,', '1'), ('2,', '2'), ('3,', '3'), ('4,', '4')], max_length=50, null=True),
        ),
    ]

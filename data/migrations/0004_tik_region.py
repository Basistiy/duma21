# Generated by Django 3.2.7 on 2021-10-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_oik_region_tik'),
    ]

    operations = [
        migrations.AddField(
            model_name='tik',
            name='region',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

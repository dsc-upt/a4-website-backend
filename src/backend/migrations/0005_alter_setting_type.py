# Generated by Django 3.2.4 on 2021-10-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20211018_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('IMAGE', 'Image')], default='TEXT', max_length=5),
        ),
    ]
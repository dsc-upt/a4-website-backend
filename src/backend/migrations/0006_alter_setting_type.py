# Generated by Django 3.2.4 on 2021-12-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('IMAGE', 'Image')], default='TEXT', max_length=5),
        ),
    ]

# Generated by Django 3.2.4 on 2021-09-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_faq_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('value', models.TextField(max_length=300)),
                ('type', models.CharField(choices=[('TEXT', 'Text'), ('IMAGE', 'Image')], default='TEXT', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
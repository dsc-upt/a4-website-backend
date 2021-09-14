# Generated by Django 3.2.4 on 2021-09-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('value', models.TextField(blank=True, default='', max_length=300)),
                ('type', models.CharField(choices=[('IMAGE', 'Image'), ('TEXT', 'Text')], default='TEXT', max_length=5)),
            ],
        ),
    ]
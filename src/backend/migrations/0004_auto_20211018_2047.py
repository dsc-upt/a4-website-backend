# Generated by Django 3.2.4 on 2021-10-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210914_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='setting',
            name='id',
        ),
        migrations.AddField(
            model_name='setting',
            name='slug',
            field=models.SlugField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setting',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'Image'), ('TEXT', 'Text')], default='TEXT', max_length=5),
        ),
    ]
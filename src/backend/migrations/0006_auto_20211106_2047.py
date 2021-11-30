# Generated by Django 3.2.7 on 2021-11-06 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_setting_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'Image'), ('TEXT', 'Text')], default='TEXT', max_length=5),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('link', models.URLField()),
                ('type', models.CharField(choices=[('EXTERNAL', 'External Link'), ('INTERNAL', 'Internal Link'), ('SCROLL', 'Scroll To')], default='INTERNAL', max_length=9)),
                ('icon', models.URLField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.menu')),
            ],
        ),
    ]

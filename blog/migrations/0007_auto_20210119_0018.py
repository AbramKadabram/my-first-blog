# Generated by Django 3.1.5 on 2021-01-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210118_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, height_field=750, upload_to='', verbose_name='Изоброжение', width_field=300),
        ),
    ]

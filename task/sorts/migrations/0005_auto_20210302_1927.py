# Generated by Django 3.1.7 on 2021-03-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorts', '0004_auto_20210302_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sort',
            name='result',
            field=models.FileField(default='', upload_to='', verbose_name='Result file'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorts', '0007_auto_20210302_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sort',
            name='result',
            field=models.FileField(default='', upload_to='media/', verbose_name='Result file'),
        ),
    ]
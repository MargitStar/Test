# Generated by Django 3.1.7 on 2021-03-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorts', '0006_auto_20210302_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sort',
            name='initial',
            field=models.FileField(upload_to='', verbose_name='Initial file'),
        ),
    ]

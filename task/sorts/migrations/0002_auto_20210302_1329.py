# Generated by Django 3.1.7 on 2021-03-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sort',
            name='bubble',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='insertion',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='merge',
        ),
        migrations.RemoveField(
            model_name='sort',
            name='optimized_bubble',
        ),
        migrations.AddField(
            model_name='sort',
            name='type',
            field=models.CharField(default='', max_length=100, verbose_name='Type'),
        ),
    ]

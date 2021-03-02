from django.db import models
from django.contrib import admin


class Sort(models.Model):
    initial = models.FileField(
        'Initial file',
    )

    result = models.FileField(
        'Result file'
    )

    speed = models.CharField(
        'Execution time',
        max_length=100,
        default='',
    )

    type = models.CharField(
        'Type',
        max_length=100,
        default='',
    )

    def __str__(self):
        return f"Object {self.pk}"


class SearchSortType(admin.ModelAdmin):
    search_fields = ['type']

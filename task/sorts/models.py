from django.db import models
from django.contrib import admin


class Sort(models.Model):
    initial = models.FileField(
        'Initial file',
    )

    result = models.FileField(
        'Result file',
        default='',
    )

    speed = models.CharField(
        'Execution time',
        max_length=100,
        default='',
    )

    CHOICES = [
        ('Bubble sort', 'Bubble sort'),
        ('Optimized Bubble sort', 'Optimized Bubble sort'),
        ('Insertion sort', 'Insertion sort'),
        ('Merge sort', 'Merge sort'),
    ]

    type = models.CharField(
        'Type',
        choices=CHOICES,
        max_length=100,
        default='',
    )

    def __str__(self):
        return f"Object {self.pk}"


class SearchSortType(admin.ModelAdmin):
    search_fields = ['initial', 'result', 'speed', 'type']
    list_filter = ['type']

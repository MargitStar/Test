from django.contrib import admin

from .models import Sort, SearchSortType

admin.site.register(Sort, SearchSortType)


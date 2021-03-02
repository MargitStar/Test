from django.urls import path
from .views import SortView

app_name = 'sorters'

urlpatterns = [
    path('sort/', SortView.as_view(), name='sort')
]

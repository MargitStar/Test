from django.shortcuts import render
from django.views.generic import CreateView
from .models import Sort
from .forms import SortForm


class SortView(CreateView):
    template_name = 'sorts/index.html'
    model = Sort
    form_class = SortForm


import os

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files import File, uploadedfile
from django.views.generic import UpdateView, CreateView
from .models import Sort
from .forms import SortForm
from . import sorting_classes


def make_file(func, my_object, elements):
    new_elements = func(elements).sorted()
    buf = sorting_classes.write_file(new_elements)
    buf.seek(0, 2)
    result_file = uploadedfile.InMemoryUploadedFile(
        buf, 'result', f'file{my_object.pk}.txt', None, buf.tell(), None)
    my_object.result.save(result_file.name, result_file)


class SortView(CreateView):
    template_name = 'sorts/index.html'
    model = Sort
    form_class = SortForm
    success_url = '/admin'

    def get_success_url(self):

        my_object = Sort.objects.latest('pk')
        print(my_object)
        if my_object:
            opened_file = File(open(os.path.join('media/', my_object.initial.name), 'r'))
            print(opened_file)
            elements = sorting_classes.read_file(opened_file)
            if my_object.type == 'Bubble sort':
                make_file(sorting_classes.BubbleSort, my_object, elements)
            elif my_object.type == 'Optimized Bubble sort':
                make_file(sorting_classes.OptimizedBubbleSort, my_object, elements)
            elif my_object.type == 'Merge sort':
                make_file(sorting_classes.MergeSort, my_object, elements)
            else:
                make_file(sorting_classes.InsertionSort, my_object, elements)

            return f"/media/{my_object.result.name}"

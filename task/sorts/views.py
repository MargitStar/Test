import os

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files import File, uploadedfile
from django.views.generic import UpdateView
from .models import Sort
from .forms import SortForm
from . import sorting_classes


class SortView(UpdateView):
    template_name = 'sorts/index.html'
    model = Sort
    form_class = SortForm
    success_url = '/admin'

    def get_object(self, queryset=None):
        object_id = self.request.session.get('object_id')
        print('object_id', object_id)

        # if object_id:
        my_object = Sort.objects.filter(pk=20).first()
        print(my_object)
        if my_object:
            opened_file = File(open(os.path.join('media/', my_object.initial.name), 'r'))
            print(opened_file)
            elements = sorting_classes.read_file(opened_file)

            print(os.path.join(my_object.initial.name))
            if my_object.type == 'Bubble sort':
                new_elements = sorting_classes.BubbleSort(elements).sorted()
                buf = sorting_classes.write_file(new_elements)
                buf.seek(0, 2)
                result_file = uploadedfile.InMemoryUploadedFile(
                    buf, 'result', f'file{my_object.pk}.txt', None, buf.tell(), None)
                my_object.result.save(result_file.name, result_file)
            elif my_object.type == 'Optimized Bubble sort':
                new_elements = sorting_classes.OptimizedBubbleSort(elements).sorted()
                buf = sorting_classes.write_file(new_elements)
                buf.seek(0, 2)
                result_file = uploadedfile.InMemoryUploadedFile(
                    buf, 'result', f'file{my_object.pk}.txt', None, buf.tell(), None)
                my_object.result.save(result_file.name, result_file)
            elif my_object.type == 'Merge sort':
                new_elements = sorting_classes.MergeSort(elements).sorted()
                buf = sorting_classes.write_file(new_elements)
                buf.seek(0, 2)
                result_file = uploadedfile.InMemoryUploadedFile(
                    buf, 'result', f'file{my_object.pk}.txt', None, buf.tell(), None)
                my_object.result.save(result_file.name, result_file)
            else:
                new_elements = sorting_classes.InsertionSort(elements).sorted()
                buf = sorting_classes.write_file(new_elements)
                buf.seek(0, 2)
                result_file = uploadedfile.InMemoryUploadedFile(
                    buf, 'result', f'file{my_object.pk}.txt', None, buf.tell(), None)
                my_object.result.save(result_file.name, result_file)

        return my_object

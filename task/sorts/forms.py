from django import forms
from .models import Sort


class SortForm(forms.ModelForm):
    class Meta:
        model = Sort
        fields = [
            'initial',
            'type'
        ]

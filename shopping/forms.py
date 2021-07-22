from django import forms
from .models import Cart_list
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class Cart_listForm(forms.ModelForm):
    class Meta:
        model = Cart_list
        fields = ('item_name', 'item_quantity', 'item_status',
                  'date')

        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'item_quantity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'item_status': forms.Select( attrs={'class': 'form-control form-control-lg'}),
            'date': DateInput(format='%d/%m/%Y')

        }


class EditCart_listForm(forms.ModelForm):
    class Meta:
        model = Cart_list
        fields = ('item_name', 'item_quantity', 'item_status',
                  'date')

        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'item_quantity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'item_status': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'date': DateInput(format='%d/%m/%Y')

        }

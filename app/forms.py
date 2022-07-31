from django.forms import forms
from django.forms import ModelForm
from app.models import Customers


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})








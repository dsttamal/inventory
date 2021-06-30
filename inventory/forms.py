from django import forms  
from inventory.models import *

class ClientsForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder':"Name", 'id': 'clients-name', 'class': 'form-control', 'required': 'true'})
        self.fields['phn'].widget.attrs.update(
            {'placeholder':"Phone", 'onkeypress':"return isNumberKey(event)", 'id': 'clients-phone', 'class': 'form-control', 'required': 'true'})
        self.fields['adress'].widget.attrs.update(
            {'placeholder':"Address", 'id': 'clients-address', 'class': 'form-control', 'required': 'true'})
    class Meta:  
        model = clients  
        fields = ['name', 'phn', 'adress'] 

class SuppliersForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder':"Name", 'id': 'suppliers-name', 'class': 'form-control', 'required': 'true'})
        self.fields['phn'].widget.attrs.update(
            {'placeholder':"Phone", 'onkeypress':"return isNumberKey(event)", 'id': 'suppliers-phone', 'class': 'form-control', 'required': 'true'})
        self.fields['adress'].widget.attrs.update(
            {'placeholder':"Address", 'id': 'suppliers-address', 'class': 'form-control', 'required': 'true'})
    class Meta:  
        model = suppliers  
        fields = ['name', 'phn', 'adress'] 
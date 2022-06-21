from django import forms  
from inventory.models import *

class NumberTextInput(forms.widgets.TextInput):
    input_type = 'text'

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

class InventoryForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update(
            {'placeholder':"Name", 'id': 'product-name', 'class': 'form-control', 'required': 'true'})
        self.fields['litter'].widget.attrs.update(
            {'placeholder':"Liter", 'id': 'product-litter', 'class': 'form-control', 'onkeypress':"return isNumberKey(event)", 'required': 'true'})
        self.fields['qty'].widget.attrs.update(
            {'placeholder':"Quantity", 'id': 'product-quantity', 'class': 'form-control', 'onkeypress':"return isNumberKey(event)", 'required': 'true'})
        self.fields['pr_price'].widget.attrs.update(
            {'placeholder':"Purchase Price", 'id': 'product-pr_price', 'class': 'form-control', 'onkeypress':"return isNumberKey(event)", 'required': 'true'})

    class Meta:  
        model = Inventory  
        fields = ['product', 'litter', 'pr_price', 'sl_price', 'qty', 'supplier_invoice_id']
        widgets = {
            'litter': NumberTextInput(),
            'qty': NumberTextInput(),
            'pr_price': NumberTextInput(),
        }

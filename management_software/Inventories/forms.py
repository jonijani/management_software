from django import forms

class Inventory_form(forms.Form):
    device = forms.CharField(label='Your name', max_length=100)
    make = forms.CharField(label='Your name', max_length=100)
    model = forms.CharField(label='Your name', max_length=100)
    part_name = forms.CharField(label='Your name', max_length=100)
    part_color = forms.CharField(label='Your name', max_length=100)
    supplier = forms.CharField(label='Your name', max_length=100)
    quantity = forms.CharField(label='Your name', max_length=100)
    cost = forms.CharField(label='Your name', max_length=100)
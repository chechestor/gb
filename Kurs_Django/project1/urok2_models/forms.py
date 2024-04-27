from django import forms
from .models import Product

class ImageAddForm(forms.Form):
    product_id = forms.IntegerField(min_value=0)
    image = forms.ImageField()


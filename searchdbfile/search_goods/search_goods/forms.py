# search_goods/forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Select a file')

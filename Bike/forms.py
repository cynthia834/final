from django import forms
from .models import Bicycle, CheckIn, ImageModel


class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = ['owner_name', 'bicycle_name', 'time_taken', 'price', 'image']


class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['name', 'phone', 'type']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']

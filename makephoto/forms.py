from django import forms
from .models import PhotoModel


class PhotoForm(forms.Form):
    photo = forms.ImageField()

    def save(self):
        photo = PhotoModel(**self.cleaned_data)
        photo.save()
        return photo

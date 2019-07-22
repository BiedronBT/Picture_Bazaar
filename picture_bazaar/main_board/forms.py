from django import forms
from .models import Picture

class UploadPictureForm(forms.ModelForm):

    title = forms.CharField(max_length=63, help_text='Up to 63 characters')
    tags = forms.CharField(help_text='Type tags related to uploaded picture separated by comas')

    class Meta:
        model = Picture
        fields = ['image', 'title', 'tags']


class EditPictureForm(forms.ModelForm):

    title = forms.CharField(max_length=63, help_text='Up to 63 characters')
    tags = forms.CharField(help_text='Type tags related to uploaded picture separated by comas')

    class Meta:
        model = Picture
        fields = ['title', 'tags']
from django import forms
from .models import Avatar
from plugin.forms import  ImageFileInput

class AvatarForm(forms.ModelForm):
    

    class Meta:
        model = Avatar
        exclude = []

        widgets = {
            'image': ImageFileInput(),
        }
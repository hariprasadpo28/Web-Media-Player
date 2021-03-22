from django import forms
from .models import videos


class file_upload_form(forms.ModelForm):
    class Meta:
        model = videos
        fields = ['name', 'datafile', 'private']

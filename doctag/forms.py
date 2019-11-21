from django import forms
from .models import docTagg

class docTaggForm(forms.ModelForm):
    
    class Meta:
        model = docTagg
        fields = ("docName","tags")
    

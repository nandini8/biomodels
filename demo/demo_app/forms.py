from django import forms 
from .models import biomodel

class BioModelForm(forms.ModelForm):
    class Meta:
        model = biomodel
        fields = '__all__'


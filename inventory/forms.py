from django import forms
from .models import Monument

class MonumentForm(forms.ModelForm):
    class Meta:
        model = Monument
        fields = ['name', 'category', 'weight', 'length', 'width', 'height', 'quantity', 'status']

# c:\Proyectos\pusuqui\iap\pusukids\forms.py
from django import forms
from .models import coordinator, group

class CoordinatorForm(forms.ModelForm):
    class Meta:
        model = coordinator
        fields = ['name', 'surname']
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = group
        fields = ['name', 'description']        
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

# c:\Proyectos\pusuqui\iap\pusukids\forms.py
from django import forms
from .models import coordinator, group, server, groupage

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
class ServerForm(forms.ModelForm):
    class Meta:
        model = server
        fields = ['name', 'surname', 'coordinator', 'group']
        # Opcional: Personalizar etiquetas si lo deseas
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'coordinator': 'Coordinador(a)',
            'group': 'Grupo',
        }
        # Opcional: Añadir widgets si necesitas más control (ej. selects más bonitos)
        widgets = {
             'coordinator': forms.Select(attrs={'class': 'form-control'}),
             'group': forms.Select(attrs={'class': 'form-control'}),
        }

class GroupageForm(forms.ModelForm):
    class Meta:
        model = groupage
        fields = ['name', 'description']

    
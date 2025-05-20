
from django import forms
from .models import (
    coordinator, group, server,  child, assistance,

)


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


class ChildForm(forms.ModelForm): # <-- Renombrada
    class Meta:
        model = child # <-- Cambiado a child
        fields = ['name', 'surname', 'birthday', 'parent_name', 'contact_phone']
        # ... (labels y widgets como los tenías, asegúrate que las claves coinciden con los fields) ...
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'birthday': 'Fecha de Nacimiento',
            'parent_name': 'Nombre del Padre/Madre/Representante',
            'contact_phone': 'Teléfono de Contacto',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
        }
    
class AssistanceForm(forms.ModelForm):
    class Meta:
        model = assistance
        fields = ['child', 'date', 'group', 'coordinator', 'attended']
        labels = {
            'child': 'Niño/a',
            'date': 'Fecha de Asistencia',
            'group': 'Grupo (en esa fecha)',
            'coordinator': 'Coordinador(a) (en esa fecha)',
            'attended': '¿Asistió?',
        }
        widgets = {
            # Usar Select para las ForeignKeys
            'child': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'coordinator': forms.Select(attrs={'class': 'form-control'}),
            # Checkbox para el BooleanField
            'attended': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Opcional: Ordenar los desplegables para mejor usabilidad
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordenar niños por apellido y nombre
        self.fields['child'].queryset = child.objects.order_by('surname', 'name')
        # Ordenar fechas por la más reciente primero
        self.fields['date'].queryset = fecha.objects.order_by('-date')
        # Ordenar grupos por nombre
        self.fields['group'].queryset = group.objects.order_by('name')
        # Ordenar coordinadores por apellido y nombre
        self.fields['coordinator'].queryset = coordinator.objects.order_by('surname', 'name')

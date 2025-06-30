from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here. 

def validate_date(value):
    try:
        value.strftime('%Y-%m-%d')  # Forzar validación
    except ValueError as e:
        raise ValidationError(str(e))

class coordinator(models.Model):
    name = models.CharField(max_length=128, unique=True)
    surname = models.CharField(max_length=128)     
    def __str__(self):
        return self.name


class group(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class server(models.Model):
    name = models.CharField(max_length=128, unique=True)
    surname = models.CharField(max_length=128)
    coordinator = models.ForeignKey(coordinator, on_delete=models.PROTECT)
    group = models.ForeignKey(group, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.name

class child(models.Model):
    STATUS_CHOICES = [
        ('activo', 'Activo'),
        ('promovido', 'Promovido'),
    ]
    name = models.CharField(max_length=128, unique=True)
    surname = models.CharField(max_length=128)
    birthday = models.DateField(validators=[validate_date]) # El campo clave a probar
    parent_name = models.CharField(max_length=128, blank=True) # Hacemos algunos opcionales
    contact_phone = models.CharField(max_length=16, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='activo',
        verbose_name='Estado'
    )

    @property
    def calculated_age(self):
        if not self.birthday:
            return None
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age
    
    def __str__(self):
        return f"{self.name} {self.surname}"   
       
class assistance(models.Model):
    child = models.ForeignKey(child, on_delete=models.PROTECT) # <-- CAMBIAR A child
    date = models.DateField()
    group = models.ForeignKey(group, on_delete=models.PROTECT)
    coordinator = models.ForeignKey(coordinator, on_delete=models.PROTECT)
    attended = models.BooleanField()

    class Meta:
        # Asegura que no se pueda registrar la asistencia para el mismo niño en la misma fecha más de una vez.
        unique_together = ('child', 'date')

    def __str__(self):
         # Actualizar también aquí si es necesario
         return f"{self.child.name} - {str(self.date)}"

                

        
                     

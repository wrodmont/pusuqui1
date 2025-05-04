from django.db import models

# Create your models here.
class coordinator(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)     
    def __str__(self):
        return self.name


class group(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class server(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    coordinator = models.ForeignKey(coordinator, on_delete=models.PROTECT)
    group = models.ForeignKey(group, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
        
class groupage(models.Model):
    name = models.CharField(max_length=8)
    description = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name

class kid(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birthday = models.DateField()
    age = models.IntegerField()
    groupage = models.ForeignKey(groupage, on_delete=models.PROTECT)
    parent_name = models.CharField(max_length=128)
    contact_phone = models.CharField(max_length=16)

    
    def __str__(self):
        return self.name
        
class fecha(models.Model):
    date = models.DateField()
    week_no = models.IntegerField()
    
    def __str__(self):
        return str(self.date)
        
class assistance(models.Model):
    kid = models.ForeignKey(kid, on_delete=models.PROTECT)
    date = models.ForeignKey(fecha, on_delete=models.PROTECT)
    group = models.ForeignKey(group, on_delete=models.PROTECT)
    coordinator = models.ForeignKey(coordinator, on_delete=models.PROTECT)
    attended = models.BooleanField()
    
    def __str__(self):
        return self.kid.name + " - " + str(self.date.date)
                
class weekinfo(models.Model):
    total_kids = models.ImageField
    total_servers = models.IntegerField
    money_collected = models.FloatField
    fecha = models.ForeignKey(fecha, on_delete=models.PROTECT)
    coordinator = models.ForeignKey(coordinator, on_delete=models.PROTECT)
    group = models.ForeignKey(group, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.fecha.date
        
class expense(models.Model):
    description = models.CharField(max_length=64)
    amount = models.FloatField()
    fecha = models.ForeignKey(fecha, on_delete=models.PROTECT)    
    reference = models.CharField(max_length=16)
    
    def __str__(self):
        return self.description
        
                        
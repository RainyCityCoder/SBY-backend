from django.db import models

# Create your models here.
class Biologists(models.Model):
    name = models.CharField(max_length=1000)
    birthyear = models.CharField(max_length=4)
    class Meta:
        managed = False 
        db_table = 'biologists'
    
    def __str__(self):
        return self.name
    
    
class ComputerScientists(models.Model):
    name = models.CharField(max_length=1000)
    birthyear = models.CharField(max_length=4)
    class Meta:
        managed = False 
        db_table = 'computerscientists'

    def __str__(self):
        return self.name
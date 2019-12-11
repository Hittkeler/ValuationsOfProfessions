from django.db import models

# Create your models here.
class RolProfesional(models.Model):
    name_profesion= models.CharField(max_length= 60)

    def __str__(self):
        return self.name_profesion

class Assesesment(models.Model):
    Assest= models.CharField(max_length=1)

class Person(models.Model):
    name_person= models.CharField(max_length=50)
    description_service= models.CharField(max_length= 60)
    rol_profesionals= models.ManyToManyField(RolProfesional, blank= True)

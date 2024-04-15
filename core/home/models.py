from django.db import models

# Create your models here.
#every class is a table
#id field is something django automatically adds without even mentioning like primary key
#every row in the table is considered as an object

class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True , blank=True)
    address = models.TextField(null=True , blank=True)
    #image = models.ImageField()
    #file = models.FileField()
    

class Car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.name
    
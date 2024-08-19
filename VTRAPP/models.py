from django.db import models

# Create your models here.
#creating database and attributes.

class Register (models.Model):
    
    First_Name = models.CharField(max_length= 50)
    Last_Name = models.CharField(max_length= 50)
    Mother_Name = models.CharField(max_length= 50)
    Father_Name = models.CharField(max_length= 50)
    Address = models.CharField(max_length= 100)
    DOB = models.IntegerField()
    States = models.CharField(max_length= 50)
    Pin = models.IntegerField()
    Course = models.CharField(max_length= 50)
    Email = models.EmailField()
    
#python manage.py migrate  
#python manage.py makemigrations   it is going to create one pythone file 0001_initial.cpythan under migrations
#python manage.py migrate
#python manage.py createsuperuser

class Signup (models.Model):

    name = models.CharField(max_length= 50)
    Mail = models.EmailField()
    Password = models.CharField(max_length= 50)
    Confirm_Password = models.CharField(max_length= 50)

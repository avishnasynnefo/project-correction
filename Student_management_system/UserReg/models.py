from django.db import models

# Create your models here.


class department(models.Model):
    dep_name = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.dep_name

class Tables (models.Model):
     Fname =models.CharField(max_length=50)
     Lname =models.CharField(max_length=50)
     Dob = models.DateField()
     email= models.EmailField()
     phn = models.IntegerField()
     dept = models.CharField(max_length=20,default="")
   


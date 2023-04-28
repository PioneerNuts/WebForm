from django.db import models
from django.utils import timezone

class Metal_detection(models.Model):

    Work = (
        ('1', 'Yes'),
        ('2', 'No')
    )
    MaterialType = (
        ('F', 'Ferrous'),
        ('N', 'Non-Ferrous'),
        ('S', 'Stainless-Steel')
    )
    
    Emp = models.CharField(max_length=50)
    InsNo = models.CharField(max_length=50)
    Loc= models.CharField(max_length=50)
    Working = models.CharField(max_length=5, choices=Work)
    Type = models.CharField(max_length=20, choices=MaterialType)
    Time = models.DateTimeField(default=timezone.now)
    Comments = models.CharField(max_length=200)
   
class Hazard_material(models.Model):
    HazarType=(
        
        ('B','Biological'),
        ('c','chemical'),
        ('p','pysical'),
    )
    sh_wallnut =models.CharField(max_length=50, choices=HazarType, default="B")
    Desc= models.CharField(max_length=50, default="1")

    rc_shwallnut=models.CharField(max_length=50, choices=HazarType, default="B")
    Desc1= models.CharField(max_length=50, default="1")

    sorting =models.CharField(max_length=50, choices=HazarType, default="B")
    Desc2= models.CharField(max_length=50, default="1")

    shelling =models.CharField(max_length=50, choices=HazarType, default="B")
    Desc3= models.CharField(max_length=50, default="1")

    Time = models.DateTimeField(default=timezone.now)

    sizer =models.CharField(max_length=50, choices=HazarType, default="B")
    Desc4= models.CharField(max_length=50, default="1")

class UserNew(models.Model):
    First_Name = models.CharField(max_length=25, default="1")
    Last_Name = models.CharField(max_length=25, default="1")
    emailAdd = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    EmpId = models.CharField(max_length=8)
    Password = models.CharField(max_length=25)

#new class for check in form
class Emp_wellness(models.Model):
    Yn= (
        ('1', 'Yes'),
        ('2', 'No')
        )

    ill =models.CharField(max_length=50, choices=Yn, default="1")
    garments=models.CharField(max_length=50,choices=Yn,default='1')
    wash=models.CharField(max_length=50,choices=Yn,default='1')
    jwelry=models.CharField(max_length=50,choices=Yn,default='1')
    hair=models.CharField(max_length=50,choices=Yn,default='1')
    food=models.CharField(max_length=50,choices=Yn,default='1')
    food_package=models.CharField(max_length=50,choices=Yn,default='1')
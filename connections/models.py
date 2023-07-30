from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    issue = models.TextField()

    def __str__(self):
        return self.name
    
class Load(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Circle (models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Division (models.Model):
    circle = models.ForeignKey(Circle,on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class SubDivision (models.Model):
    division = models.ForeignKey(Division,on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Consumer(models.Model):
    name = models.CharField(max_length=30,null=True, blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    House_Number = models.CharField(max_length=100,null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    Village_Town = models.CharField(max_length=100,null=True, blank=True)
    Post_Office = models.CharField(max_length=100,null=True, blank=True)
    Police_Station = models.CharField(max_length=100,null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    Applied_Category = models.ForeignKey(Load,on_delete=models.CASCADE,null=True, blank=True)
    Applied_Load = models.FloatField(null=True, blank=True,validators=[MinValueValidator(0.1),MaxValueValidator(25.0)])
    circle = models.ForeignKey(Circle,on_delete=models.CASCADE,null=True, blank=True)
    division= models.ForeignKey(Division,on_delete=models.CASCADE,null=True, blank=True)
    subdivision = models.ForeignKey(SubDivision,on_delete=models.CASCADE,null=True, blank=True)
    Passport_Photo = models.ImageField(null=True, blank=True,upload_to='images/')
    Identity_Proof = models.FileField(null=True, blank=True,upload_to='pdfs/')
    Address_Proof = models.FileField(null=True, blank=True,upload_to='pdfs/')
    Occupency_Certificate = models.FileField(null=True, blank=True,upload_to='pdfs/')
    Test_Report = models.FileField(null=True, blank=True,upload_to='pdfs/')
    Agreement_Form = models.FileField(null=True, blank=True,upload_to='pdfs/')

    def __str__(self):
        return self.name
    
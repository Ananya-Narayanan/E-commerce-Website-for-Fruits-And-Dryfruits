from django.db import models

# Create your models here.

class contactdb(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Email=models.CharField(max_length=20,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=20, null=True, blank=True)
    Message = models.CharField(max_length=20, null=True, blank=True)


class registerdb(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Username = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)

class cartdb(models.Model):
    productname=models.CharField(max_length=20,null=True,blank=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)

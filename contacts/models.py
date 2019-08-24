from django.db import models


# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=200)
    gst_no = models.CharField(max_length=50)
    primary_phone = models.CharField(max_length=200)
    secondary_phone = models.CharField(max_length=200)
    primary_email = models.CharField(max_length=255)
    secondary_email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200,default=None)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    company = models.ForeignKey(Organization,on_delete=models.CASCADE)
    def __str__(self):
        return self.fname+" "+self.lname
    
    def name(self):
        return self.fname+" "+self.lname

    def organization(self):
        return self.company


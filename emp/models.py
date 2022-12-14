from email.policy import default
from random import choices

from django.db import models
from account.models import Account

# Create your models here.

class EMPs(models.Model):

    genders= (
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    )

    id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length= 15)
    f_name= models.CharField(max_length= 15)
    gender= models.CharField(max_length= 6, choices= genders, default= 'male')
    date= models.DateField(default= '2001-01-01') # yyyy-mm-dd
    numberPhone= models.IntegerField()
    address= models.CharField(max_length= 30)
    salary= models.FloatField(default= 0)
    # id_account= models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,blank=True)
    email= models.EmailField(max_length= 50, unique= True)
    status= models.BooleanField(default= True)

    def __str__(self):
        return str(self.id)

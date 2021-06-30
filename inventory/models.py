from django.db import models

# Create your models here.

class clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    phn = models.CharField(max_length=11, unique=True)
    adress = models.CharField(max_length=200)
    due = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    
    class Meta:
        db_table = "clients"
    
    def __str__(self):
        return self.name
        

class suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    phn = models.CharField(max_length=11, unique=True)
    adress = models.CharField(max_length=200)
    due = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    
    class Meta:
        db_table = "suppliers"
    
    def __str__(self):
        return self.name
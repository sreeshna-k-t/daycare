from django.db import models

# Create your models here.

class ParentRegister(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    password = models.CharField(max_length=30)

    class Meta():
        db_table="parent_reg"


class ChildRegister(models.Model):
    parent_fk = models.ForeignKey(ParentRegister, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dateofbirth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_information = models.TextField()
    dieatry_preferences = models.TextField()
    pickup_list = models.TextField()
    parental_preferences = models.TextField()
    

    class Meta():
        db_table="child_reg"
        
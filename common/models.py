from django.db import models

# Create your models here.

class ParentRegister(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta():
        db_table="parent_reg"
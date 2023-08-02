from django.db import models

from common.models import *

# Create your models here.


class Nutritions(models.Model):
    child_fk = models.ForeignKey(ChildRegister,on_delete=models.CASCADE)
    fruits = models.JSONField(blank=True, default=list)
    dairy = models.JSONField(blank=True, default=list)
    proteins = models.JSONField(blank=True, default=list)
    cereals = models.JSONField(blank=True, default=list)
    notes = models.TextField()


    class Meta():
        db_table = "nutritions"


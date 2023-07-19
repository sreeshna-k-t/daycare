from django.db import models
from common.models import ParentRegister

# Create your models here.
class ParentFeedback(models.Model):
    parent_fk = models.ForeignKey(ParentRegister,on_delete=models.CASCADE)
    feed_description= models.TextField()
    feed_date = models.DateField()
    
    class Meta():
        db_table="parent_feedback"

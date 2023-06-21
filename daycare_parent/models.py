from django.db import models
from common.models import ParentRegister

# Create your models here.
class ParentFeedback(models.Model):
    parent_fk = models.ForeignKey(ParentRegister,on_delete=models.CASCADE)
    feed_name = models.CharField(max_length=20)
    feed_no = models.CharField(max_length=30)
    feed_email = models.CharField(max_length=30)
    feed_feedback= models.TextField()
    feed_date = models.EmailField()
    

    class Meta():
        db_table="parent_feedback"

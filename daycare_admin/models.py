from django.db import models 
from common.models import *
# Create your models here.

class IncidentReport(models.Model):
    parent_fk = models.ForeignKey(ParentRegister, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=30)
    parent_email_id = models.CharField(max_length=30)
    description = models.TextField()
    current_status = models.TextField()
    incident_date = models.CharField(max_length=20)
    

    class Meta():
        db_table="incident_report"  

class StaffRegistration(models.Model):
    staff_name = models.CharField(max_length=30)
    staff_address = models.TextField()
    staff_email_id = models.CharField(max_length=30)
    staff_dob = models.CharField(max_length=30)
    staff_gender = models.CharField(max_length=20)
    staff_qualification = models.CharField(max_length=30)
    staff_mobile_no = models.CharField(max_length=30)
    staff_username = models.CharField(max_length=30)
    staff_password = models.CharField(max_length=30)

    class Meta():
        db_table = "staff_registration"




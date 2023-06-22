from django.db import models 

# Create your models here.

class IncidentReport(models.Model):
    child_name = models.CharField(max_length=20)
    parent_email_id = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    current_status = models.CharField(max_length=30)
    reported_by = models.CharField(max_length=20)
    incident_date = models.CharField(max_length=20)
    

    class Meta():
        db_table="incident_report"

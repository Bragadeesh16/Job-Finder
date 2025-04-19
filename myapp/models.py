from django.db import models
from account.models import Organization,CustomUser,CitiesModel


LOCATION_TYPE = (
    ("Work from home", "Work from home"),
    ("Hybrid", "Hybrid"),
    ("Onsite", "Onsite"),
)
EXPERIENCE = (
    ("Fresher", "Fresher"),
    ("0-1 Year", "0-1 Year"),
    ("1-2 Year", "1-2 Year"),
    ("2-3 Year", "2-3 Year"),
    ("3-4 Year", "3-4 Year"),
    ("4-5 Year", "4-5 Year"),
    ("5+ Year", "5+ Year"),
)
JOB_TYPE = (
    ('internship', 'Internship'),
    ('job', 'Job'),
)
EMPLOYMENT_TYPE = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
    ]


class Jobpost(models.Model):
    organization_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="jobposts"
    )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="jobposts")
    
    job_type = models.CharField(
        max_length=10,
        choices=JOB_TYPE,
        default='job',
    )
    
    employment_type = models.CharField(
        max_length=10,
        choices=EMPLOYMENT_TYPE,
        default='full_time',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience_required = models.CharField(max_length=255,choices=EXPERIENCE)
    location = models.ForeignKey(CitiesModel, on_delete=models.CASCADE, related_name="jobposts" ,
                                null=True,blank=True)
    location_type = models.CharField(max_length=200,choices=LOCATION_TYPE)
    skills_required = models.TextField()
    applied_users = models.ManyToManyField(
        CustomUser, related_name="applied_jobs", blank=True
    )

    def __str__(self):
        return self.title
    def save(self):
        
        super().save()



class Notification_model(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notification_sender")
    reveiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notification_reveiver")
    message = models.TextField()
    file = models.FileField(upload_to='files/', null=True, blank=True)
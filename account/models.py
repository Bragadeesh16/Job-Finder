from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    is_organization = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username or self.email
    

class Organization(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="organization_logos/", blank=True, null=True)
    country = models.ForeignKey('CountiesModel', on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey('CitiesModel', on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    country = models.ForeignKey('CountiesModel', on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey('CitiesModel', on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    skills = models.ForeignKey('skills', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"


class CountiesModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CitiesModel(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class skills(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
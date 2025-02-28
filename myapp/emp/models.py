from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length = 10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length = 10) 

    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    name = models.CharField(max_length = 200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to = "testimonials/")
    rating = models.IntegerField()

    def __str__(self):
        return self.testimonial
    
    


# Django default user model using AbstractUser
class CustomUser(AbstractUser):
    profile_picture =models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    date_of_birth = models.DateField(blank = True, null = True)

     # Resolve related_name conflicts
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)



    def __str__(self):
        return self.username


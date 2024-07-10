from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class BarangayUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    middle_name = models.CharField(max_length=50)
    profile_pic = models.FileField(
        upload_to='profile-pics/', default='profile-pics/tamago.png')
    barangay_position = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    office_hours_weekdays = models.DateTimeField(null=True)
    office_hours_weekends = models.DateTimeField(null=True)
    responsibilities = models.CharField(max_length=200)
    about = models.CharField(max_length=100)

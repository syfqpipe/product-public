from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

class CustomUser(AbstractUser):
    # Account information
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    nationality = models.CharField(max_length=30, blank=True, null=True)
    identification_type = models.CharField(max_length=20, blank=True, null=True)
    nric_number = models.CharField(max_length=12, null=True, blank=True)

    gender = models.CharField(max_length=20, blank=True)
    race = models.CharField(max_length=20, blank=True)

    USER_TYPE = [
        ('AD', 'Admin'),
        ('EG', 'eGovernment'),
        ('PB', 'Public'),

        ('NA', 'Not Available'),        
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=2, default='PB')

    # Contact information
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    home_number = models.CharField(max_length=20, blank=True, null=True)
    office_number = models.CharField(max_length=20, blank=True, null=True)
    fax_number = models.CharField(max_length=20, blank=True, null=True)

    address_1 = models.CharField(max_length=20, blank=True, default='NA')
    address_2 = models.CharField(max_length=20, blank=True, default='NA')
    address_3 = models.CharField(max_length=20, blank=True, default='NA')
    city = models.CharField(max_length=20, blank=True, default='NA')
    postcode = models.CharField(max_length=20, blank=True, default='NA')
    state = models.CharField(max_length=20, blank=True, default='NA')
    country = models.CharField(max_length=20, blank=True, default='NA')

    # Business information
    registration_number = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    company_number = models.CharField(max_length=20, blank=True, null=True)
    company_email = models.CharField(max_length=20, blank=True, null=True)
    company_address_1 = models.CharField(max_length=20, blank=True, null=True)
    company_address_2 = models.CharField(max_length=20, blank=True, null=True)
    company_address_3 = models.CharField(max_length=20, blank=True, null=True)
    company_city = models.CharField(max_length=20, blank=True, null=True)
    company_postcode = models.CharField(max_length=20, blank=True, null=True)
    company_state = models.CharField(max_length=20, blank=True, null=True)
    company_country = models.CharField(max_length=20, blank=True, null=True)

    # eGOV 
    egov_package = models.IntegerField(default=0, null=False)
    egov_quota = models.IntegerField(default=0, null=True)
    egov_expired_date = models.DateTimeField(null=True, blank=True)
    position_or_grade = models.CharField(max_length=30, blank=True, null=True)

    head_of_department_name = models.CharField(max_length=50, blank=True, null=True)
    head_of_department_position = models.CharField(max_length=50, blank=True, null=True)
    head_of_department_email = models.EmailField(max_length=50, blank=True, null=True)

    ministry_name = models.CharField(max_length=50, blank=True, null=True)
    department_name = models.CharField(max_length=50, blank=True, null=True)
    division_name = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


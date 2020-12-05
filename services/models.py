# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from users.models import (
    CustomUser
)

from entities.models import (
    Entity
)


class Service(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')

    SERVICE_TYPE = [
        ('CB', 'CBID'),
        ('IN', 'Investigation'),
        ('NA', 'Not Available')
    ]
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=2, default='NA')    

    ENTITIES_TYPE = [
        ('RB', 'Registration of Business'),
        ('RC', 'Registration of Company'),
        ('NA', 'Not Available')
    ]
    entities_type = models.CharField(choices=ENTITIES_TYPE, max_length=2, default='NA')   
    fee = models.IntegerField(default=1000)

    PRODUCT_TYPE = [
        ('ST', 'Statistics'),
        ('LS', 'Listing'),
        ('NA', 'Not Available')
    ]
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=2, default='NA')           

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.full_name

class ServiceRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)        
    reference_id = models.CharField(max_length=100, default=True)
    receipt_number = models.CharField(max_length=100, default=True)

    name = models.CharField(max_length=512, null=True)
    organisation = models.CharField(max_length=512, null=True) 
    address = models.CharField(max_length=512, null=True) 
    email_address = models.CharField(max_length=512, null=True) 
    phone_number = models.CharField(max_length=512, null=True)
    
    pending = models.BooleanField(default=True)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    in_progress_date = models.DateTimeField(null=True)
    completed_date = models.DateTimeField(null=True)

    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    remarks = models.TextField(null=True)

    pic = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='service_pic')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['created_date']

    def __str__(self):
        return self.receipt_number


class DocumentRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)        
    reference_no = models.CharField(max_length=100, null=True, blank=True)
    reference_letter_no = models.CharField(max_length=100, null=True)
    ip_no = models.CharField(max_length=100, null=True)
    court_case_no = models.CharField(max_length=100, null=True)

    official_letter_request = models.FileField(null=True, upload_to=PathAndRename('document-request-official-letter-request'))
    official_letter_egov = models.FileField(null=True, upload_to=PathAndRename('document-request-official-letter-egov'))
    
    offence = models.TextField(null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']      

class DocumentRequestItem(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)        
    reference_no = models.CharField(max_length=100, null=True, blank=True)

    DOCUMENT_STATUS = [
        ('PD', 'Pending'),
        ('AP', 'Approve')
    ]
    document_status = models.CharField(max_length=2, choices=DOCUMENT_STATUS, default='PD')
    
    DOCUMENT_TYPE = [
        ('FR', 'Form'),
        ('PF', 'Profile')
    ]
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE, default='FR')
    document_request = models.ForeignKey(DocumentRequest, on_delete=models.CASCADE, null=True, related_name='document_request_item')

    document_name = models.CharField(max_length=100, blank=True, null=True)
    image_form_type = models.CharField(max_length=100, blank=True, null=True)
    image_version_id = models.CharField(max_length=100, blank=True, null=True)

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    generated_profile = models.FileField(null=True, upload_to=PathAndRename('document-request-item-profile'))

    approver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='document_request_approver')
    approved_date = models.DateTimeField(null=True)    

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']    


class EgovernmentMinistry(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)        
    name = models.CharField(max_length=100, blank=True, null=True)   
    active = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['created_date']    

    def __str__(self):
        return self.name


class EgovernmentDepartment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)        
    name = models.CharField(max_length=150, blank=True, null=True) 
    ministry = models.ForeignKey(EgovernmentMinistry, on_delete=models.CASCADE, null=True)  
    active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['created_date']    

    def __str__(self):
        return self.name


class EgovernmentRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    approver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='egov_request_approver')
    reference_no = models.CharField(max_length=100, null=True, blank=True)

    REQUEST_TYPE = [
        ('RG', 'Registration'),
        ('QU', 'Quota Request'),
        ('RN', 'Renew Account'),
        ('UI', 'Update Information')
    ]
    request_type = models.CharField(choices=REQUEST_TYPE, max_length=2, default='RG')

    REQUEST_STATUS = [
        ('NA', 'NA'),
        ('AP', 'Approved'),
        ('PD', 'Pending'),
        ('RJ', 'Rejected')
    ]
    request_status = models.CharField(choices=REQUEST_STATUS, max_length=2, default='PD')

    egov_package = models.IntegerField(default=0, null=False)
    egov_quota = models.IntegerField(default=0, null=True)
    
    position_or_grade = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)

    head_of_department_name = models.CharField(max_length=100, blank=True, null=True)
    head_of_department_position = models.CharField(max_length=100, blank=True, null=True)
    head_of_department_email = models.EmailField(max_length=100, blank=True, null=True)

    ministry_name = models.CharField(max_length=100, blank=True, null=True)
    department_name = models.CharField(max_length=100, blank=True, null=True)   
    division_name = models.CharField(max_length=100, blank=True, null=True)

    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    address_3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    attachment_letter = models.FileField(null=True, upload_to=PathAndRename('egovernment-request-attachment-letter'))
    expired_date = models.DateTimeField(null=True, blank=True)

    remarks = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['created_date']    


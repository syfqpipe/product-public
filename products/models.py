from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=100, default='NA')
    description = models.TextField(default='NA')
    slug = models.CharField(max_length=100, default='NA')

    active = models.BooleanField(default=True)
    ctc = models.BooleanField(default=True)
    roc = models.BooleanField(default=True)

    fee = models.IntegerField(default=0)

    tax = models.IntegerField(default=0)
    tax_start_date = models.DateTimeField(null=True)
    tax_end_date = models.DateTimeField(null=True)

    discount = models.IntegerField(default=0)
    discount_start_date = models.DateTimeField(null=True)
    discount_end_date = models.DateTimeField(null=True)

    coa_code = models.CharField(max_length=100, null=True, blank=True)
    coa_description = models.CharField(max_length=100, null=True, blank=True)

    webservice = models.CharField(max_length=100, null=True, blank=True)
    channel = models.CharField(max_length=100, null=True, blank=True)
    
    OUTPUT_TYPE = [
        ('DO', 'Document'),
        ('IM', 'Image'),
        ('LI', 'List'),
    ]
    output_type = models.CharField(
        choices=OUTPUT_TYPE,
        max_length=2,
        default='CP'
    )

    LANGUAGE= [
        ('EN', 'English'),
        ('MS', 'Malay'),

        ('NA', 'Not Available'),
    ]
    language = models.CharField(
        choices=LANGUAGE,
        max_length=2,
        default='EN'
    )    

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class ProductSearchCriteria(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    incorp_date_from = models.CharField(max_length=100) 
    incorp_date_to = models.CharField(max_length=100) 
    company_status = models.CharField(max_length=100, default='NA') 
    company_type = models.CharField(max_length=100, default='NA') 
    company_origin = models.CharField(max_length=100, default='NA') 
    company_location = models.CharField(max_length=100, default='NA') 
    division = models.CharField(max_length=100, default='NA') 
    business_code = models.CharField(max_length=100, default='NA')
    total_page = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    class meta:
        ordering = ['id']
    
    def __str__(self):
        return self.id    
    
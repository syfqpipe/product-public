from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename
from entities.models import Entity
from users.models import CustomUser

class Quota(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    QOUTA_TYPE = [
        ('0A', 'Custom Listing A'),
        ('0B', 'Custom Listing B'),
        ('0C', 'Custom Listing C'),
        ('0D', 'Custom Listing D'),

        ('E1', 'EGov Package 1'),
        ('E2', 'EGov Package 2'),
        ('E3', 'EGov Package 3'),
        ('E4', 'EGov Package 4'),

        ('DS', 'Document Search'),
    ]
    quota_type  = models.CharField(
        choices=QOUTA_TYPE ,
        max_length=2,
        default='NA'
    )    
    
    quota = models.IntegerField(default=0)
    # entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']


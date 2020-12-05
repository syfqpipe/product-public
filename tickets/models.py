# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from products.models import (
    Product
)

from users.models import (
    CustomUser
)

class TicketTopic(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_en = models.CharField(max_length=100, default='NA')
    name_bm = models.CharField(max_length=100, default='NA')
    active = models.BooleanField(default=True)

    CATEGORY = [
        ('GN', 'General'),
        ('EG', 'eGovernment')
    ]
    category = models.CharField(
        choices=CATEGORY,
        max_length=2,
        default='GN'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.name_en


class TicketSubject(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_en = models.CharField(max_length=100, default='NA')
    name_bm = models.CharField(max_length=100, default='NA')
    active = models.BooleanField(default=True)

    topic = models.ForeignKey(TicketTopic, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.name_en


class Ticket(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, default='NA')
    ticket_no = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='NA')

    TICKET_TYPE = [
        ('GN', 'General'),
        ('EG', 'eGovernment')
    ]
    ticket_type = models.CharField(
        choices=TICKET_TYPE,
        max_length=2,
        default='GN'
    )
    
    TICKET_STATUS = [
        ('RS', 'Resolved'),
        ('US', 'Unresolved'),
        ('AS', 'Assigned'),
        ('IP', 'In Progress'),
        ('IQ', 'In Progress - Response Required'),
        ('IC', 'In Progress - Response Received'),
        ('EC', 'Escalation'),
        ('CA', 'Closed - Assigned'),
        ('CR', 'Closed - Not Related'),
        ('CD', 'Closed - Not Responded'),
        ('CO', 'Closed - Resolved'),
        ('CL', 'Closed')
    ]
    ticket_status = models.CharField(
        choices=TICKET_STATUS,
        max_length=2,
        default='IP'
    )
    
    topic = models.ForeignKey(TicketTopic, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(TicketSubject, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # name = models.CharField(max_length=100, null=True, blank=True)
    # email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    receipt_number = models.CharField(max_length=100, null=True, blank=True)
    # attached_document = models.FileField(null=True, upload_to=PathAndRename('enquiry-attached-document'))

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-ticket_no']
    
    def __str__(self):
        return self.ticket_no


class TicketCBID(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requestor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    remarks = models.TextField(default='NA')
    
    ENTITY_TYPE = [
        ('ROB', 'Registration of Business'),
        ('ROC', 'Registration of Company')
    ]
    entity_type = models.CharField(choices=ENTITY_TYPE, max_length=3, default='ROB')

    PRODUCT_TYPE = [
        ('BT', 'Both'),
        ('LT', 'Listing'),
        ('PD', 'Product')
    ]
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=2, default='BT')

    STATUS_TYPE = [
        ('PG', 'Pending'),
        ('PD', 'Paid'),
        ('CP', 'Completed')
    ]
    status = models.CharField(choices=STATUS_TYPE, max_length=2, default='PG')
    
    pending_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['requestor']
    
    def __str__(self):
        return self.entity_type


class TicketInvestigation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    officer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reference_letter_number = models.CharField(max_length=100, default='NA')
    ip_no = models.CharField(max_length=100, default='NA')
    court_case_number = models.CharField(max_length=100, default='NA')
    official_attachment = models.FileField(null=True, upload_to=PathAndRename('investigation-attachment-official'))
    offense = models.CharField(max_length=100, default='NA')
    document_request = models.FileField(null=True, upload_to=PathAndRename('investigation-document-request'))
    submit_request = models.FileField(null=True, upload_to=PathAndRename('investigation-submit-request'))

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['requestor']
    
    def __str__(self):
        return self.entity_type


class EnquiryTicket(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')

    #topic_id
    #subject_id

    TICKET_TYPE = [
        
        
        ('NA', 'Not Available')
    ]
    ticket_type = models.CharField(choices=TICKET_TYPE, max_length=2, default='NA')

    TICKET_STATUS = [
        
        
        ('NA', 'Not Available')
    ]
    ticket_status = models.CharField(choices=TICKET_STATUS, max_length=2, default='PG')    


    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name



class EnquiryTicketReply(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='ticket_replies') 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    escalation_email = models.CharField(max_length=100, null=True, blank=True)
    
    REPLY_TYPE = [
        ('IP', 'In Progress'),
        ('IQ', 'In Progress - Response Required'),
        ('IC', 'In Progress - Response Received'),
        ('AS', 'Assigned'),
        ('EC', 'Escalation'),
        ('CA', 'Closed - Assigned'),
        ('CR', 'Closed - Not Related'),
        ('CD', 'Closed - Not Responded'),
        ('CO', 'Closed - Resolved'),
        ('CL', 'Closed')
    ] 
    reply_type = models.CharField(
        choices=REPLY_TYPE,
        max_length=2,
        default='IP'
    )

    message = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.ticket


class EnquiryTicketSelection(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')
    category = models.CharField(max_length=100, default='NA')
    selection_type = models.CharField(max_length=100, default='NA')

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class EnquiryNote(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    
    LANGUAGE = [
        ('EN', 'ENGLISH'),
        ('BM', 'BAHASA MELAYU')
    ]
    language = models.CharField(
        choices=LANGUAGE,
        max_length=2,
        default='EN'
    )
    description = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class EnquiryMedia(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='ticket_attachments') 
    attached_document = models.FileField(null=True, upload_to=PathAndRename('enquiry-attached-document'))
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from carts.models import (
    Cart
)

from users.models import (
    CustomUser
)

class Transaction(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    total_amount = models.IntegerField(null=True)

    PAYMENT_STATUS = [
        ('OK', 'Successful'),
        ('FL', 'Failed'),
        ('PD', 'Pending'),

        ('NA', 'Not Available')
    ]

    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    transaction_message = models.CharField(max_length=255, blank=True, null=True)
    card_holder = models.CharField(max_length=255, blank=True, null=True)
    card_no_mask = models.CharField(max_length=255, blank=True, null=True)
    
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=2, default='PD')    
    payment_gateway_update_date = models.DateTimeField(null=True) 

    PAYMENT_METHOD = [
        ('CC', 'Credit Card'),
        ('DD', 'Direct Debit'),
        ('WA', 'e-Wallet'),
        ('NA', 'Not Available')
    ]
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=2, null=True)

    name = models.CharField(max_length=512, null=True)
    organisation = models.CharField(max_length=512, null=True) 
    address1 = models.CharField(max_length=512, null=True) 
    address2 = models.CharField(max_length=512, null=True) 
    address3 = models.CharField(max_length=512, null=True) 
    postcode = models.CharField(max_length=512, null=True) 
    state = models.CharField(max_length=512, null=True) 
    city = models.CharField(max_length=512, null=True) 
    country = models.CharField(max_length=512, null=True) 
    email_address = models.CharField(max_length=512, null=True) 
    phone_number = models.CharField(max_length=512, null=True) 

    reference =  models.CharField(max_length=512, null=True)     

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    payment_gateway_order_id = models.IntegerField(default=0)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    reference_no = models.CharField(max_length=512, null=True)
    transaction_id = models.CharField(max_length=512, null=True)
    receipt_no = models.CharField(max_length=512, null=True)
    receipt = models.FileField(null=True, upload_to=PathAndRename('transaction-receipt'))

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['-payment_gateway_update_date']


class TransactionPayment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class RefundDropdown(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

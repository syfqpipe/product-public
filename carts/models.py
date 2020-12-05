# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from entities.models import (
    Entity
)

from products.models import (
    Product, ProductSearchCriteria
)

from quotas.models import (
    Quota
)

from services.models import (
    ServiceRequest
)

from users.models import (
    CustomUser
)

class Cart(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    active = models.BooleanField(default=True)
    total_price_before_tax = models.IntegerField(default=0)
    total_tax = models.IntegerField(default=0)
    total_tax_after_tax = models.IntegerField(default=0)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    CART_STATUS = [
        ('CM', 'Completed'),
        ('AB', 'Abandoned'),
        ('CR', 'Created'),

        ('NA', 'Not Available')
    ]
    cart_status = models.CharField(choices=CART_STATUS, max_length=2, default='CR')    

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
    


class CartItem(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    active = models.BooleanField(default=True)

    order_no = models.CharField(max_length=100, null=True)
    
    CART_ITEM_TYPE = [
        ('PS', 'Product Search Criteria'),
        ('PR', 'Product'),
        ('SE', 'Service'),
        ('QU', 'Quota'),

        ('NA', 'Not Available')
    ]
    cart_item_type = models.CharField(choices=CART_ITEM_TYPE, max_length=2, default='NA')

    cart = models.ForeignKey(Cart, related_name='cart_item', on_delete=models.CASCADE, null=True)

    # PRODUCT
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    year1 = models.CharField(null=True, max_length=100)
    year2 = models.CharField(null=True, max_length=100)
    
    # PRODUCT IMAGE
    image_form_type = models.CharField(max_length=100, null=True)
    image_version_id = models.CharField(max_length=100, null=True)

    # SERVICE
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, null=True)

    # QUOTA
    quota = models.ForeignKey(Quota, on_delete=models.CASCADE, null=True)

    # PRODUCT SEARCH CRITERIA
    product_search_criteria = models.ForeignKey(ProductSearchCriteria, on_delete=models.CASCADE, null=True)

    # DOCUMENT
    output_document = models.FileField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

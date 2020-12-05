from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    Product,
    ProductSearchCriteria,
)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductSearchCriteriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSearchCriteria
        fields = '__all__'

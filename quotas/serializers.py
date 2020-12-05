from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    Quota
)

from users.serializers import (
    CustomUserSerializer
)

class QuotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quota
        fields = '__all__'


class QuotaExtendedSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Quota
        fields = '__all__'

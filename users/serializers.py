from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now
#from api.settings import AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME

from .models import (
    CustomUser
)

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'title', 
            'full_name', 
            'birth_date', 
            'nationality', 
            'identification_type',
            'nric_number',
            'gender',
            'race',
            'user_type',
            'email',
            'phone_number',
            'home_number',
            'office_number',
            'fax_number',
            'address_1',
            'address_2',
            'address_3',
            'city',
            'postcode',
            'state',
            'country',
            'registration_number',
            'company_name',
            'company_number',
            'company_email',
            'company_address_1',
            'company_address_2',
            'company_address_3',
            'company_city',
            'company_postcode',
            'company_state',
            'company_country',
            'egov_package',
            'egov_quota',
            'position_or_grade',
            'head_of_department_name',
            'head_of_department_position',
            'head_of_department_email',
            'ministry_name',
            'division_name',
            'department_name',
            'username',
            'is_active'
        )
        read_only_fields = ('email', 'id')


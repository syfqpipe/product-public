from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from drf_extra_fields.fields import Base64FileField

from .models import (
    Service,
    ServiceRequest,
    DocumentRequest,
    DocumentRequestItem,
    EgovernmentRequest,
    EgovernmentMinistry,
    EgovernmentDepartment
)

from users.serializers import CustomUserSerializer

from entities.serializers import EntitySerializer

class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        return 'pdf'

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class ServiceRequestSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = ServiceRequest
        fields = '__all__'


class DocumentRequestItemSerializer(serializers.ModelSerializer):

    generated_profile = PDFBase64File()
    entity = EntitySerializer(many=False)
    approver = CustomUserSerializer(many=False)

    class Meta:
        model = DocumentRequestItem
        fields = '__all__'  


class DocumentRequestSerializer(serializers.ModelSerializer):
    official_letter_request = PDFBase64File()
    official_letter_egov = PDFBase64File()

    class Meta:
        model = DocumentRequest
        fields = '__all__'


class DocumentRequestExtendedSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(many=False)
    document_request_item = DocumentRequestItemSerializer(many=True)

    class Meta:
        model = DocumentRequest
        fields = '__all__'


class EgovernmentRequestSerializer(serializers.ModelSerializer):

    attachment_letter = PDFBase64File()
    class Meta:
        model = EgovernmentRequest
        fields = '__all__'          


class EgovernmentRequestExtendedSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(many=False)
    approver = CustomUserSerializer(many=False)
    
    class Meta:
        model = EgovernmentRequest
        fields = '__all__'          


class EgovernmentMinistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = EgovernmentMinistry
        fields = '__all__'          



class EgovernmentDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = EgovernmentDepartment
        fields = '__all__'          


class EgovernmentDepartmentExtendedSerializer(serializers.ModelSerializer):

    ministry = EgovernmentMinistrySerializer(many=False)

    class Meta:
        model = EgovernmentDepartment
        fields = '__all__'          


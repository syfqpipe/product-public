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
    TicketTopic,
    TicketSubject,
    Ticket,
    TicketCBID,
    TicketInvestigation,
    EnquiryTicket,
    EnquiryTicketReply,
    EnquiryTicketSelection,
    EnquiryNote,
    EnquiryMedia
)

from users.serializers import (
    CustomUserSerializer
)

class DocumentBase64File(Base64FileField):
    ALLOWED_TYPES = [
        'pdf',
        'doc',
        'docx',
        'jpg',
        'jpeg',
        'png'
    ]

    def get_file_extension(self, filename, decoded_file):
        return 'pdf'

class TicketTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketTopic
        fields = '__all__'


class TicketSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketSubject
        fields = '__all__'


class TicketSubjectExtendedSerializer(serializers.ModelSerializer):
    topic = TicketTopicSerializer(read_only=True)

    class Meta:
        model = TicketSubject
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketCBIDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TicketCBID
        fields = '__all__'


class TicketCBIDExtendedSerializer(serializers.ModelSerializer):
    requestor = CustomUserSerializer(read_only=True)

    class Meta:
        model = TicketCBID
        fields = '__all__'


class TicketInvestigationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketInvestigation
        fields = '__all__'



class EnquiryTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnquiryTicket
        fields = '__all__'

class EnquiryTicketReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = EnquiryTicketReply
        fields = '__all__'

class EnquiryTicketReplyExtendedSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = EnquiryTicketReply
        fields = '__all__'


class EnquiryTicketSelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnquiryTicketSelection
        fields = '__all__'                


class EnquiryNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnquiryNote
        fields = '__all__'

class EnquiryMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnquiryMedia
        fields =  '__all__'


class TicketExtendedSerializer(serializers.ModelSerializer):
    topic = TicketTopicSerializer(read_only=True)
    subject = TicketSubjectSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    ticket_replies = EnquiryTicketReplyExtendedSerializer(many=True)
    ticket_attachments = EnquiryMediaSerializer(many=True)
    
    class Meta:
        model = Ticket
        fields = '__all__'
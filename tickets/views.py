from django.shortcuts import render
from django.db.models import Q
import json
import datetime
import pytz
import base64
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django_filters.rest_framework import DjangoFilterBackend

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

from .serializers import (
    TicketTopicSerializer,
    TicketSubjectSerializer,
    TicketSubjectExtendedSerializer,
    TicketSerializer,
    TicketExtendedSerializer,
    TicketCBIDSerializer,
    TicketCBIDExtendedSerializer,
    TicketInvestigationSerializer,
    EnquiryTicketSerializer,
    EnquiryTicketReplySerializer,
    EnquiryTicketSelectionSerializer  ,
    EnquiryNoteSerializer,
    EnquiryMediaSerializer
)

from users.models import CustomUser

class TicketTopicViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketTopic.objects.all()
    serializer_class = TicketTopicSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketTopic.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = TicketTopic.objects.all()
            else:
                queryset = TicketTopic.objects.filter(company=company.id)
        """
        return queryset    
 

class TicketSubjectViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketSubject.objects.all()
    serializer_class = TicketSubjectSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketSubject.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = TicketSubject.objects.all()
            else:
                queryset = TicketSubject.objects.filter(company=company.id)
        """
        return queryset


    @action(methods=['GET'], detail=False)
    def extended(self, request, *args, **kwargs):
        
        queryset = TicketSubject.objects.all()
        serializer_class = TicketSubjectExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data)
 

class TicketViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Ticket.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Ticket.objects.all()
            else:
                queryset = Ticket.objects.filter(company=company.id)
        """
        return queryset 
    
    @action(methods=['POST'], detail=False)
    def create_ticket(self, request, *args, **kwargs):
        ticket_request = json.loads(request.body)
        # print('>>>>> ', ticket_request)
        ticket_request_description = ticket_request['description']
        ticket_request_type = ticket_request['ticket_type']
        ticket_request_topic_id = ticket_request['topic']
        ticket_request_subject_id = ticket_request['subject']
        ticket_request_user_id = ticket_request['user']
        ticket_request_phone_number = ticket_request['phone_number']
        ticket_request_receipt_number = ticket_request['receipt_number']
        ticket_request_attached_documents_ = ticket_request['documents']

        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')
        
        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)
        
        filter_year = datetime.datetime.now(tz=timezone.utc).year
        filter_month = datetime.datetime.now(tz=timezone.utc).month
        filter_day = datetime.datetime.now(tz=timezone.utc).day

        running_no_ = Ticket.objects.filter(
            Q(ticket_no__isnull=False) &
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()
        running_no_ = "{0:0>5}".format(running_no_ + 1)

        ticket_request_user = CustomUser.objects.filter(id=str(ticket_request_user_id)).first()
        ticket_request_topic = TicketTopic.objects.filter(id=str(ticket_request_topic_id)).first()
        ticket_request_subject = TicketSubject.objects.filter(id=str(ticket_request_subject_id)).first()

        if ticket_request_type == 'GN':
            running_no = 'PG' + current_year + current_month + current_day + running_no_
        else:
            running_no = 'EG' + current_year + current_month + current_day + running_no_

        new_ticket = Ticket.objects.create(
            ticket_no=running_no,
            description=ticket_request_description,
            ticket_type=ticket_request_type,
            topic=ticket_request_topic,
            subject=ticket_request_subject,
            user=ticket_request_user,
            phone_number=ticket_request_phone_number,
            receipt_number=ticket_request_receipt_number
        )

        if ticket_request_attached_documents_:
            for media in ticket_request_attached_documents_:
                media_base64 = media['file'].encode('utf-8')
                format, pdfstr = media_base64.decode().split(';base64,') 
                ext = format.split('/')[-1] 
                file_name = media['name']
                media_ = ContentFile(base64.b64decode(pdfstr), name=file_name)
                new_media = EnquiryMedia.objects.create(
                    name=file_name,
                    ticket=new_ticket,
                    attached_document=media_
                )

        serializer = TicketExtendedSerializer(new_ticket)
        return Response(serializer.data)


    @action(methods=['POST'], detail=True)
    def resolve_ticket(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'RS'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)   
    
    @action(methods=['GET'], detail=False)
    def extended(self, request, *args, **kwargs):
        
        queryset = Ticket.objects.all()
        serializer_class = TicketExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data)
    
    @action(methods=['POST'], detail=True)
    def status_ip_required(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'IQ'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)   
    
    @action(methods=['POST'], detail=True)
    def status_ip_received(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'IC'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)   
    
    @action(methods=['POST'], detail=True)
    def status_escalated(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'EC'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)   
    
    @action(methods=['POST'], detail=True)
    def status_assign(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'AS'
        ticket.ticket_type = 'EG'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data) 

    @action(methods=['POST'], detail=True)
    def status_closed_assigned(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'CA'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)   
    
    @action(methods=['POST'], detail=True)
    def status_closed_not_related(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'CR'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)  

    @action(methods=['POST'], detail=True)
    def status_closed_not_responded(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'CD'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)  

    @action(methods=['POST'], detail=True)
    def status_closed_resolved(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'CO'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)     
    
    @action(methods=['POST'], detail=True)
    def status_closed(self, request, *args, **kwargs):
        ticket = self.get_object()

        ticket.ticket_status = 'CL'
        ticket.save()

        serializer = TicketExtendedSerializer(ticket)
        return Response(serializer.data)   


class TicketCBIDViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketCBID.objects.all()
    serializer_class = TicketCBIDSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketCBID.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = TicketCBID.objects.all()
            else:
                queryset = TicketCBID.objects.filter(company=company.id)
        """
        return queryset   

    @action(methods=['GET'], detail=False)
    def extended(self, request, *args, **kwargs):
        
        queryset = TicketCBID.objects.all()
        serializer_class = TicketCBIDExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data) 
 

class TicketInvestigationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketInvestigation.objects.all()
    serializer_class = TicketInvestigationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketInvestigation.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = TicketInvestigation.objects.all()
            else:
                queryset = TicketInvestigation.objects.filter(company=company.id)
        """
        return queryset    
 

class TicketInvestigationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketInvestigation.objects.all()
    serializer_class = TicketInvestigationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketInvestigation.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = TicketInvestigation.objects.all()
            else:
                queryset = TicketInvestigation.objects.filter(company=company.id)
        """
        return queryset    
 
class EnquiryTicketViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EnquiryTicket.objects.all()
    serializer_class = EnquiryTicketSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EnquiryTicket.objects.all()
        return queryset    

class EnquiryTicketReplyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EnquiryTicketReply.objects.all()
    serializer_class = EnquiryTicketReplySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EnquiryTicketReply.objects.all()
        return queryset    
    

    @action(methods=['POST'], detail=False)
    def create_reply(self, request, *args, **kwargs):
        reply_request = json.loads(request.body)
        reply_request_ticket_id = reply_request['ticket']
        reply_request_user_id = reply_request['user']
        reply_request_type = reply_request['type']
        reply_request_message = reply_request['message']
        reply_request_remarks = reply_request['remarks']

        reply_request_ticket = Ticket.objects.filter(id=str(reply_request_ticket_id)).first()
        reply_request_user = CustomUser.objects.filter(id=str(reply_request_user_id)).first()

        ticket_reply = EnquiryTicketReply.objects.create(
            ticket=reply_request_ticket,
            user=reply_request_user,
            reply_type=reply_request_type,
            message=reply_request_message,
            remarks=reply_request_remarks
        )

        serializer = EnquiryTicketReplySerializer(ticket_reply)
        return Response(serializer.data)


class EnquiryTicketSelectionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EnquiryTicketSelection.objects.all()
    serializer_class = EnquiryTicketSelectionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EnquiryTicketSelection.objects.all()
        return queryset    

class EnquiryNoteViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EnquiryNote.objects.all()
    serializer_class = EnquiryNoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EnquiryNote.objects.all()
        return queryset 
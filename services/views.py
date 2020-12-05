import hashlib
import json
import datetime
import pytz
import base64

from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.db.models import Q
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings


from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Service,
    ServiceRequest,
    DocumentRequest,
    DocumentRequestItem,
    EgovernmentRequest,
    EgovernmentMinistry,
    EgovernmentDepartment
)

from .serializers import (
    ServiceSerializer,
    ServiceRequestSerializer,
    DocumentRequestSerializer,
    DocumentRequestExtendedSerializer,
    DocumentRequestItemSerializer,
    EgovernmentRequestSerializer,
    EgovernmentRequestExtendedSerializer,
    EgovernmentMinistrySerializer,
    EgovernmentDepartmentSerializer,
    EgovernmentDepartmentExtendedSerializer
)

from entities.models import Entity
from carts.models import Cart, CartItem
from carts.serializers import CartItemSerializer, CartSerializer
from transactions.models import Transaction
from users.models import CustomUser

class ServiceViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Service.objects.all()

        return queryset    

    @action(methods=['GET'], detail=False)
    def status(self, request, *args, **kwargs):        

        status = request.GET.get('q', '')
        
        if status == 'created':

            transactions = Transaction.objects.filter(Q(payment_status='PD') | Q(payment_status='FL'))
            carts = Cart.objects.filter(cart_item_type='SE')
            cart_items = CartItem.objects.filter(cart=carts)
            services_ = Service.objects.filter(service_type='CB', completed=False)

            services = transactions | carts | cart_items | services_
            

        elif status == 'paid':
            transactions = Transaction.objects.filter(payment_status='OK')
            carts = Cart.objects.filter(cart_item_type='SE')
            cart_items = CartItem.objects.filter(cart=carts)
            services_ = Service.objects.filter(service_type='CB', completed=False)

            services = transactions | carts | cart_items | services_

        elif status == 'completed':
            services = Service.objects.filter(service_type='CB', completed=True)
        else:
            return Response('Query q is empty or wrong!')

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def request(self, request, *args, **kwargs):       

        json_body = json.loads(request.body)  

        service_id = json_body['service_id']
        service = Service.objects.get(id=str(service_id))

        name = json_body['name']
        organisation = json_body['organisation']
        address = json_body['address']
        # address1 = json_body['# address1']
        # address2 = json_body['# address2']
        # address3 = json_body['# address3']
        # postcode = json_body['# postcode']
        # country = json_body['# country']
        # city = json_body['# city']
        email_address = json_body['email']
        phone_number = json_body['phone_number']

        service_request = ServiceRequest.objects.create(
            service=service,
            name=name,
            organisation=organisation,
            address=address,
            email_address=email_address,
            phone_number=phone_number
        )

        serializer = ServiceRequestSerializer(service_request)
        return Response(serializer.data)


class ServiceRequestViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = ServiceRequest.objects.all()

        return queryset   


    @action(methods=['GET'], detail=False)
    def report(self, request, *args, **kwargs):   

        service_requests = ServiceRequest.objects.all()

        serializer = ServiceRequestSerializer()

        new_list = []

        for service_request in service_requests:
            serializer = ServiceRequestSerializer(service_request)
            data_ = serializer.data
            cart_item = CartItem.objects.filter(service_request=service_request).first()
            cart_item_serializer = CartItemSerializer(cart_item)
            data_['transaction'] = cart_item_serializer.data
            new_list.append(data_)
        
        return Response(new_list)        


    @action(methods=['POST'], detail=True)
    def mark_as_complete(self, request, *args, **kwargs):       

        json_body = json.loads(request.body)  

        service_request = self.get_object()

        service_request.completed = True
        service_request.completed_date = json_body['completed_date']
        service_request.remarks = json_body['remarks']
        service_request.save()

        serializer = ServiceRequestSerializer(service_request)
        return Response(serializer.data)


class DocumentRequestViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = DocumentRequest.objects.all()
    serializer_class = DocumentRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = DocumentRequest.objects.all()

        return queryset    

    @action(methods=['POST'], detail=False)
    def create_request(self, request, *args, **kwargs):
        request_document_request = json.loads(request.body)
        request_official_letter_request_original = request_document_request['official_letter_request']
        request_official_letter_egov_original = request_document_request['official_letter_egov']
        request_reference_letter_no = request_document_request['reference_letter_no']
        request_ip_no = request_document_request['ip_no']
        request_court_case_no = request_document_request['court_case_no']
        request_offence = request_document_request['offence']
        request_user_id = request_document_request['user']

        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')
        
        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)
        
        filter_year = datetime.datetime.now(tz=timezone.utc).year
        filter_month = datetime.datetime.now(tz=timezone.utc).month
        filter_day = datetime.datetime.now(tz=timezone.utc).day

        running_no_1_ = EgovernmentRequest.objects.filter(
            Q(reference_no__isnull=False) &
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()
        running_no_2_ = DocumentRequest.objects.filter(
            Q(reference_no__isnull=False) &
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()
        running_no_ = "{0:0>6}".format(running_no_1_ + running_no_2_ + 1)

        request_user = CustomUser.objects.filter(id=str(request_user_id)).first()

        request_official_letter_request_base64 = request_official_letter_request_original.encode('utf-8')
        format, pdfstr = request_official_letter_request_base64.decode().split(';base64,') 
        ext = format.split('/')[-1] 
        request_official_letter_request = ContentFile(base64.b64decode(pdfstr), name='temp.' + ext)

        request_official_letter_egov_base64 = request_official_letter_egov_original.encode('utf-8')
        format, pdfstr = request_official_letter_egov_base64.decode().split(';base64,') 
        ext = format.split('/')[-1] 
        request_official_letter_egov = ContentFile(base64.b64decode(pdfstr), name='temp.' + ext)

        new_document_request = DocumentRequest.objects.create(
            reference_no='EGOV' + current_year + current_month + current_day + running_no_,
            reference_letter_no=request_reference_letter_no,
            ip_no=request_ip_no,
            court_case_no=request_court_case_no,
            official_letter_request=request_official_letter_request,
            official_letter_egov=request_official_letter_egov,
            offence=request_offence,
            user=request_user
        )

        serializer = DocumentRequestExtendedSerializer(new_document_request)
        return Response(serializer.data)


    @action(methods=['GET'], detail=True)
    def with_item(self, request, *args, **kwargs):  

        document_request = self.get_object()

        serializer = DocumentRequestExtendedSerializer(document_request)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def approve_item(self, request, *args, **kwargs):

        item_request = json.loads(request.body)
        item_request_item_id = item_request['item']
        item_request_approver_id = item_request['approver']

        item_document = DocumentRequestItem.objects.filter(id=str(item_request_item_id)).first()
        approver = CustomUser.objects.filter(id=str(item_request_approver_id)).first()

        item_document.document_status = 'AP'
        item_document.approver = approver
        item_document.approved_date = datetime.datetime.now()

        item_document.save()

        serializer = DocumentRequestItemSerializer(item_document)
        return Response(serializer.data)


    @action(methods=['POST'], detail=True)
    def reject_item(self, request, *args, **kwargs):

        item_request = json.loads(request.body)
        item_request_item_id = item_request['item']
        item_request_approver_id = item_request['approver']

        item_document = DocumentRequestItem.objects.filter(id=str(item_request_item_id)).first()
        approver = CustomUser.objects.filter(id=str(item_request_approver_id)).first()

        item_document.document_status = 'RJ'
        item_document.approver = approver
        item_document.approved_date = datetime.datetime.now()

        item_document.save()

        serializer = DocumentRequestItemSerializer(item_document)
        return Response(serializer.data)


    @action(methods=['POST'], detail=True)
    def add_item_to_document_request(self, request, *args, **kwargs):    

        document_request_item_request = json.loads(request.body)
        document_type = document_request_item_request['document_type']
        
        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')
        
        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)
        
        filter_year = datetime.datetime.now(tz=timezone.utc).year
        filter_month = datetime.datetime.now(tz=timezone.utc).month
        filter_day = datetime.datetime.now(tz=timezone.utc).day

        running_no_ = DocumentRequestItem.objects.filter(
            Q(reference_no__isnull=False) &
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()

        running_no = "{0:0>6}".format(running_no_ + 1)
        print(running_no)
        
        document_request = self.get_object()
            
        if document_type == 'FR':
            request_image_version_id = document_request_item_request['image_version_id']
            request_image_form_type = document_request_item_request['image_form_type']
            request_document_name = document_request_item_request['document_name']
            request_entity_id = document_request_item_request['entity_id']
            request_entity = Entity.objects.filter(id=request_entity_id).first()
            new_document_request_item = DocumentRequestItem.objects.create(
                reference_no = 'GOV' + current_year + current_month + current_day + running_no,
                document_type=document_type,
                image_form_type=request_image_form_type,
                image_version_id=request_image_version_id,
                document_request=document_request,
                document_name=request_document_name,
                entity=request_entity
            )
        elif document_type == 'PF':
            request_document_name = document_request_item_request['document_name']
            request_entity_id = document_request_item_request['entity_id']
            request_entity = Entity.objects.filter(id=request_entity_id).first()
            new_document_request_item = DocumentRequestItem.objects.create(
                reference_no = 'GOV' + current_year + current_month + current_day + running_no,
                document_type=document_type,
                document_request=document_request,
                document_name=request_document_name,
                entity=request_entity
            )
            
        serializer = DocumentRequestExtendedSerializer(document_request)
        return Response(serializer.data)


    @action(methods=['POST'], detail=True)
    def remove_item_from_document_request(self, request, *args, **kwargs):  

        document_request_item_id = json.loads(request.body)['document_request_item_id']
        document_request_item = DocumentRequestItem.objects.filter(id=document_request_item_id).first()
        
        document_request = self.get_object()    

        document_request.document_request_item.remove(document_request_item)
        document_request.save()

        serializer = DocumentRequestExtendedSerializer(document_request)
        return Response(serializer.data)              


    @action(methods=['POST'], detail=False)
    def user_request(self, request, *args, **kwargs):

        user_request_item = json.loads(request.body)
        user_ = user_request_item['user']

        requests = DocumentRequest.objects.filter(user=user_).order_by('-created_date')

        serializer = DocumentRequestExtendedSerializer(requests, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def accept_request(self, request, *args, **kwargs):

        document_request_item_id = json.loads(request.body)['document_request_item_id']
        # document_request_item_id = json.loads(request.body)['document_request_item_id']
        document_request_item = DocumentRequestItem.objects.filter(id=document_request_item_id).first()

        document_request = self.get_object()    

        document_request.document_request_item.approved = True
        document_request.document_request_item.approved_date = datetime.now()
        document_request.save()

        serializer = DocumentRequestExtendedSerializer(document_request)
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=False)
    def all_with_item(self, request, *args, **kwargs):

        queryset = DocumentRequest.objects.all()
        serializer_class = DocumentRequestExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data)
    

class EgovernmentRequestViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EgovernmentRequest.objects.all()
    serializer_class = EgovernmentRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = [
        # 'egov_request'
    ]
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EgovernmentRequest.objects.all()

        return queryset  
    
    @action(methods=['POST'], detail=False)
    def add_request(self, request, *args, **kwargs):

        request_items = json.loads(request.body) 
        request_user_id = request_items['user']
        request_request_type = request_items['request_type']
        request_attachment_letter_original = request_items['attachment_letter']

        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')
        
        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)
        
        filter_year = datetime.datetime.now(tz=timezone.utc).year
        filter_month = datetime.datetime.now(tz=timezone.utc).month
        filter_day = datetime.datetime.now(tz=timezone.utc).day

        running_no_1_ = EgovernmentRequest.objects.filter(
            Q(reference_no__isnull=False) &
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()
        running_no_2_ = DocumentRequest.objects.filter(
            Q(reference_no__isnull=False) &
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()
        running_no_ = "{0:0>6}".format(running_no_1_ + running_no_2_ + 1)
        request_user = CustomUser.objects.filter(id=str(request_user_id)).first()

        # Convert base64
        if request_attachment_letter_original:
            request_attachment_letter_base64 = request_attachment_letter_original.encode('utf-8')
            format, pdfstr = request_attachment_letter_base64.decode().split(';base64,') 
            ext = format.split('/')[-1] 
            request_attachment_letter = ContentFile(base64.b64decode(pdfstr), name='temp.' + ext)
        else:
            request_attachment_letter = None
            
        if request_request_type == 'RG':
            request_position_or_grade = request_items['position_or_grade']
            request_head_of_department_name = request_items['head_of_department_name']
            request_head_of_department_position = request_items['head_of_department_position']
            request_head_of_department_email = request_items['head_of_department_email']
            request_ministry_name = request_items['ministry_name']
            request_department_name = request_items['department_name']
            request_division_name = request_items['division_name']
            request_address_1 = request_items['address_1']
            request_address_2 = request_items['address_2']
            request_address_3 = request_items['address_3']
            request_city = request_items['city']
            request_postcode = request_items['postcode']
            request_state = request_items['state']
            

            new_egov_request = EgovernmentRequest.objects.create(
                user=request_user,
                request_type=request_request_type,
                position_or_grade=request_position_or_grade,
                reference_no='EGOV'+ current_year + current_month + current_day + running_no_,
                head_of_department_name=request_head_of_department_name,
                head_of_department_position=request_head_of_department_position,
                head_of_department_email=request_head_of_department_email,
                ministry_name=request_ministry_name,
                department_name=request_department_name,
                division_name=request_division_name,
                address_1=request_address_1,
                address_2=request_address_2,
                address_3=request_address_3,
                city=request_city,
                postcode=request_postcode,
                state=request_state,
                attachment_letter=request_attachment_letter
            )
        elif request_request_type == 'QU':
            new_egov_request = EgovernmentRequest.objects.create(
                user=request_user,
                request_type=request_request_type,
                reference_no='EGOV'+ current_year + current_month + current_day + running_no_,
                attachment_letter=request_attachment_letter
            )
        elif request_request_type == 'RN':
            new_egov_request = EgovernmentRequest.objects.create(
                user=request_user,
                request_type=request_request_type,
                reference_no='EGOV'+ current_year + current_month + current_day + running_no_,
                attachment_letter=request_attachment_letter
            )
        elif request_request_type == 'UI':
            request_phone_number = request_items['phone_number']
            request_position_or_grade = request_items['position_or_grade']
            request_head_of_department_name = request_items['head_of_department_name']
            request_head_of_department_position = request_items['head_of_department_position']
            request_head_of_department_email = request_items['head_of_department_email']
            request_ministry_name = request_items['ministry_name']
            request_department_name = request_items['department_name']
            request_division_name = request_items['division_name']
            request_address_1 = request_items['address_1']
            request_address_2 = request_items['address_2']
            request_address_3 = request_items['address_3']
            request_city = request_items['city']
            request_postcode = request_items['postcode']
            request_state = request_items['state']

            new_egov_request = EgovernmentRequest.objects.create(
                user=request_user,
                request_type=request_request_type,
                phone_number=request_phone_number,
                position_or_grade=request_position_or_grade,
                reference_no='EGOV'+ current_year + current_month + current_day + running_no_,
                head_of_department_name=request_head_of_department_name,
                head_of_department_position=request_head_of_department_position,
                head_of_department_email=request_head_of_department_email,
                ministry_name=request_ministry_name,
                department_name=request_department_name,
                division_name=request_division_name,
                address_1=request_address_1,
                address_2=request_address_2,
                address_3=request_address_3,
                city=request_city,
                postcode=request_postcode,
                state=request_state,
                attachment_letter=request_attachment_letter
            )


        serializer = EgovernmentRequestExtendedSerializer(new_egov_request)
        return Response(serializer.data)


    @action(methods=['GET'], detail=False)
    def extended(self, request, *args, **kwargs):

        queryset = EgovernmentRequest.objects.all().order_by('-modified_date')
        serializer_class = EgovernmentRequestExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data)


    @action(methods=['POST'], detail=True)
    def approve_user(self, request, *args, **kwargs):    

        egovernment_request_json = json.loads(request.body)    
        user_id = egovernment_request_json['user_id']
        package = egovernment_request_json['package']
        quota = egovernment_request_json['quota']
        expired_date = egovernment_request_json['expired_date']
        approver_id = egovernment_request_json['approver']
        remarks = egovernment_request_json['remarks']
        egovernment_request_ = self.get_object()

        user = CustomUser.objects.filter(id=str(user_id)).first()
        approver = CustomUser.objects.filter(id=str(approver_id)).first()

        egovernment_request_.request_status = 'AP'
        egovernment_request_.egov_package = int(package)
        egovernment_request_.egov_quota = int(quota)
        egovernment_request_.expired_date = expired_date
        egovernment_request_.remarks = remarks
        egovernment_request_.approver = approver
        egovernment_request_.save()

        user.egov_quota = int(quota)
        user.egov_package = int(package)
        user.egov_expired_date = expired_date
        user.save()
            
        serializer = EgovernmentRequestSerializer(egovernment_request_)
        return Response(serializer.data)     

    @action(methods=['POST'], detail=True)
    def reject_user(self, request, *args, **kwargs):    

        egovernment_request_json = json.loads(request.body)    
        user_id = egovernment_request_json['user_id']
        approver_id = egovernment_request_json['approver']
        remarks = egovernment_request_json['remarks']
        egovernment_request_ = self.get_object()

        user = CustomUser.objects.filter(id=str(user_id)).first()
        approver = CustomUser.objects.filter(id=str(approver_id)).first()

        egovernment_request_.request_status = 'RJ'
        egovernment_request_.remarks = remarks
        egovernment_request_.approver = approver
        egovernment_request_.save()
            
        serializer = EgovernmentRequestSerializer(egovernment_request_)
        return Response(serializer.data)          

    @action(methods=['POST'], detail=True)
    def approve_request(self, request, *args, **kwargs):

        request_ = json.loads(request.body)
        request_type = request_['request_type']
        remarks = request_['remarks']
        approver_id = request_['approver']

        egovernment_request_ = self.get_object()
        user = CustomUser.objects.filter(id=str(egovernment_request_.user.id)).first()
        approver = CustomUser.objects.filter(id=str(approver_id)).first()

        if request_type == 'QU':
            quota_ = request_['quota']
            egovernment_request_.egov_quota = int(quota_)
            egovernment_request_.request_status = 'AP'
            egovernment_request_.remarks = remarks
            egovernment_request_.approver = approver
            egovernment_request_.save()

            user.egov_quota = int(quota_) + user.egov_quota
            user.save()
        elif request_type == 'UI':
            print('update')
            user.position_or_grade = egovernment_request_.position_or_grade
            user.phone_number = egovernment_request_.phone_number
            user.head_of_department_name = egovernment_request_.head_of_department_name
            user.head_of_department_position = egovernment_request_.head_of_department_position
            user.head_of_department_email = egovernment_request_.head_of_department_email
            user.ministry_name = egovernment_request_.ministry_name
            user.department_name = egovernment_request_.department_name
            user.division_name = egovernment_request_.division_name
            user.address_1 = egovernment_request_.address_1
            user.address_2 = egovernment_request_.address_2
            user.address_3 = egovernment_request_.address_3
            user.city = egovernment_request_.city
            user.postcode = egovernment_request_.postcode
            user.state = egovernment_request_.state

            user.save()

            egovernment_request_.request_status = 'AP'
            egovernment_request_.remarks = remarks
            egovernment_request_.approver = approver
            egovernment_request_.save()
        elif request_type == 'RN':
            print('renew')
            hod_name = request_['head_of_department_name']
            hod_position = request_['head_of_department_position']
            hod_email = request_['head_of_department_email']
            attachment_letter = request_['attachment_letter']
            expired_date = ['expired_date']

            user.egov_quota = 1000
            egov_expired_date = expired_date
            user.save()

            egovernment_request_.expired_date = expired_date
            egovernment_request_.egov_quota = 1000
            egovernment_request_.request_status = 'AP'
            egovernment_request_.remarks = remarks
            egovernment_request_.save()

        serializer = EgovernmentRequestSerializer(egovernment_request_)
        return Response(serializer.data)            

    @action(methods=['POST'], detail=True)
    def reject_request(self, request, *args, **kwargs):

        request_ = json.loads(request.body)
        request_type = request_['request_type']
        remarks = request_['remarks']
        approver_id = request_['approver']

        egovernment_request_ = self.get_object()
        user = CustomUser.objects.filter(id=str(egovernment_request_.user.id)).first()
        approver = CustomUser.objects.filter(id=str(approver_id)).first()

        egovernment_request_.request_status = 'RJ'
        egovernment_request_.remarks = remarks
        egovernment_request_.approver = approver
        egovernment_request_.save()

        serializer = EgovernmentRequestSerializer(egovernment_request_)
        return Response(serializer.data)            


class EgovernmentMinistryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EgovernmentMinistry.objects.all()
    serializer_class = EgovernmentMinistrySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EgovernmentMinistry.objects.all()

        return queryset


class EgovernmentDepartmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = EgovernmentDepartment.objects.all()
    serializer_class = EgovernmentDepartmentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = EgovernmentDepartment.objects.all()

        return queryset  
    

    @action(methods=['GET'], detail=False)
    def extended(self, request, *args, **kwargs):

        queryset = EgovernmentDepartment.objects.all()
        serializer_class = EgovernmentDepartmentExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data)

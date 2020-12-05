from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Entity
)

from .serializers import (
    EntitySerializer
)

class EntityViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = [
        'local_or_foreign',
        'type_of_entity',
        'check_digit',
        'company_number'
    ]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Entity.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Entity.objects.all()
            else:
                queryset = Entity.objects.filter(company=company.id)
        """
        return queryset    
 
    @action(methods=['GET'], detail=False)
    def search(self, request, *args, **kwargs):    

        name = request.GET.get('name', '')
        entities = Entity.objects.filter(
            Q(name__icontains=name) | 
            Q(company_number__icontains=name) |
            Q(registration_number__icontains=name) |
            Q(company_number_new__icontains=name) |
            Q(registration_number_new__icontains=name) |            
            Q(audit_firm_number__icontains=name)).all()

        serializer = EntitySerializer(entities, many=True)
        return Response(serializer.data)
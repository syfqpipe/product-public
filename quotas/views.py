import hashlib
import json
import datetime

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

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Quota,
)

from .serializers import (
    QuotaSerializer,
    QuotaExtendedSerializer
)

from users.models import (
    CustomUser
)


class QuotaViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Quota.objects.all()
    serializer_class = QuotaSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = [
        'user'
    ]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Quota.objects.all()

        return queryset

    @action(methods=['POST'], detail=False)
    def check_active(self, request, *args, **kwargs):

        request_ = json.loads(request.body)
        request_user_id_ = request_['user']
        request_type_ = request_['type']
        
        request_user_ = CustomUser.objects.filter(id=request_user_id_).first()

        delta = datetime.timedelta(hours=24)
        current_time = datetime.datetime.now(tz=timezone.utc)
        date_filter = current_time - delta

        latest_quota = Quota.objects.filter(
            created_date__gte=date_filter,
            user=request_user_,
            quota_type=request_type_
        ).first()

        serializer = QuotaExtendedSerializer(latest_quota)
        return Response(serializer.data)

        
    @action(methods=['GET'], detail=False)
    def extended_egov(self, request, *args, **kwargs):

        queryset = Quota.objects.filter(
            Q(quota_type = 'E1') |
            Q(quota_type = 'E2') |
            Q(quota_type = 'E3') |
            Q(quota_type = 'E4')
        ).all()
        serializer_class = QuotaExtendedSerializer(queryset, many=True)
        
        return Response(serializer_class.data)

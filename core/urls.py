from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

import django_saml2_auth.views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView,
    attrs,
    index,
    metadata
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# Carts app

from carts.views import (
    CartViewSet
)

carts_router = router.register(
    'carts', CartViewSet
)

# Entities app

from entities.views import (
    EntityViewSet
)

entities_router = router.register(
    'entities', EntityViewSet
)

# Freeforms app

from freeforms.views import (
    FreeformViewSet
)

freeforms_router = router.register(
    'freeforms', FreeformViewSet
)

# Organisations app

from organisations.views import (
    OrganisationViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)


# Products app

from products.views import (
    ProductViewSet,
    ProductSearchCriteriaViewSet
)

products_router = router.register(
    'products', ProductViewSet
)

product_search_criterias_router = router.register(
    'product-search-criterias', ProductSearchCriteriaViewSet
)

# Quotas app

from quotas.views import (
    QuotaViewSet
)

quotas_router = router.register(
    'quotas', QuotaViewSet
)

# Services app

from services.views import (
    ServiceViewSet,
    ServiceRequestViewSet,
    DocumentRequestViewSet,
    EgovernmentRequestViewSet,
    EgovernmentMinistryViewSet,
    EgovernmentDepartmentViewSet
)

services_router = router.register(
    'services', ServiceViewSet
)
service_requests_router = router.register(
    'service-requests', ServiceRequestViewSet
)

document_requests_router = router.register(
    'document-requests', DocumentRequestViewSet
)

egovernment_requests_router = router.register(
    'egovernment-requests', EgovernmentRequestViewSet
)

egovernment_ministries_router = router.register(
    'egovernment-ministries', EgovernmentMinistryViewSet
)

egovernment_departments_router = router.register(
    'egovernment-departments', EgovernmentDepartmentViewSet
)

# Tickets app

from tickets.views import (
    TicketTopicViewSet,
    TicketSubjectViewSet,
    TicketViewSet,
    TicketCBIDViewSet,
    TicketInvestigationViewSet,
    EnquiryTicketViewSet,
    EnquiryTicketReplyViewSet,
    EnquiryTicketSelectionViewSet,
    EnquiryNoteViewSet,
    # EnquiryMediaView
)

tickets_router = router.register(
    'tickets', TicketViewSet
)

ticket_subjects_router = router.register(
    'ticket-subjects', TicketSubjectViewSet
)

ticket_topics_router = router.register(
    'ticket-topics', TicketTopicViewSet
)


enquiry_tickets_router = router.register(
    'enquiry-tickets', EnquiryTicketViewSet
)

enquiry_ticket_repliess_router = router.register(
    'enquiry-ticket-replies', EnquiryTicketReplyViewSet
)

# enquiry_ticket_selections_router = router.register(
#     'enquiry-ticket-selections', EnquiryTicketSelectionViewSet
# )

enquiry_notes_router = router.register(
    'enquiry-notes', EnquiryNoteViewSet
)

# enquiry_medias_router = router.register(
#     'enquiry-medias', EnquiryMediaSerializer
# )

# Transactions app

from transactions.views import (
    TransactionViewSet,
    RefundDropdownViewSet
)

transactions_router = router.register(
    'transactions', TransactionViewSet
)

refund_dropdowns_router = router.register(
    'refund-dropdowns', RefundDropdownViewSet
)
# Users app

from users.views import (
    CustomUserViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

urlpatterns = [
    # These are the SAML2 related URLs. You can change "^saml2_auth/" regex to
    # any path you want, like "^sso_auth/", "^sso_login/", etc. (required)
    # url(r'^saml2_auth/', include('django_saml2_auth.urls')),
    # url(r'^accounts/login/$', django_saml2_auth.views.signin),
    # url(r'^admin/login/$', django_saml2_auth.views.signin),
    url(r'^SSOLogin/$', index, name='index'),
    url(r'^SSOLogin/attrs/$', attrs, name='attrs'),
    url(r'^SSOLogin/metadata/$', metadata, name='metadata'),
    
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),
    # url(r'sso/sso_auth/', include('django_saml2_auth.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]
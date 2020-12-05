from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.files.storage import default_storage
from django.utils.timezone import make_aware

from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings
from wsgiref.util import FileWrapper


# import datetime
import json
import uuid
import tempfile
import pytz
import subprocess
import io
import xlsxwriter

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from datetime import datetime

from products.services.get_comp_prof import get_comp_prof
from products.services.get_info_acgs import get_info_acgs
from products.services.get_new_format_entity import get_new_format_entity
from products.services.get_cert_incorp import get_cert_incorp
from products.services.get_cert_reg_foreign import get_cert_reg_foreign
from products.services.get_info_comp_name_chg import get_info_comp_name_chg
from products.services.get_info_branch_listing import get_info_branch_listing
from products.services.get_info_fin2 import get_info_fin2
from products.services.get_info_fin3 import get_info_fin3
from products.services.get_info_fin5 import get_info_fin5
from products.services.get_info_fin10 import get_info_fin10
from products.services.get_info_hist2 import get_info_hist2
from products.services.get_cert_conversion import get_cert_conversion
from products.services.get_info_financial import get_info_financial
from products.services.get_roc_business_officers import get_roc_business_officers
from products.services.get_roc_changes_registered_address import get_roc_changes_registered_address
from products.services.get_details_of_shareholders import get_details_of_shareholders
from products.services.get_details_of_share_capital import get_details_of_share_capital
from products.services.get_biz_profile import get_biz_profile
from products.services.get_particulars_of_cosec import get_particulars_of_cosec
from products.services.get_info_rob_termination import get_info_rob_termination
from products.services.get_info_charges import get_info_charges
from products.services.get_comp_listing_cnt import get_comp_listing_cnt
from products.services.get_comp_listing_a import get_comp_listing_a
from products.services.get_comp_listing_b import get_comp_listing_b
from products.services.get_comp_listing_c import get_comp_listing_c
from products.services.get_comp_listing_d import get_comp_listing_d
from products.services.get_image import get_image
from products.services.get_image_view import get_image_view
from products.services.get_image_list import get_image_list
from products.services.get_image_ctc import get_image_ctc
from products.services.get_particulars_of_adt_firm import get_particulars_of_adt_firm
from products.services.get_co_count import get_co_count
from products.services.get_co_page import get_co_page

from .services.availability.get_info_charges_listing import get_info_charges_listing
from .services.availability.get_info_financial_year import get_info_financial_year
from .services.availability.get_info_acgs_query import get_info_acgs_query
from .services.availability.get_info_incorp import get_info_incorp
from .services.availability.get_list_address_changes_year import get_list_address_changes_year
from .services.availability.get_is_act_2016 import get_is_act_2016
from .services.availability.get_is_name_changed import get_is_name_changed
from .services.availability.get_is_company_converted import get_is_company_converted
from .services.availability.get_info_rob_termination_list import get_info_rob_termination_list
from .services.availability.get_info_branch_list import get_info_branch_list

from .helpers.info_acgs import info_acgs
from .helpers.roc_business_officers import roc_business_officers
from .helpers.biz_profile import biz_profile
from .helpers.particular_address import particular_address
from .helpers.cert_incorp import cert_incorp
from .helpers.info_fin_2 import info_fin_2
from .helpers.info_hist_2 import info_hist_2
from .helpers.comp_prof import comp_prof
from .helpers.mapping import status_of_comp_mapping, comp_type_mapping, state_mapping

from .helpers.acgs import acgs
from .helpers.change_name import change_name
from .helpers.particular_audit_firm import particular_audit_firm
from .helpers.company_charges import company_charges
from .helpers.particular_sharecapital import particular_sharecapital
from .helpers.particular_shareholders import particular_shareholders
from .helpers.info_rob_termination import info_rob_termination

from .models import (
    Product,
    ProductSearchCriteria
)

from .serializers import (
    ProductSerializer,
    ProductSearchCriteriaSerializer
)

class ProductViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = [
        'active',
        'ctc',
        'roc',
        'channel',
        'webservice',
        'output_type',
        'language'
    ]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Product.objects.all()

        """
        if self.request.user.is_anonymous:
            queryset = Company.objects.none()

        else:
            user = self.request.user
            company_employee = CompanyEmployee.objects.filter(employee=user)
            company = company_employee[0].company
            
            if company.company_type == 'AD':
                queryset = Product.objects.all()
            else:
                queryset = Product.objects.filter(company=company.id)
        """
        return queryset    
 

    @action(methods=['POST'], detail=False)
    def services(self, request, *args, **kwargs):        

        call_json = json.loads(request.body)        
        request_service_name = call_json['name']
        registration_number = call_json['registration_number']
        entity_type = call_json['entity_type']

        tz = pytz.timezone('Asia/Kuala_Lumpur')
        now = datetime.now(tz=tz) 
        print(now)
        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        url_info = 'http://integrasistg.ssm.com.my/InfoService/1'
        url_listing = 'http://integrasistg.ssm.com.my/ListingService/1'
        url_docu = 'http://integrasistg.ssm.com.my/DocufloService/1'

        headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }

        # New format entity
        if request_service_name == 'getNewFormatEntity': 
            json_response = get_new_format_entity(url_info, headers, registration_number, entity_type)

        # Attestation of Company Good Standing (ACGS) - Non CTC / MS EN
        elif request_service_name == 'getInfoAcgs': 
            json_response = get_info_acgs(url_info, headers, registration_number, entity_type)
        
        # Sijil Pemerbadanan Syarikat Persendirian di bawah AS 2016 - Non CTC / MS EN
        # Sijil Pemerbadanan Syarikat Awam di bawah AS 2016 - Non CTC / MS EN
        # Sijil Pemerbadanan Syarikat Awam di bawah AS 2016 - Non CTC / MS EN (menurut jaminan)
        elif request_service_name == 'getCertIncorp':
            json_response = get_cert_incorp(url_info, headers, registration_number, entity_type)

        # Sijil Pemerbadanan Syarikat Persendirian di bawah AS 2016 - CTC / MS EN
        # Sijil Pemerbadanan Syarikat Awam di bawah AS 2016 - CTC / MS EN
        # Sijil Pemerbadanan Syarikat Awam di bawah AS 2016 - CTC / MS EN (menurut jaminan)
        elif request_service_name == 'getCertIncorpCtc':
            json_response = get_cert_incorp_ctc(url_info, headers, registration_number, entity_type)
        
        # Sijil Pendaftaran Syarikat Asing di bawah AS 2016 - Non CTC / MS EN
        elif request_service_name == 'getCertRegForeign':
            json_response = get_cert_reg_foreign(url_info, headers, registration_number, entity_type)

        # Sijil Pendaftaran Syarikat Asing di bawah AS 2016 - CTC / MS EN
        elif request_service_name == 'getCertRegForeignCtc':
            json_response = get_cert_reg_foreign_ctc(url_info, headers, registration_number, entity_type)  

        # Sijil Pertukaran Nama Syarikat AS 2016 - Non CTC / MS EN
        elif request_service_name == 'getInfoCompNameChg':
            json_response = get_info_comp_name_chg(url_info, headers, registration_number, entity_type)      
        
        # Sijil Pertukaran Nama Syarikat AS 2016 - CTC / MS EN
        elif request_service_name == 'getInfoCompNameChgCtc':
            json_response = get_info_comp_name_chg_ctc(url_info, headers, registration_number, entity_type)  

        # Sijil Pertukaran Status Syarikat AS 2016 - Non CTC / MS EN
        elif request_service_name == 'getCertConversion':            
            json_response = get_cert_conversion(url_info, headers, registration_number, entity_type)  
        
        # Sijil Pertukaran Status Syarikat AS 2016 - CTC / MS EN
        elif request_service_name == 'getCertConversionCtc':            
            json_response = get_cert_conversion_ctc(url_info, headers, registration_number, entity_type) 

        # Financial Historical 2 Years - Non CTC / MS EN
        elif request_service_name == 'getInfoFinancial':            
            json_response = get_info_financial(url_info, headers, registration_number, entity_type)
        
        # Financial Historical 2 Years - CTC / MS EN
        elif request_service_name == 'getInfoFinancialCtc':            
            json_response = get_info_financial_ctc(url_info, headers, registration_number, entity_type)  
        
        # Financial Comparison 2 Years - Non CTC  / MS EN
        elif request_service_name == 'getInfoFin2':            
            json_response = get_info_fin2(url_info, headers, registration_number, entity_type)  
         
        # Financial Comparison 3 Years - Non CTC / MS EN
        elif request_service_name == 'getInfoFin3':            
            json_response = get_info_fin3(url_info, headers, registration_number, entity_type)  

        # Financial Comparison 5 Years - Non CTC / MS EN
        elif request_service_name == 'getInfoFin5':            
            json_response = get_info_fin5(url_info, headers, registration_number, entity_type)
        
        # Financial Comparison 10 Years - Non CTC / MS EN
        elif request_service_name == 'getInfoFin10':            
            json_response = get_info_fin10(url_info, headers, registration_number, entity_type) 

        # Particulars of Directors/Officers - Non CTC / MS EN
        elif request_service_name == 'getRocBusinessOfficers':            
            json_response = get_roc_business_officers(url_info, headers, registration_number, entity_type)    

        # Particulars of Directors/Officers - CTC / MS EN
        elif request_service_name == 'getRocBizOfficersCtc':            
            json_response = get_roc_business_officers_ctc(url_info, headers, registration_number, entity_type)  

        # Particulars of Registered Address - Non CTC / MS EN
        elif request_service_name == 'getRocChangesRegisteredAddress':            
            json_response = get_roc_changes_registered_address(url_info, headers, registration_number, entity_type)      

        # Particulars of Registered Address - CTC / MS EN
        elif request_service_name == 'getRocChgRegAddrCtc':            
            json_response = get_roc_changes_registered_address_ctc(url_info, headers, registration_number, entity_type) 

        # Particular of Shareholders - Non CTC / MS EN
        elif request_service_name == 'getDetailsOfShareholders':            
            json_response = get_details_of_shareholders(url_info, headers, registration_number, entity_type) 

        # Particular of Shareholders - CTC / MS EN
        elif request_service_name == 'getDtlsOfShareholdersCtc':            
            json_response = get_details_of_shareholders_ctc(url_info, headers, registration_number, entity_type)    
        
        # Particulars of Share Capital - Non CTC / MS EN
        elif request_service_name == 'getDetailsOfShareCapital':            
            json_response = get_details_of_share_capital(url_info, headers, registration_number, entity_type)     

        # Particulars of Share Capital - CTC / MS EN
        elif request_service_name == 'getDtlsOfShareCapCtc':            
            json_response = get_details_of_share_capital_ctc(url_info, headers, registration_number, entity_type) 

        # Company Profile - Non CTC / MS EN
        elif request_service_name == 'getCompProfile':
            json_response = get_comp_prof(url_info, headers, registration_number, entity_type)
        
        # Company Profile - CTC / MS EN
        elif request_service_name == 'getCompProfileCtc':
            json_response = get_comp_prof_ctc(url_info, headers, registration_number, entity_type)
        
        # Business Profile – Non CTC / MS EN
        elif request_service_name == 'getBizProfile':            
            json_response = get_biz_profile(url_info, headers, registration_number)      
        
        # Business Profile – CTC / MS EN
        elif request_service_name == 'getBizProfileCtc':            
            json_response = get_biz_profile_ctc(url_info, headers, registration_number, entity_type)   

        # Business Certificate - Digital CTC / MS EN

        # Particulars of Company Secretary - Non CTC / MS EN
        elif request_service_name == 'getParticularsOfCosec':            
            json_response = get_particulars_of_cosec(url_info, headers, registration_number, entity_type)         

        # Particulars of Company Secretary - CTC / MS EN
        elif request_service_name == 'getParticularsOfCosecCtc':            
            json_response = get_particulars_of_cosec_ctc(url_info, headers, registration_number, entity_type)  
        
        # Audit Firm Profile – Non CTC / MS EN
        elif request_service_name == 'getParticularsOfAdtFirm':            
            json_response = get_particulars_of_adt_firm(url_info, headers, registration_number, entity_type) 

        # Audit Firm Profile – CTC / MS EN
        elif request_service_name == 'getParticularsOfAdtFirmCtc':            
            json_response = get_particulars_of_adt_firm_ctc(url_info, headers, registration_number, entity_type) 

        # Business Termination Letter (BTL) - Non CTC / MS EN
        elif request_service_name == 'getInfoRobTermination':            
            json_response = get_info_rob_termination(url_info, headers, registration_number, entity_type)                                                               
        
        # Company Charges - Non CTC / MS EN
        elif request_service_name == 'getInfoCharges':            
            json_response = get_info_charges(url_info, headers, registration_number, entity_type)  

        # Company Charges - CTC / MS EN
        elif request_service_name == 'getInfoChargesCtc':            
            json_response = get_info_charges_ctc(url_info, headers, registration_number, entity_type)  

        # Company Listing
        elif request_service_name == 'getCompListingCnt':            
            json_response = get_comp_listing_cnt(url_listing, headers, registration_number, entity_type)          

        # Company Listing Package A
        elif request_service_name == 'getCompListingA':            
            json_response = get_comp_listing_a(url_listing, headers, registration_number, entity_type)      

        # Company Listing Package B
        elif request_service_name == 'getCompListingB':            
            json_response = get_comp_listing_b(url_listing, headers, registration_number, entity_type)  

        # Document and Form View + Download getImageView / getImageList
        elif request_service_name == 'getImage':            
            json_response = get_image(url_docu, headers, registration_number, entity_type)  

        elif request_service_name == 'getImageList':            
            json_response = get_image_list(url_docu, headers, registration_number, entity_type) 

        # Document and Form View + Download + CTC getImageViewCTC

        elif request_service_name == 'getImageView':            
            json_response = get_image_list(url_docu, headers, registration_number, entity_type) 

        # Document and Form View (Statutory Docs)  getImageCtc

        elif request_service_name == 'getImageCtc':            
            json_response = get_image_ctc(url_docu, headers, registration_number, entity_type)    

        elif request_service_name == 'getCoCount':
            json_response = get_co_count(url_info, headers, registration_number, entity_type) 

        elif request_service_name == 'getCoPage':
            json_response = get_co_page(url_info, headers, registration_number, entity_type)             

        return JsonResponse(json_response)

    @action(methods=['POST'], detail=False)
    def check_availability(self, request, *args, **kwargs):

        product_request_json = json.loads(request.body)

        registration_ = product_request_json['registration_no']
        entity_type_ = product_request_json['entity_type']

        information_url = 'http://integrasistg.ssm.com.my/InfoService/1'

        now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        request_headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }

        info_charges = get_info_charges_listing(information_url, request_headers, registration_)
        financial_year = get_info_financial_year(information_url, request_headers, registration_)
        acgs = get_info_acgs_query(information_url, request_headers, registration_)
        info_incorp_share = get_info_incorp(information_url, request_headers, registration_, 'share')
        list_address_changes_year = get_list_address_changes_year(information_url, request_headers, registration_)
        is_incorp_act_2016 = get_is_act_2016(information_url, request_headers, registration_)
        info_incorp_reg = get_info_incorp(information_url, request_headers, registration_, 'reg')
        is_name_changed = get_is_name_changed(information_url, request_headers, registration_)
        is_company_converted = get_is_company_converted(information_url, request_headers, registration_)
        info_termination_list = get_info_rob_termination_list(information_url, request_headers, registration_)
        info_branch_list = get_info_branch_list(information_url, request_headers, registration_) 

        data_json = {
            'info_charges': info_charges,
            'financial_year': financial_year, 
            'acgs': acgs,
            'shareholders': info_incorp_share,
            'share_capital': info_incorp_share,
            'list_address_changes_year': list_address_changes_year,
            'info_incorp_reg': is_incorp_act_2016,
            'is_name_changed': is_name_changed,
            'info_incorp': info_incorp_reg,
            'is_company_converted': is_company_converted,
            'info_termination_list': info_termination_list,
            'info_branch_list': info_branch_list
        }   

        return JsonResponse(data_json)


    @action(methods=['POST'], detail=False)
    def generate_product(self, request, *args, **kwargs):

        product_request_json = json.loads(request.body)

        name_ = product_request_json['name']
        language_ = product_request_json['language']
        ctc_ = product_request_json['ctc']
        registration_ = product_request_json['registration_no']
        entity_type_ = product_request_json['entity_type']

        information_url = 'http://integrasistg.ssm.com.my/InfoService/1'
        listing_url = 'http://integrasistg.ssm.com.my/ListingService/1'
        document_url = 'http://integrasistg.ssm.com.my/DocufloService/1'

        now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        request_headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }

        css_file = 'https://pipeline-project.sgp1.digitaloceanspaces.com/mbpp-elatihan/css/template.css'        
        #css_file = 'http://127.0.0.1:8000/static/css/template.css'

        new_entity_id = get_new_format_entity(information_url, request_headers, registration_, entity_type_)

        if name_ == 'acgs':
            middleware_data = get_info_acgs(information_url, request_headers, registration_, entity_type_)
            latest_doc_date = get_comp_prof(information_url, request_headers, registration_, entity_type_)['rocCompanyInfo']['latestDocUpdateDate']
            middleware_data['latest_doc_date'] = latest_doc_date
            data_loaded = acgs(middleware_data, new_entity_id, language_)

        elif name_ == 'certificate_of_incorporation_registration':
            middleware_data = get_cert_incorp(information_url, request_headers, registration_)
            data_loaded = cert_incorp(middleware_data, new_entity_id, language_)

            if middleware_data['companyStatus'] == 'U':
                if middleware_data['companyType'] == 'S':
                    name_ = 'public_incorp_cert'
                else:
                    name_ = 'public_guarantee_incorp_cert'
            else:
                name_ = 'certificate_of_incorporation_registration'

            if middleware_data['localforeignCompany'] != 'L':
                name_ = 'foreign_incorp_cert'

        # elif name_ == 'public_incorp_cert':
        #     middleware_data = get_cert_incorp(information_url, request_headers, registration_)
        #     data_loaded = cert_incorp(middleware_data, new_entity_id, language_)

        # elif name_ == 'public_guarantee_incorp_cert':
        #     middleware_data = get_cert_incorp(information_url, request_headers, registration_)
        #     data_loaded = cert_incorp(middleware_data, new_entity_id, language_)

        # elif name_ == 'foreign_incorp_cert':
        #     middleware_data = get_cert_reg_foreign(information_url, request_headers, registration_)
        #     data_loaded = cert_incorp(middleware_data, new_entity_id, language_)

        elif name_ == 'certificate_of_change_of_name':
            middleware_data = get_info_comp_name_chg(information_url, request_headers, registration_)
            data_loaded = change_name(middleware_data, new_entity_id, language_)

        elif name_ == 'certificate_of_conversion':
            middleware_data = get_cert_conversion(information_url, request_headers, registration_)
            data_loaded = change_name(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_historical':
            year1 = product_request_json['year1']
            year2 = product_request_json['year2']
            middleware_data_year1 = get_info_hist2(information_url, request_headers, registration_, entity_type_, year1)
            middleware_data_year2 = get_info_hist2(information_url, request_headers, registration_, entity_type_, year2)
            data_loaded_1 = info_hist_2(middleware_data_year1,new_entity_id, language_)
            data_loaded_2 = info_hist_2(middleware_data_year2,new_entity_id, language_)
            data_loaded = data_loaded_1

            
            balance_sheet_year1 = data_loaded_1['balance_sheet'][0]
            balance_sheet_year2 = data_loaded_2['balance_sheet'][0]
            
            profit_loss_year1 = data_loaded_1['profit_loss'][0]
            profit_loss_year2 = data_loaded_2['profit_loss'][0]

            del data_loaded['balance_sheet']
            del data_loaded['profit_loss']
            data_loaded['balance_sheet'] = []
            data_loaded['profit_loss'] = []

            data_loaded['balance_sheet'].append(balance_sheet_year1)
            data_loaded['balance_sheet'].append(balance_sheet_year2)
            data_loaded['profit_loss'].append(profit_loss_year1)
            data_loaded['profit_loss'].append(profit_loss_year2)

            print(data_loaded)

        elif name_ == 'financial_comparison_2':
            now = datetime.now()
            middleware_data = get_info_fin2(information_url, request_headers, registration_, entity_type_, str(now.year-2), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_comparison_3':
            now = datetime.now()
            middleware_data = get_info_fin3(information_url, request_headers, registration_, entity_type_, str(now.year-3), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_comparison_5':
            now = datetime.now()
            middleware_data = get_info_fin5(information_url, request_headers, registration_, entity_type_, str(now.year-5), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_comparison_10':
            now = datetime.now()
            middleware_data = get_info_fin10(information_url, request_headers, registration_, entity_type_, str(now.year-10), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'particulars_of_directors_officers':
            middleware_data = get_roc_business_officers(information_url, request_headers, registration_, entity_type_)
            data_loaded = roc_business_officers(middleware_data, new_entity_id, language_)  

        elif name_ == 'particulars_of_registered_address':
            middleware_data = get_roc_changes_registered_address(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_address(middleware_data, new_entity_id, language_)  

        elif name_ == 'particulars_of_shareholders':
            middleware_data = get_details_of_shareholders(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_shareholders(middleware_data, new_entity_id, language_)  

        elif name_ == 'particulars_of_share_capital':
            middleware_data = get_details_of_share_capital(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_sharecapital(middleware_data, new_entity_id, language_,entity_type_)

        elif name_ == 'company_profile':
            now = datetime.now()
            middleware_data = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            data_loaded = comp_prof(middleware_data, new_entity_id, language_)  

        elif name_ == 'business_profile':
            print(entity_type_ )
            middleware_data = get_biz_profile(information_url, request_headers, registration_)
            data_loaded = biz_profile(middleware_data, new_entity_id, language_)

        elif name_ == 'particulars_of_company_secretary':
            middleware_data = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            data_loaded = comp_prof(middleware_data, new_entity_id, language_)   

        elif name_ == 'audit_firm_profile':
            middleware_data = get_particulars_of_adt_firm(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_audit_firm(middleware_data, new_entity_id, language_)  

        elif name_ == 'business_termination_letter':
            middleware_data = get_info_rob_termination(information_url, request_headers, registration_)
            data_loaded = info_rob_termination(middleware_data, new_entity_id, language_)

        elif name_ == 'company_charges':
            com_profile = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            middleware_data = get_info_charges(information_url, request_headers, registration_, entity_type_)
            data_loaded = company_charges(middleware_data, new_entity_id, com_profile, language_, entity_type_)

        elif name_ == 'foreign_change_name':
            middleware_data = get_info_charges(information_url, request_headers, registration_, entity_type_)
            data_loaded = change_name(middleware_data, new_entity_id, language_)            

        else:
            pass
        

        if language_ == 'en':
            html_string = render_to_string('product/'+ name_ +'_en.html', {'data': data_loaded})

        elif language_ == 'ms':
            html_string = render_to_string('product/'+ name_ +'_ms.html', {'data': data_loaded})

        if 'pdf' in product_request_json:
            if product_request_json['pdf'] == False:
                serializer = data_loaded
                return Response(serializer)


            
        html = HTML(string=html_string)
        #pdf_file = html.write_pdf(stylesheets=[CSS(css_file)])
        pdf_file = html.write_pdf()
            
        file_path = "ssm/product/" + name_ + "-" + datetime.utcnow().strftime("%s") + "-" + uuid.uuid4().hex + '.pdf'
        saved_file = default_storage.save(
            file_path, 
            ContentFile(pdf_file)
        )
            
        full_url_path = settings.MEDIA_ROOT + saved_file

        serializer = data_loaded
        serializer['pdflink'] = 'https://pipeline-project.sgp1.digitaloceanspaces.com/' + file_path
        return Response(serializer)


    @action(methods=['POST'], detail=False)
    def generate_image(self, request, *args, **kwargs):

        product_request_json = json.loads(request.body)

        name_ = product_request_json['name'] # Either 'list' or 'specific'
        registration_ = product_request_json['registration_no']
        entity_type_ = product_request_json['entity_type']

        information_url = 'http://integrasistg.ssm.com.my/InfoService/1'
        document_url = 'http://integrasistg.ssm.com.my/DocufloService/1'

        now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        request_headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }

        if entity_type_ == 'ROC':
            check_digit = get_comp_prof(information_url, request_headers, registration_, entity_type_)['rocCompanyInfo']['checkDigit']
        elif entity_type_ == 'ROB':
            check_digit = get_biz_profile(information_url, request_headers, registration_)['robBusinessInfo']['checkDigit']

        if name_ == 'list':
            middleware_data = get_image_view(document_url, request_headers, registration_, entity_type_, check_digit)
            data_ = middleware_data['documentInfos']['documentInfos']
        else:
            version_id = int(product_request_json['version_id'])
            middleware_data = get_image(document_url, request_headers, registration_, entity_type_, check_digit, version_id)
            data_ = middleware_data['docContent']
        
        return Response(data_)


    @action(methods=['POST'], detail=False)
    def generate_branch_list(self, request, *args, **kwargs):
        
        product_request_json = json.loads(request.body)

        registration_ = product_request_json['registration_no']

        info_url = 'http://integrasistg.ssm.com.my/InfoService/1'

        now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        request_headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }

        middleware_data = get_info_branch_listing(info_url, request_headers, registration_)
        data_ = middleware_data

        return Response(data_)


    @action(methods=['POST'], detail=False)
    def generate_list(self, request, *args, **kwargs): 
        import xlsxwriter

        product_request_json = json.loads(request.body)
        a_ = product_request_json

        name_ = product_request_json['name']
        package_ = product_request_json['package']

        information_url = 'http://integrasistg.ssm.com.my/InfoService/1'
        document_url = 'http://integrasistg.ssm.com.my/DocufloService/1'
        listing_url = 'http://integrasistg.ssm.com.my/ListingService/1'

        now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        request_headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }

        if name_ == "list":
            if package_ == 'A':

                middleware_data = get_comp_listing_a(listing_url, request_headers, 
                    a_['bizCode'], 
                    a_['compLocation'], 
                    a_['compOrigin'], 
                    a_['compStatus'], 
                    a_['compType'], 
                    a_['incorpDtFrom'], 
                    a_['incorpDtTo'], 
                    1)     

                data_ = middleware_data
                return Response(data_)                                       

            elif package_ == 'B':

                middleware_data = get_comp_listing_b(listing_url, request_headers, 
                    a_['bizCode'], 
                    a_['compLocation'], 
                    a_['compOrigin'], 
                    a_['compStatus'], 
                    a_['compType'], 
                    a_['incorpDtFrom'], 
                    a_['incorpDtTo'], 
                    1,
                    a_['directorNat'],
                    a_['shareholderNat'])     

                data_ = middleware_data
                return Response(data_)   

            elif package_ == 'C':
                pass
            elif package_ == 'D':
                pass
        elif name_ == 'excel':
            if package_ == 'A':

                middleware_data = get_comp_listing_a(listing_url, request_headers, 
                        a_['bizCode'], 
                        a_['compLocation'], 
                        a_['compOrigin'], 
                        a_['compStatus'], 
                        a_['compType'], 
                        a_['incorpDtFrom'], 
                        a_['incorpDtTo'], 
                        1) 
                output = io.BytesIO()
 
                workbook = xlsxwriter.Workbook(output)
                worksheet2 = workbook.add_worksheet('COMPANY INFORMATION')

                data2 = [["No.","Company No.","Company Name","Old Company Name","Entity Type","Company Type","Company Status","Incorp. Date"]]
                count = 1

                for co in middleware_data['company']:
                    count += 1
                    new_row = [count, co["compInfo"]["compNo"] + '-' + co["compInfo"]["chkDigit"], co["compInfo"]["compName"], co["compInfo"]["compOldNm"], "LOCAL", comp_type_mapping(co["compInfo"]["compType"], 'en'), status_of_comp_mapping(co["compInfo"]["compStatus"]), co["compInfo"]["incorpDt"] ]
                    data2.append(new_row)

                for row_num, columns in enumerate(data2):
                    for col_num, cell_data in enumerate(columns):
                        worksheet2.write(row_num, col_num, cell_data)

                worksheet3 = workbook.add_worksheet('ADDRESS')

                data3 = [["No.","Company No.","Company Name","Registered Address", "Business Address"]]
                count = 1

                for co in middleware_data['company']:
                    count += 1

                    if co["regAddress"]["address3"]:
                        registered_address = co["regAddress"]["address1"] + co["regAddress"]["address2"] + co["regAddress"]["address3"] + co["regAddress"]["town"] + co["regAddress"]["postcode"] +   state_mapping(co["regAddress"]["stateCode"])
                    else: 
                        registered_address = co["regAddress"]["address1"] + co["regAddress"]["address2"] + co["regAddress"]["town"] + co["regAddress"]["postcode"] + state_mapping(co["regAddress"]["stateCode"])

                    if co["busAddress"]["address3"]:
                        business_address = co["busAddress"]["address1"] + co["busAddress"]["address2"] + co["busAddress"]["address3"] + co["busAddress"]["town"] + co["busAddress"]["postcode"] +   state_mapping(co["busAddress"]["stateCode"])
                    else: 
                        business_address = co["busAddress"]["address1"] + co["busAddress"]["address2"] + co["busAddress"]["town"] + co["busAddress"]["postcode"] + state_mapping(co["busAddress"]["stateCode"])


                    new_row = [count, co["compInfo"]["compNo"] + '-' + co["compInfo"]["chkDigit"], co["compInfo"]["compName"], registered_address, business_address]
                    data3.append(new_row)

                for row_num, columns in enumerate(data3):
                    for col_num, cell_data in enumerate(columns):
                        worksheet3.write(row_num, col_num, cell_data)  

                worksheet4 = workbook.add_worksheet('NATURE OF BUSINESS')

                data4 = [["No.","Company No.","Company Name","Business Code", "Description", "Priotiy"]]
                count = 1

                for co in middleware_data['company']:
                    count += 1
                    new_row = [count, co["compInfo"]["compNo"] + '-' + co["compInfo"]["chkDigit"], co["compInfo"]["compName"], co["bizCodes"]["code"], co["bizCodes"]["descEng"],co["bizCodes"]["priority"] ]
                    data4.append(new_row)

                for row_num, columns in enumerate(data4):
                    for col_num, cell_data in enumerate(columns):
                        worksheet4.write(row_num, col_num, cell_data)


                workbook.close()
                output.seek(0)   

                filename = 'PackageA.xlsx'
                response = HttpResponse(
                    output,
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response   

            elif package_ == 'B':

                middleware_data = get_comp_listing_a(listing_url, request_headers, 
                        a_['bizCode'], 
                        a_['compLocation'], 
                        a_['compOrigin'], 
                        a_['compStatus'], 
                        a_['compType'], 
                        a_['incorpDtFrom'], 
                        a_['incorpDtTo'], 
                        1,
                        a_['directorNat'],
                        a_['shareholderNat']) 
                output = io.BytesIO()
 
                workbook = xlsxwriter.Workbook(output)
                worksheet2 = workbook.add_worksheet('COMPANY INFORMATION')

                data2 = [["No.","Company No.","Company Name","Old Company Name","Entity Type","Company Type","Company Status","Incorp. Date"]]
                count = 1

                for co in middleware_data['company']:
                    count += 1
                    new_row = [count, co["compInfo"]["compNo"] + '-' + co["compInfo"]["chkDigit"], co["compInfo"]["compName"], co["compInfo"]["compOldNm"], "LOCAL", comp_type_mapping(co["compInfo"]["compType"], 'en'), status_of_comp_mapping(co["compInfo"]["compStatus"]), co["compInfo"]["incorpDt"] ]
                    data2.append(new_row)

                for row_num, columns in enumerate(data2):
                    for col_num, cell_data in enumerate(columns):
                        worksheet2.write(row_num, col_num, cell_data)

                worksheet3 = workbook.add_worksheet('ADDRESS')

                data3 = [["No.","Company No.","Company Name","Registered Address", "Business Address"]]
                count = 1

                for co in middleware_data['company']:
                    count += 1

                    if co["regAddress"]["address3"]:
                        registered_address = co["regAddress"]["address1"] + co["regAddress"]["address2"] + co["regAddress"]["address3"] + co["regAddress"]["town"] + co["regAddress"]["postcode"] +   state_mapping(co["regAddress"]["stateCode"])
                    else: 
                        registered_address = co["regAddress"]["address1"] + co["regAddress"]["address2"] + co["regAddress"]["town"] + co["regAddress"]["postcode"] + state_mapping(co["regAddress"]["stateCode"])

                    if co["busAddress"]["address3"]:
                        business_address = co["busAddress"]["address1"] + co["busAddress"]["address2"] + co["busAddress"]["address3"] + co["busAddress"]["town"] + co["busAddress"]["postcode"] +   state_mapping(co["busAddress"]["stateCode"])
                    else: 
                        business_address = co["busAddress"]["address1"] + co["busAddress"]["address2"] + co["busAddress"]["town"] + co["busAddress"]["postcode"] + state_mapping(co["busAddress"]["stateCode"])


                    new_row = [count, co["compInfo"]["compNo"] + '-' + co["compInfo"]["chkDigit"], co["compInfo"]["compName"], registered_address, business_address]
                    data3.append(new_row)

                for row_num, columns in enumerate(data3):
                    for col_num, cell_data in enumerate(columns):
                        worksheet3.write(row_num, col_num, cell_data)  

                worksheet4 = workbook.add_worksheet('NATURE OF BUSINESS')

                data4 = [["No.","Company No.","Company Name","Business Code", "Description", "Priotiy"]]
                count = 1

                for co in middleware_data['company']:
                    count += 1
                    new_row = [count, co["compInfo"]["compNo"] + '-' + co["compInfo"]["chkDigit"], co["compInfo"]["compName"], co["bizCodes"]["code"], co["bizCodes"]["descEng"],co["bizCodes"]["priority"] ]
                    data4.append(new_row)

                for row_num, columns in enumerate(data4):
                    for col_num, cell_data in enumerate(columns):
                        worksheet4.write(row_num, col_num, cell_data)


                workbook.close()
                output.seek(0)   

                filename = 'PackageA.xlsx'
                response = HttpResponse(
                    output,
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response    
                          
            else:
                return Response({})
    

    @action(methods=['POST'], detail=False)
    def generate_egov(self, request, *args, **kwargs):

        product_request_json = json.loads(request.body)

        name_ = product_request_json['name']
        language_ = product_request_json['language']
        ctc_ = product_request_json['ctc']
        registration_ = product_request_json['registration_no']
        entity_type_ = product_request_json['entity_type']

        information_url = 'http://integrasistg.ssm.com.my/InfoService/1'
        listing_url = 'http://integrasistg.ssm.com.my/ListingService/1'
        document_url = 'http://integrasistg.ssm.com.my/DocufloService/1'

        now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")

        request_headers = {
            'content-type': "text/xml;charset=UTF-8",
            'authorization': auth_code
        }
      
        #css_file = 'http://127.0.0.1:8000/static/css/template.css'

        new_entity_id = get_new_format_entity(information_url, request_headers, registration_, entity_type_)

        if name_ == 'acgs':
            middleware_data = get_info_acgs(information_url, request_headers, registration_, entity_type_)
            latest_doc_date = get_comp_prof(information_url, request_headers, registration_, entity_type_)['rocCompanyInfo']['latestDocUpdateDate']
            middleware_data['latest_doc_date'] = latest_doc_date
            data_loaded = acgs(middleware_data, new_entity_id, language_)

        elif name_ == 'certificate_of_incorporation_registration':
            middleware_data = get_cert_incorp(information_url, request_headers, registration_)
            data_loaded = cert_incorp(middleware_data, new_entity_id, language_)

            if middleware_data['companyStatus'] == 'U':
                if middleware_data['companyType'] == 'S':
                    name_ = 'public_incorp_cert'
                else:
                    name_ = 'public_guarantee_incorp_cert'
            else:
                name_ = 'certificate_of_incorporation_registration'

            if middleware_data['localforeignCompany'] != 'L':
                name_ = 'foreign_incorp_cert'

        elif name_ == 'certificate_of_change_of_name':
            middleware_data = get_info_comp_name_chg(information_url, request_headers, registration_)
            data_loaded = change_name(middleware_data, new_entity_id, language_)

        elif name_ == 'certificate_of_conversion':
            middleware_data = get_cert_conversion(information_url, request_headers, registration_)
            data_loaded = change_name(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_historical':
            year1 = product_request_json['year1']
            year2 = product_request_json['year2']
            middleware_data_year1 = get_info_hist2(information_url, request_headers, registration_, entity_type_, year1)
            middleware_data_year2 = get_info_hist2(information_url, request_headers, registration_, entity_type_, year2)
            data_loaded_1 = info_hist_2(middleware_data_year1,new_entity_id, language_)
            data_loaded_2 = info_hist_2(middleware_data_year2,new_entity_id, language_)
            data_loaded = data_loaded_1

            balance_sheet_year1 = data_loaded_1['balance_sheet'][0]
            balance_sheet_year2 = data_loaded_2['balance_sheet'][0]
            
            profit_loss_year1 = data_loaded_1['profit_loss'][0]
            profit_loss_year2 = data_loaded_2['profit_loss'][0]

            del data_loaded['balance_sheet']
            del data_loaded['profit_loss']
            data_loaded['balance_sheet'] = []
            data_loaded['profit_loss'] = []

            data_loaded['balance_sheet'].append(balance_sheet_year1)
            data_loaded['balance_sheet'].append(balance_sheet_year2)
            data_loaded['profit_loss'].append(profit_loss_year1)
            data_loaded['profit_loss'].append(profit_loss_year2)

            # print(data_loaded)

        elif name_ == 'financial_comparison_2':
            now = datetime.now()
            middleware_data = get_info_fin2(information_url, request_headers, registration_, entity_type_, str(now.year-2), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_comparison_3':
            now = datetime.now()
            middleware_data = get_info_fin3(information_url, request_headers, registration_, entity_type_, str(now.year-3), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_comparison_5':
            now = datetime.now()
            middleware_data = get_info_fin5(information_url, request_headers, registration_, entity_type_, str(now.year-5), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'financial_comparison_10':
            now = datetime.now()
            middleware_data = get_info_fin10(information_url, request_headers, registration_, entity_type_, str(now.year-10), str(now.year))
            data_loaded = info_fin_2(middleware_data, new_entity_id, language_)

        elif name_ == 'particulars_of_directors_officers':
            middleware_data = get_roc_business_officers(information_url, request_headers, registration_, entity_type_)
            data_loaded = roc_business_officers(middleware_data, new_entity_id, language_)  

        elif name_ == 'particulars_of_registered_address':
            middleware_data = get_roc_changes_registered_address(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_address(middleware_data, new_entity_id, language_)  

        elif name_ == 'particulars_of_shareholders':
            middleware_data = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            data_loaded = comp_prof(middleware_data, new_entity_id, language_)  

        elif name_ == 'particulars_of_share_capital':
            middleware_data = get_details_of_share_capital(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_sharecapital(middleware_data, new_entity_id, language_,entity_type_)

        elif name_ == 'company_profile':
            now = datetime.now()
            middleware_data = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            data_loaded = comp_prof(middleware_data, new_entity_id, language_)  

        elif name_ == 'business_profile':
            # print(entity_type_ )
            middleware_data = get_biz_profile(information_url, request_headers, registration_)
            data_loaded = biz_profile(middleware_data, new_entity_id, language_)

        elif name_ == 'particulars_of_company_secretary':
            middleware_data = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            data_loaded = comp_prof(middleware_data, new_entity_id, language_)   

        elif name_ == 'audit_firm_profile':
            middleware_data = get_particulars_of_adt_firm(information_url, request_headers, registration_, entity_type_)
            data_loaded = particular_audit_firm(middleware_data, new_entity_id, language_)  

        elif name_ == 'business_termination_letter':
            middleware_data = get_info_rob_termination(information_url, request_headers, registration_)
            data_loaded = info_rob_termination(middleware_data, new_entity_id, language_)

        elif name_ == 'company_charges':
            com_profile = get_comp_prof(information_url, request_headers, registration_, entity_type_)
            middleware_data = get_info_charges(information_url, request_headers, registration_, entity_type_)
            data_loaded = company_charges(middleware_data, new_entity_id, com_profile, language_, entity_type_)

        elif name_ == 'foreign_change_name':
            middleware_data = get_info_charges(information_url, request_headers, registration_, entity_type_)
            data_loaded = change_name(middleware_data, new_entity_id, language_)            

        else:
            pass

        serializer = data_loaded
        return Response(serializer)
    

    @action(methods=['GET'], detail=False)
    def lala(self, request, *args, **kwargs):

        output = io.BytesIO()
 
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Sheet One')

        data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

        for row_num, columns in enumerate(data):
            for col_num, cell_data in enumerate(columns):
                worksheet.write(row_num, col_num, cell_data)

        workbook.close()
        output.seek(0)   

        filename = 'PackageA.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename                               
        return response             


class ProductSearchCriteriaViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ProductSearchCriteria.objects.all()
    serializer_class = ProductSearchCriteriaSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = ProductSearchCriteria.objects.all()

        return queryset 
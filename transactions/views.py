import hashlib
import json
import datetime
import pytz
import uuid
import xlsxwriter
import csv
import io

from django.utils.timezone import make_aware

from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.db.models import Q
from django.utils import timezone
from django.core.files.storage import default_storage

from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings
from wsgiref.util import FileWrapper

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Transaction,
    RefundDropdown
)

from .serializers import (
    TransactionSerializer,
    TransactionWithCartSerializer,
    TransactionExtendedSerializer,
    RefundDropdownSerializer
)

from carts.models import (
    Cart,
    CartItem
)

from services.models import (
    ServiceRequest
)

from entities.models import (
    Entity
)

from products.models import (
    Product
)

class TransactionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['reference']


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset

    
    @action(methods=['GET'], detail=False)
    def with_cart(self, request, *args, **kwargs):  

        transactions = Transaction.objects.all().order_by('-created_date')

        serializer = TransactionExtendedSerializer(transactions, many=True)
        return Response(serializer.data)


    @action(methods=['POST'], detail=False)
    def pg_return(self, request, *args, **kwargs):  

        reference = request.POST.get("PaymentID", "")   
        pg_transaction_id = request.POST.get("TxnID", "")
        transaction_method = request.POST.get("PymtMethod", "")
        transaction_status = request.POST.get("TxnStatus", "")[0]
        pg_transaction_type = request.POST.get('TransactionType', '')
        pg_transaction_payment_method = request.POST.get('PymtMethod', '')
        pg_transaction_message = request.POST.get('TxnMessage', '')
        pg_transaction_card_holder = request.POST.get('CardHolder', '')
        pg_transaction_card_no_mask = request.POST.get('CardNoMask', '')
        # print('tt', request.POST.get("PymtMethod", ""))
        print('______________')
        print('Reference', reference)
        print('PG Transaction ID', pg_transaction_id)
        
        transaction = Transaction.objects.filter(reference=reference).first()

        print('\n')
        print(transaction.cart)
        cart = Cart.objects.filter(id=transaction.cart.id).first()
        print(cart.cart_status)

        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')
        
        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)
        
        filter_year = datetime.datetime.now(tz=timezone.utc).year
        filter_month = datetime.datetime.now(tz=timezone.utc).month
        filter_day = datetime.datetime.now(tz=timezone.utc).day

        transaction.transaction_id = pg_transaction_id
        transaction_id_unix = str(int(transaction.created_date.timestamp()))[-6:]
        # print('ori', int(transaction.created_date.timestamp()))
        # print('edite', transaction_id_unix)
        
        transaction.transaction_type = pg_transaction_type
        transaction.payment_method = pg_transaction_payment_method
        transaction.transaction_message = pg_transaction_message
        transaction.card_holder = pg_transaction_card_holder
        transaction.card_no_mask = pg_transaction_card_no_mask

        transaction.reference_no = 'P' + current_year + current_month + transaction_id_unix
        transaction_length = Transaction.objects.filter(
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day) &
            Q(receipt_no__isnull=False)
        ).count()
        transaction_running_no = "{0:0>6}".format(transaction_length + 1)

        css_file = 'https://pipeline-project.sgp1.digitaloceanspaces.com/mbpp-elatihan/css/template.css'
        
        # return Response(serializer)

        # transaction 0 - successful
        if transaction_status == '0':
            transaction.payment_status = 'OK'
            transaction.payment_gateway_update_date = datetime.datetime.now(timezone_)

            transaction.receipt_no = 'PP' + current_year + current_month + current_day + transaction_running_no
            
            cart.cart_status = 'CM'

            cart_items = CartItem.objects.filter(cart=cart.id)

            for item in cart_items:
                product_length = CartItem.objects.filter(
                    Q(cart_item_type = 'PR') &
                    Q(order_no__isnull=False) &
                    Q(created_date__year=filter_year) &
                    Q(created_date__month=filter_month) &
                    Q(created_date__day=filter_day)
                ).count()
                order_running_no = "{0:0>6}".format(product_length + 1)
                print('running > ', order_running_no)

                if item.cart_item_type == 'PR':
                    item.order_no = 'PD' + current_year + current_month + current_day + order_running_no
                    item.save()

            data_loaded = {
                'transaction': transaction,
                'cart_items': cart_items
            }
            # data_loaded['transaction'].created_date = datetime.datetime(data_loaded['transaction'].created_date).strftime("%Y-%m-%d")
            index_counter = 1

            for item in data_loaded['cart_items']:
                # item['index'] = index_counter
                index_counter = index_counter + 1
                # item['index'] = index_counter

                if item.product:
                    item.product.fee = format(item.product.fee/100, '.2f')
                    print('he')
                elif item.product_search_criteria:
                    item.product_search_criteria.total_price = format(item.product_search_criteria.total_price/100, '.2f')
                    print('he')
                elif item.service_request:
                    item.service_request.service.fee = format(item.service_request.service.fee/100, '.2f')
                    print('he')

            total_amount_original = data_loaded['transaction'].total_amount

            data_loaded['transaction'].total_amount = format(total_amount_original/100, '.2f')

            html_string = render_to_string('receipt/receipt.html', {'data': data_loaded})
            html = HTML(string=html_string)
            pdf_file = html.write_pdf(stylesheets=[CSS(css_file)])
            # pdf_file = html.write_pdf()
                
            file_path = "ssm/receipt/ssm-receipt" + "-" + datetime.datetime.utcnow().strftime("%s") + '.pdf'
            saved_file = default_storage.save(
                file_path, 
                ContentFile(pdf_file)
            )
                
            full_url_path = settings.MEDIA_ROOT + saved_file
            lol_ = file_path
            print(lol_)
            print('oiiii', total_amount_original)
            data_loaded['transaction'].total_amount = total_amount_original
            transaction.receipt = full_url_path
            
            transaction.save()
            cart.save()

        # transaction 1 - failed
        elif transaction_status == '1':
            transaction.payment_status = 'FL'
            transaction.payment_gateway_update_date = datetime.datetime.now(tz=timezone.utc)
            transaction.payment_method = transaction_method
            transaction.receipt_no = 'PP' + current_year + current_month + current_day + transaction_running_no
            transaction.save()

            cart.cart_status = 'AB'
            cart.save()            

        # transaction 2 - pending
        elif transaction_status == '2':
            transaction.payment_status = 'PD'
            transaction.payment_gateway_update_date = datetime.datetime.now(tz=timezone.utc)
            transaction.payment_method = transaction_method
            transaction.receipt_no = 'PP' + current_year + current_month + current_day + transaction_running_no
            transaction.save()
        
        print('______________')
        # portal.ssm.prototype.com.my
        # url = 'https://portal.ssm.prototype.com.my/#/payment/return?transactionId=' + reference
        url = 'https://xcessdev.ssm.com.my/#/payment/return?transactionId=' + reference
        return redirect(url)      


    @action(methods=['POST'], detail=True)
    def encode(self, request, *args, **kwargs):
        
        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')
        
        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)
        
        filter_year = datetime.datetime.now(tz=timezone.utc).year
        filter_month = datetime.datetime.now(tz=timezone.utc).month
        filter_day = datetime.datetime.now(tz=timezone.utc).day

        transaction_length = Transaction.objects.filter(
            Q(created_date__year=filter_year) &
            Q(created_date__month=filter_month) &
            Q(created_date__day=filter_day)
        ).count()
        transaction_running_no = "{0:0>6}".format(transaction_length + 1)

        merchant_pwd = 'sm212345'
        encode_request = json.loads(request.body)
        transaction = self.get_object()
        payment_id = current_year + current_month + current_day + transaction_running_no
        encoding_string = (
            'sm212345' 
            + 'SM2'
            + payment_id
            + encode_request['merchantReturnUrl']
            + encode_request['amount'] 
            + encode_request['currencyCode'] 
            + encode_request['custIP'] 
            + encode_request['pageTimeout']
        )

        print(encode_request)
        print(encoding_string)
        
        encoding_string = encoding_string.encode('utf-8')
        encoded_string = hashlib.sha256(encoding_string).hexdigest()
        print(encoded_string)

        encode_request['order_number'] = transaction.id
        encode_request['hash_value'] = encoded_string
        encode_request['payment_id'] = payment_id

        transaction.reference = payment_id
        transaction.save()
        
        return Response(encode_request)


    @action(methods=['PUT'], detail=True)
    def update_payment_status(self, request, *args, **kwargs):
        
        transaction = self.get_object()    
        current_time = datetime.datetime.now(tz=timezone.utc)

        transaction.payment_gateway_update_date = current_time
        transaction.save()

        
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)


    @action(methods=['GET'], detail=False)
    def latest_successful(self, request, *args, **kwargs): 

        user_id = request.GET.get('user', '') 

        delta = datetime.timedelta(days=7)      
        current_time = datetime.datetime.now(tz=timezone.utc)
        date_filter = current_time - delta

        all_latest_successful_transactions = Transaction.objects.filter(
            payment_status='OK',
            payment_gateway_update_date__gte=date_filter,
            cart__cart_status='CM', 
            cart__user_id=user_id,
        ).all()

        serializer = TransactionExtendedSerializer(all_latest_successful_transactions, many=True)
        return Response(serializer.data)


    @action(methods=['GET'], detail=False)
    def ell(self, request, *args, **kwargs):        

        all_t = Transaction.objects.all()

        for tran in all_t:
            tran.delete()

    @action(methods=['GET'], detail=False)
    def report(self, request, *args, **kwargs):        

        all_ok_transactions = Transaction.objects.filter(payment_status='OK').filter()
        serializer = TransactionExtendedSerializer(all_ok_transactions, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def query_request(self, request, *args, **kwargs):
        print('query_request')

    @action(methods=['POST'], detail=False)
    def generate_report_table(self, request, *args, **kwargs):
        table_request = json.loads(request.body)
        report_column = table_request['type']
        report_start_date = table_request['start_date']
        report_end_date = table_request['end_date']

        date_format = '%-d-%m-%Y '
        time_zone = 'Asia/Kuala_Lumpur'

        combined_generated_table = []

        if report_column == 'csv':
            filtered_table = Transaction.objects.filter(
                created_date__range=(report_start_date, report_end_date)
            ).all()

            for transaction_row in filtered_table:
                print('ane cendol', transaction_row)
                transaction_ = Transaction.objects.filter(id=transaction_row.id).first()
                cart_items_ = CartItem.objects.filter(cart=transaction_.cart).all()
                for cart_item_row in cart_items_:
                    if cart_item_row.product and cart_item_row.entity:
                        print('heheheh', cart_item_row.product)
                        product_ = Product.objects.filter(id=cart_item_row.product.id).first()
                        entity_ = Entity.objects.filter(id=cart_item_row.entity.id).first()

                        if entity_.type_of_entity == 'AD':
                            entity_reg_no_ = entity_.audit_firm_number
                        elif entity_.type_of_entity == 'BS':
                            entity_reg_no_ = entity_.registration_number_new + '(' + entity_.registration_number + '-' + entity_.check_digit + ')'
                        elif entity_.type_of_entity == 'CP':
                            entity_reg_no_ = entity_.company_number_new + '(' + entity_.company_number + '-' + entity_.check_digit + ')'

                        new_row = [
                            transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
                            'Online',
                            transaction_.name,
                            transaction_.email_address,
                            transaction_.phone_number,
                            transaction_.address1,
                            transaction_.address2,
                            transaction_.address3,
                            transaction_.postcode,
                            transaction_.city,
                            transaction_.state,
                            product_.description,
                            entity_.name,
                            entity_reg_no_,
                            product_.fee/100,
                            product_.discount,
                            product_.tax,
                            product_.fee/100,
                            transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
                            transaction_.transaction_id,
                            transaction_.transaction_type,
                            transaction_.payment_method,
                            transaction_.card_holder,
                            transaction_.card_no_mask,
                            transaction_.total_amount/100,
                            transaction_.payment_status,
                            transaction_.receipt_no,
                            transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''
                        ]
                        combined_generated_table.append(new_row)

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="xcess_portal_mtt.csv"'

            csv_writer = csv.writer(response)   
            csv_writer.writerow([
                'Date', 
                'Channel', 
                'Customer Name', 
                'Customer Email Address',
                'Customer Phone No.',
                'Customer Address 1',
                'Customer Address 2',
                'Customer Address 3',
                'Customer Postcode',
                'Customer City',
                'Product Type',
                'Product Name',
                'Entity Name',
                'Entity No.',
                'Product Fee',
                'Discount Amount',
                'Tax Amount',
                'Gross Amount',
                'Transaction Date',
                'Payment Transaction ID',
                'Transaction Type',
                'Payment Mode',
                'Card Holder',
                'Card No.',
                'Charge Amount',
                'Transaction Status',
                'Receipt No.',
                'Receipt Date',
                'Ministry Name',
                'Department / Agency Name',
                'Division / Section / Unit Name',
                'Address 1',
                'Address 2',
                'Address 3',
                'Postcode',
                'City',
                'State',
                'KJAKP Email Address',
                'KJAKP IC No.',
                'KJAKP Package',
                'KJAKP HOD Name',
                'KJAKP HOD Position',
                'KJAKP HOD Email',
                'KJAKP Approval Date',
                'KJAKP Expiry Date',
                'KJAKP Quota',
                'KJAKP Total Document',
                'KJAKP Status'
            ])

            for row in combined_generated_table:
                csv_writer.writerow(row)
    
        elif report_column == 'excel':
            filtered_table = Transaction.objects.filter(
                created_date__range=(report_start_date, report_end_date)
            ).all()

            for transaction_row in filtered_table:
                print('ane cendol', transaction_row)
                transaction_ = Transaction.objects.filter(id=transaction_row.id).first()
                cart_items_ = CartItem.objects.filter(cart=transaction_.cart).all()
                for cart_item_row in cart_items_:
                    if cart_item_row.product and cart_item_row.entity:
                        print('heheheh', cart_item_row.product)
                        product_ = Product.objects.filter(id=cart_item_row.product.id).first()
                        entity_ = Entity.objects.filter(id=cart_item_row.entity.id).first()

                        if entity_.type_of_entity == 'AD':
                            entity_reg_no_ = entity_.audit_firm_number
                        elif entity_.type_of_entity == 'BS':
                            entity_reg_no_ = entity_.registration_number_new + '(' + entity_.registration_number + '-' + entity_.check_digit + ')'
                        elif entity_.type_of_entity == 'CP':
                            entity_reg_no_ = entity_.company_number_new + '(' + entity_.company_number + '-' + entity_.check_digit + ')'

                        new_row = [
                            transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
                            'Online',
                            transaction_.name,
                            transaction_.email_address,
                            transaction_.phone_number,
                            transaction_.address1,
                            transaction_.address2,
                            transaction_.address3,
                            transaction_.postcode,
                            transaction_.city,
                            transaction_.state,
                            product_.description,
                            product_.description,
                            entity_.name,
                            entity_reg_no_,
                            product_.fee/100,
                            product_.discount,
                            product_.tax,
                            product_.fee/100,
                            transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
                            transaction_.transaction_id,
                            transaction_.transaction_type,
                            transaction_.total_amount/100,
                            transaction_.payment_status,
                            transaction_.receipt_no,
                            transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            '',
                            ''
                        ]
                        combined_generated_table.append(new_row)

            output = io.BytesIO()
 
            workbook = xlsxwriter.Workbook(output)
            worksheet2 = workbook.add_worksheet('Master Transaction Table')

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="xcess_portal_mtt.csv"'

            data_ = [[
                'Date', 
                'Channel', 
                'Customer Name', 
                'Customer Email Address',
                'Customer Phone No.',
                'Customer Address 1',
                'Customer Address 2',
                'Customer Address 3',
                'Customer Postcode',
                'Customer City',
                'Product Type',
                'Product Name',
                'Entity Name',
                'Entity No.',
                'Product Fee',
                'Discount Amount',
                'Tax Amount',
                'Gross Amount',
                'Payment Transaction ID',
                'Transaction Date',
                'Payment Mode',
                'Charge Amount',
                'Transaction Status',
                'Receipt No.',
                'Receipt Date',
                'Ministry Name',
                'Department / Agency Name',
                'Division / Section / Unit Name',
                'Address 1',
                'Address 2',
                'Address 3',
                'Postcode',
                'City',
                'State',
                'KJAKP Email Address',
                'KJAKP IC No.',
                'KJAKP Package',
                'KJAKP HOD Name',
                'KJAKP HOD Position',
                'KJAKP HOD Email',
                'KJAKP Approval Date',
                'KJAKP Expiry Date',
                'KJAKP Quota',
                'KJAKP Total Document',
                'KJAKP Status'
            ]]

            for row in combined_generated_table:
                data_.append(row)

            for row_num, columns in enumerate(data_):
                for col_num, cell_data in enumerate(columns):
                    worksheet2.write(row_num, col_num, cell_data)
            
            workbook.close()
            output.seek(0)
            file_name = 'xcess_portal_mtt.xlsx'
            response = HttpResponse(
                    output,
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
            response['Content-Disposition'] = 'attachment; filename=%s' % file_name
            # print(response)
        print('generate_report_table')
        return response

    @action(methods=['POST'], detail=False)
    def generate_gaf(self, request, *args, **kwargs):
        print('generate_gaf')
        request_ = json.loads(request.body)
        start_date_ = request_['start_date']
        end_date_ = request_['end_date']

        date_format = '%-d-%m-%Y '
        time_zone = 'Asia/Kuala_Lumpur'

        combined_data_ = []

        s_counter = 0
        transaction_total = 0
        l_counter = 0
        debit_sum = 0
        credit_sum = 0
        balance = 0
        
        filtered_table = Transaction.objects.filter(
            created_date__range=(start_date_, end_date_)
        ).all()

        start_date_new_ = make_aware(datetime.datetime.strptime(start_date_, '%Y-%m-%dT%H:%M:%S.%fZ'))
        end_date_new_ = make_aware(datetime.datetime.strptime(end_date_, '%Y-%m-%dT%H:%M:%S.%fZ'))
        
        combined_data_.append([
            'C',
            'SURUHANJAYA SYARIKAT MALAYSIA',
            '',
            '000640557056',
            start_date_new_.astimezone(pytz.timezone(time_zone)).strftime('%d/%m/%Y'),
            end_date_new_.astimezone(pytz.timezone(time_zone)).strftime('%d/%m/%Y'),
            datetime.datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d/%m/%Y'),
            'XCESS',
            'GAFv1.0.0'
        ])
        index_1 = 1
        for transaction_row in filtered_table:
            # print('ane cendol', transaction_row)
            
            transaction_ = Transaction.objects.filter(id=transaction_row.id).first()
            cart_items_ = CartItem.objects.filter(cart=transaction_.cart).all()
            item_counter = 1
            print('S: ', index_1, 'Transaction ID', transaction_.receipt_no)
            print('Old ', transaction_total/100)
            transaction_total = transaction_total + transaction_.total_amount
            print('New ', transaction_total/100)
            # print('sssss', transaction_.created_date)
            index_1 = index_1 + 1

            for supply_item in cart_items_:
                if supply_item.product and supply_item.entity:
                    # print('heheheh', supply_item.product)
                    product_ = Product.objects.filter(id=supply_item.product.id).first()

                    new_row = [
                        'S', 
                        transaction_.name,
                        transaction_.phone_number,
                        transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d/%m/%Y'),
                        transaction_.receipt_no,
                        item_counter,
                        product_.webservice,
                        product_.fee/100,
                        '0.00',
                        'OS',
                        'MALAYSIA',
                        'MYR',
                        '0.00',
                        '0.00'
                    ]
                    combined_data_.append(new_row)
                    item_counter = item_counter + 1
                    s_counter = s_counter + 1
        
        for transaction_ledger in filtered_table:
            transaction_ = Transaction.objects.filter(id=transaction_ledger.id).first()
            cart_items_ = CartItem.objects.filter(cart=transaction_.cart).all()
            item_counter = 1

            ledger_length = len(cart_items_)
            ledger_index = 0

            for ledger_item in cart_items_:
                if ledger_item.product and ledger_item.entity:
                    # print('heheheh', ledger_item.product)
                    product_ = Product.objects.filter(id=ledger_item.product.id).first()
                    
                    new_row_debit = [
                        'L', 
                        transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d/%m/%Y'),
                        'S-H01-000-000-A16003',
                        'EGHL006',
                        transaction_.reference_no,
                        transaction_.name,
                        transaction_.transaction_id,
                        transaction_.receipt_no,
                        'AR',
                        product_.fee/100,
                        '0.00',
                        '0.00',
                        'OS',
                        '',
                        '',
                        '',
                        ''
                    ]
                    l_counter = l_counter + 1
                    debit_sum = debit_sum + product_.fee
                    combined_data_.append(new_row_debit)

                    new_row_credit = [
                        'L', 
                        transaction_.created_date.astimezone(pytz.timezone(time_zone)).strftime('%d/%m/%Y'),
                        product_.coa_code,
                        'EGHL006',
                        product_.webservice,
                        transaction_.name,
                        transaction_.reference_no,
                        transaction_.receipt_no,
                        'AR',
                        '0.00',
                        product_.fee/100,
                        '0.00',
                        'OS',
                        '',
                        '',
                        '',
                        ''
                    ]
                    l_counter = l_counter + 1
                    credit_sum = credit_sum + product_.fee
                    print('Sum: ', credit_sum, 'Transaction ID', transaction_.receipt_no)
                    combined_data_.append(new_row_credit)
                    
                    item_counter = item_counter + 1
        
        combined_data_.append([
            'F',
            '0',
            '0',
            '0',
            s_counter,
            transaction_total/100,
            '0',
            l_counter,
            debit_sum/100,
            credit_sum/100,
            (debit_sum - credit_sum) / 100
        ])

        timezone_ = pytz.timezone('Asia/Kuala_Lumpur')

        current_year = str(datetime.datetime.now(timezone_).year)
        current_month = str(datetime.datetime.now(timezone_).month)
        current_day = str(datetime.datetime.now(timezone_).day)

        file_name = 'GAF-XCESS-' + current_year + current_month + current_day + '.txt'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="' + file_name +'"'

        csv_writer = csv.writer(response, delimiter='|')   

        for row in combined_data_:
            csv_writer.writerow(row)
        
        return response

class RefundDropdownViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = RefundDropdown.objects.all()
    serializer_class = RefundDropdownSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_fields = ['reference']


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    

    def get_queryset(self):
        queryset = RefundDropdown.objects.all()
        return queryset

# Dari app pass reference to PG : 20201012000001
# PG pass transaction_id: SM00000020201012000001
# Reference ID : P20201012000001
# Receipt ID: PP20201012000001
# Order ID: FOC20201012000001, FOCGOV20201012000001, PD20201012000001, RESP20201012000001, CBID20201012000001, 
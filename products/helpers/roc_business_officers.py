import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware
from .mapping import (
    officer_designation_mapping, 
    state_mapping, 
    charge_code,
    time_mapping,
    comp_status_mapping,
    comp_type_mapping,
    status_of_comp_mapping,
    origin_country_mapping
)

from collections import OrderedDict

def roc_business_officers(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    print('____________   ')
    print('particular_biz_officer: ', data_mdw_1)
    print('____________   ')

    date_format = '%d-%m-%Y'
    time_zone = 'Asia/Kuala_Lumpur'

    business_address_info = mdw_1['rocBusinessAddressInfo']
    business_address_info['stateString'] = state_mapping(business_address_info['state']) 

    registered_address_info = mdw_1['rocRegAddressInfo']
    registered_address_info['stateString'] = state_mapping(registered_address_info['state']) 

    temp_incorp_date_old = data_mdw_1['rocCompanyInfo']['incorpDate']['#text']
    temp_incorp_date_new = time_mapping(temp_incorp_date_old)

    temp_comp_type_old = data_mdw_1['rocCompanyInfo']['companyStatus']
    temp_comp_type_new = comp_status_mapping(temp_comp_type_old, lang)
    
    temp_comp_status_old = data_mdw_1['rocCompanyInfo']['companyType']
    temp_comp_status_new = comp_type_mapping(temp_comp_status_old, lang)

    temp_status_of_comp_old = data_mdw_1['rocCompanyInfo']['statusOfCompany']
    temp_status_of_comp_new = status_of_comp_mapping(temp_status_of_comp_old)
    
    temp_reg_address_1_old = data_mdw_1['rocRegAddressInfo']['address1']
    temp_reg_address_2_old = data_mdw_1['rocRegAddressInfo']['address2']
    temp_reg_address_3_old = data_mdw_1['rocRegAddressInfo']['address3']
    temp_reg_postcode_old = data_mdw_1['rocRegAddressInfo']['postcode']
    temp_reg_town_old = data_mdw_1['rocRegAddressInfo']['town']
    temp_reg_state_old = data_mdw_1['rocRegAddressInfo']['state']

    if temp_reg_address_1_old == 'TIADA FAIL':
        temp_reg_address_1_new = None
    elif temp_reg_address_1_old == None:
        temp_reg_address_1_new = None
    else:
        temp_reg_address_1_new = temp_reg_address_1_old

    if temp_reg_address_2_old == 'TIADA FAIL':
        temp_reg_address_2_new = None
    elif temp_reg_address_2_old == None:
        temp_reg_address_2_new = None
    else:
        temp_reg_address_2_new = temp_reg_address_2_old

    if temp_reg_address_3_old == 'TIADA FAIL':
        temp_reg_address_3_new = None
    elif temp_reg_address_3_old == None:
        temp_reg_address_3_new = None
    else:
        temp_reg_address_3_new = temp_reg_address_3_old

    if temp_reg_state_old == 'TIADA FAIL':
        temp_reg_state_new = None
    elif temp_reg_state_old == None:
        temp_reg_state_new = None
    else:
        temp_reg_state_new = state_mapping(temp_reg_state_old)

    if temp_reg_postcode_old == 'TIADA FAIL':
        temp_reg_postcode_new = None
    elif temp_reg_postcode_old == None:
        temp_reg_postcode_new = None
    else:
        temp_reg_postcode_new = temp_reg_postcode_old

    if temp_reg_town_old == 'TIADA FAIL':
        temp_reg_town_new = None
    elif temp_reg_town_old == None:
        temp_reg_town_new = None
    else:
        temp_reg_town_new = temp_reg_town_old
    
    temp_comp_origin_old = data_mdw_1['rocCompanyInfo']['companyCountry']
    temp_comp_origin_new = origin_country_mapping(temp_comp_origin_old)
    
    temp_biz_address_1_old = data_mdw_1['rocBusinessAddressInfo']['address1']
    temp_biz_address_2_old = data_mdw_1['rocBusinessAddressInfo']['address2']
    temp_biz_address_3_old = data_mdw_1['rocBusinessAddressInfo']['address3']
    temp_biz_postcode_old = data_mdw_1['rocBusinessAddressInfo']['postcode']
    temp_biz_town_old = data_mdw_1['rocBusinessAddressInfo']['town']
    temp_biz_state_old = data_mdw_1['rocBusinessAddressInfo']['state']

    if temp_biz_address_1_old == 'TIADA FAIL':
        temp_biz_address_1_new = None
    elif temp_biz_address_1_old == None:
        temp_biz_address_1_new = None
    else:
        temp_biz_address_1_new = temp_biz_address_1_old

    if temp_biz_address_2_old == 'TIADA FAIL':
        temp_biz_address_2_new = None
    elif temp_biz_address_2_old == None:
        temp_biz_address_2_new = None
    else:
        temp_biz_address_2_new = temp_biz_address_2_old

    if temp_biz_address_3_old == 'TIADA FAIL':
        temp_biz_address_3_new = None
    elif temp_biz_address_3_old == None:
        temp_biz_address_3_new = None
    else:
        temp_biz_address_3_new = temp_biz_address_3_old

    if temp_biz_state_old == 'TIADA FAIL':
        temp_biz_state_new = None
    elif temp_biz_state_old == None:
        temp_biz_state_new = None
    else:
        temp_biz_state_new = state_mapping(temp_biz_state_old)
    
    if temp_biz_postcode_old == 'TIADA FAIL':
        temp_biz_postcode_new = None
    elif temp_biz_postcode_old == None:
        temp_biz_postcode_new = None
    else:
        temp_biz_postcode_new = temp_biz_postcode_old

    if temp_biz_town_old == 'TIADA FAIL':
        temp_biz_town_new = None
    elif temp_biz_town_old == None:
        temp_biz_town_new = None
    else:
        temp_biz_town_new = temp_biz_town_old

    # Start current officers
    temp_current_officers = data_mdw_1['rocCompanyOfficerListInfo']['rocCompanyOfficerInfos']['rocCompanyOfficerInfos']
    temp_current_officers.sort(key = lambda x:x['startDate']['#text'], reverse=True) 
    temp_current_officers_arr = []

    # print('item',temp_current_officers)
    # print('instance',isinstance(temp_current_officers, list))
    if isinstance(temp_current_officers, list):
        for officer in temp_current_officers:
        
            if officer['idType'] == 'MK':

                nric_1 = officer['idNo'][0:6]
                nric_2 = officer['idNo'][6:8]
                nric_3 = officer['idNo'][8:]
                nric = nric_1 + '-' + nric_2 + '-' + nric_3
            else:
                nric = officer['idNo']        
            officer['idNo'] = nric
            officer['state'] = state_mapping(officer['state'])
            officer['designationCode'] = officer_designation_mapping(officer['designationCode'])
            # print('sadasdsad', officer)
            if officer['startDate']['#text']:
                officer['startDate'] = make_aware(datetime.strptime(officer['startDate']['#text'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_current_officers_arr.append(officer)

    else:
        if officer['idType'] == 'MK':
            nric_1 = officer['idNo'][0:6]
            nric_2 = officer['idNo'][6:8]
            nric_3 = officer['idNo'][8:]
            nric = nric_1 + '-' + nric_2 + '-' + nric_3
        else:
            nric = officer['idNo']    

        officer['idNo'] = nric
        officer['state'] = state_mapping(officer['state'])
        officer['designationCode'] = officer_designation_mapping(officer['designationCode'])
        # print('sadasdsad', officer)
        officer['startDate'] = make_aware(datetime.strptime(officer['startDate']['#text'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)

    if 'rocChangeCompanyOfficerListInfo' in data_mdw_1:
        if 'rocCompanyOfficerChgsInfos' in data_mdw_1['rocChangeCompanyOfficerListInfo']:
            if data_mdw_1['rocChangeCompanyOfficerListInfo']['rocCompanyOfficerChgsInfos']:
                temp_previous_officers = data_mdw_1['rocChangeCompanyOfficerListInfo']['rocCompanyOfficerChgsInfos']['rocCompanyOfficerChgsInfos']
                # print('0------------')
                # print('hehehe', temp_previous_officers)
                temp_previous_officers.sort(key = lambda x:('#text' in x['resignDate'], x['resignDate'].get('#text')), reverse=True) 
                temp_previous_officers_arr = []
                temp_previous_officers_arr_inside = []
            else:
                temp_previous_officers = []
                temp_previous_officers_arr = []
    else:
        temp_previous_officers = []
        temp_previous_officers_arr = []


    for officer in temp_previous_officers:
        if officer['idType'] == 'MK':

            nric_1 = officer['idNo'][0:6]
            nric_2 = officer['idNo'][6:8]
            nric_3 = officer['idNo'][8:]
            nric = nric_1 + '-' + nric_2 + '-' + nric_3
        else:
            nric = officer['idNo']        
        officer['idNo'] = nric
        officer['state'] = state_mapping(officer['state'])
        officer['designationCode'] = officer_designation_mapping(officer['designationCode'])
        officer['startDate'] = make_aware(datetime.strptime(officer['startDate']['#text'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)
        
        if '@xsi:nil' in officer['resignDate']:
            officer['resignDate'] = None
        else:
            officer['resignDate'] = make_aware(datetime.strptime(officer['resignDate']['#text'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)

        if '@xsi:nil' in officer['removalDate']:
            officer['removalDate'] = None
        else:
            officer['removalDate'] = make_aware(datetime.strptime(officer['removalDate']['#text'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)
        
        temp_previous_officers_arr.append(officer)


    company_info = mdw_1['rocCompanyInfo']

    if 'dateOfChange' in data_mdw_1['rocCompanyInfo'].keys():
        if '#text' in data_mdw_1['rocCompanyInfo']['dateOfChange'].keys():
            date_of_change = make_aware(datetime.strptime(data_mdw_1['rocCompanyInfo']['dateOfChange']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))
            date_of_change_str = date_of_change.astimezone(pytz.timezone(time_zone)).strftime(date_format)
        else:
            date_of_change_str = 'NIL'
    else:
        date_of_change_str = 'NIL'

    
    if 'lastUpdateDate' in company_info.keys():
        if '#text' in company_info['lastUpdateDate'].keys():
            company_info['lastUpdateDate'] = make_aware(datetime.strptime(company_info['lastUpdateDate']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))
            company_info['lastUpdateDate'] = company_info['lastUpdateDate'].astimezone(pytz.timezone(time_zone)).strftime(date_format)
        else:
            company_info['lastUpdateDate'] = 'NIL'
    else:
        company_info['lastUpdateDate'] = 'NIL'    

    data_ready = {
        'mdw1': data_mdw_1,
        'mdw2': data_mdw_2,
        'corpInfo': {
            'compName': data_mdw_1['rocCompanyInfo']['companyName'],
            'compOldName': data_mdw_1['rocCompanyInfo']['companyOldName'],
            #'changeDate': temp_change_date_new,
            'checkDigit': data_mdw_1['rocCompanyInfo']['checkDigit'],
            'companyType': temp_comp_type_new,
            'companyStatus': temp_comp_status_new,        
            'statusOfCompany': temp_status_of_comp_new,
            'reg_address1': temp_reg_address_1_new,
            'reg_address2': temp_reg_address_2_new,
            'reg_address3': temp_reg_address_3_new,
            'reg_state': temp_reg_state_new,
            'reg_town': temp_reg_town_new,
            'reg_postcode': temp_reg_postcode_new,
            'reg_origin': temp_comp_origin_new,
            'biz_address1': temp_biz_address_1_new,
            'biz_address2': temp_biz_address_2_new,
            'biz_address3': temp_biz_address_3_new,
            'biz_state': temp_biz_state_new,
            'biz_town': temp_biz_town_new,
            'biz_postcode': temp_biz_postcode_new,            
            'biz_nature': data_mdw_1['rocCompanyInfo']['businessDescription']
        },
        'current': temp_current_officers_arr,
        'previous': temp_previous_officers_arr,
        'company_info': company_info,
        'date_of_change': date_of_change_str,
        'compNoNew': data_mdw_2['newFormatNo'],
        'compNoOld': data_mdw_2['oldFormatNo'],   
        'incorp_date': temp_incorp_date_new,
        'business_address_info': business_address_info,
        'registered_address_info': registered_address_info,
        'latest_update_date': time_mapping(data_mdw_1['rocCompanyInfo']['latestDocUpdateDate']['#text']),
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y'), 
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S')
    }

    return data_ready
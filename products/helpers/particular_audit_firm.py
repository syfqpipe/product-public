import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import (
    state_mapping,
    origin_country_mapping
)

def particular_audit_firm(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    print('____________   ')
    print('particular_audit_firm: ', data_mdw_1)
    print('____________   ')

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'

    temp_firm_address_1 = data_mdw_1['adtFirmProf']['prinAddr1']
    temp_firm_address_2 = data_mdw_1['adtFirmProf']['prinAddr2']
    temp_firm_address_3 = data_mdw_1['adtFirmProf']['prinAddr3']
    temp_firm_postcode = data_mdw_1['adtFirmProf']['prinPostcode']
    temp_firm_town = data_mdw_1['adtFirmProf']['prinTown']
    temp_firm_state = data_mdw_1['adtFirmProf']['prinState']
    temp_firm_country = data_mdw_1['adtFirmProf']['prinCountry']

    temp_firm_commence_date = data_mdw_1['adtFirmProf']['commenceDt']
    temp_firm_commence_date = make_aware(datetime.strptime(temp_firm_commence_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_firm_commence_date = temp_firm_commence_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    temp_firm_reg_date = data_mdw_1['adtFirmProf']['regDt']
    temp_firm_reg_date = make_aware(datetime.strptime(temp_firm_reg_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_firm_reg_date = temp_firm_reg_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    if temp_firm_address_1 == 'TIADA FAIL':
        temp_firm_address_1 = None
    elif temp_firm_address_1 == None:
        temp_firm_address_1 = None
    else:
        temp_firm_address_1 = temp_firm_address_1

    if temp_firm_address_2 == 'TIADA FAIL':
        temp_firm_address_2 = None
    elif temp_firm_address_2 == None:
        temp_firm_address_2 = None
    else:
        temp_firm_address_2 = temp_firm_address_2

    if temp_firm_address_3 == 'TIADA FAIL':
        temp_firm_address_3 = None
    elif temp_firm_address_3 == None:
        temp_firm_address_3 = None
    else:
        temp_firm_address_3 = temp_firm_address_3
    
    if temp_firm_postcode == 'TIADA FAIL':
        temp_firm_postcode = None
    elif temp_firm_postcode == None:
        temp_firm_postcode = None
    else:
        temp_firm_postcode = temp_firm_postcode

    if temp_firm_town == 'TIADA FAIL':
        temp_firm_town = None
    elif temp_firm_town == None:
        temp_firm_town = None
    else:
        temp_firm_town = temp_firm_town

    if temp_firm_state == 'TIADA FAIL':
        temp_firm_state = None
    elif temp_firm_state == None:
        temp_firm_state = None
    else:
        temp_firm_state = state_mapping(temp_firm_state)

    if temp_firm_country == 'TIADA FAIL':
        temp_firm_country = None
    elif temp_firm_country == None:
        temp_firm_country = None
    else:
        temp_firm_country = state_mapping(temp_firm_country)
    
    temp_branches = []

    if data_mdw_1['branchOffices']:
        if isinstance(data_mdw_1['branchOffices']['branchOffices'], list):
            temp_branch_list = data_mdw_1['branchOffices']['branchOffices']

            for temp_branch in temp_branch_list:
                temp_branch_state = state_mapping(temp_branch['branchState'])
                temp_branch_country = origin_country_mapping(temp_branch['branchCountry'])
                
                temp_branches.append({
                    'tel_no': temp_branch['branchTelNo'],
                    'address_1': temp_branch['branchAddr1'],
                    'address_2': temp_branch['branchAddr2'],
                    'address_3': temp_branch['branchAddr3'],
                    'postcode': temp_branch['branchPostcode'],
                    'town': temp_branch['branchTown'],
                    'country': temp_branch_country,
                    'state': temp_branch_state
                })
        else:
            temp_branch_state = state_mapping(temp_branch['branchState'])
            temp_branch_country = origin_country_mapping(temp_branch['branchCountry'])
            
            temp_branches.append({
                'tel_no': temp_branch['branchTelNo'],
                'address_1': temp_branch['branchAddr1'],
                'address_2': temp_branch['branchAddr2'],
                'address_3': temp_branch['branchAddr3'],
                'postcode': temp_branch['branchPostcode'],
                'town': temp_branch['branchTown'],
                'country': temp_branch_country,
                'state': temp_branch_state
            })
    else:
        temp_branches = None

    temp_current_partners = []

    if data_mdw_1['adtPartners']:
        if isinstance(data_mdw_1['adtPartners']['adtPartners'], list):
            temp_partners_list = data_mdw_1['adtPartners']['adtPartners']

            for temp_partner in temp_partners_list:
                temp_partner_state = state_mapping(temp_partner['resState'])
                temp_partner_country = origin_country_mapping(temp_partner['resCountry'])
                print('   ')
                print ('>>>> ', temp_partner)
                print('   ')
                if 'entryDt' in temp_partner.keys():
                    temp_partner_entry_date = make_aware(datetime.strptime(temp_partner['entryDt'], '%Y-%m-%dT%H:%M:%S.000Z'))
                    temp_partner_entry_date = temp_partner_entry_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
                else: 
                    temp_partner_entry_date = None

                if 'resignDt' in temp_partner.keys():
                    temp_partner_resign_date = make_aware(datetime.strptime(temp_partner['entryDt'], '%Y-%m-%dT%H:%M:%S.000Z'))
                    temp_partner_resign_date = temp_partner_resign_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
                else: 
                    temp_partner_resign_date = None

                temp_current_partners.append({
                    'name': temp_partner['adtName'],
                    'ic_no_new': temp_partner['adtNewIcNo'],
                    'ic_no_old': temp_partner['adtOldIcNo'],
                    'passport_no': temp_partner['adtPassportNo'],
                    'license_no': temp_partner['licenceNo'],
                    'partner_status': temp_partner['partnerStatus'],
                    'address_1': temp_partner['resAddr1'],
                    'address_2': temp_partner['resAddr2'],
                    'address_3': temp_partner['resAddr3'],
                    'postcode': temp_partner['resPostcode'],
                    'town': temp_partner['resTown'],
                    'country': temp_partner_country,
                    'state': temp_partner_state,
                    'entry_date': temp_partner_entry_date,
                    'resign_date': temp_partner_resign_date
                })
        else:
            temp_partner_state = state_mapping(temp_partner['resState'])
            temp_partner_country = origin_country_mapping(temp_partner['resCountry'])
            
            if temp_partner['entryDt']:
                temp_partner_entry_date = make_aware(datetime.strptime(temp_partner['entryDt'], '%Y-%m-%dT%H:%M:%S.000Z'))
                temp_partner_entry_date = temp_partner_entry_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
            else: 
                temp_partner_entry_date = None

            if temp_partner['resignDt']:
                temp_partner_resign_date = make_aware(datetime.strptime(temp_partner['entryDt'], '%Y-%m-%dT%H:%M:%S.000Z'))
                temp_partner_resign_date = temp_partner_resign_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
            else: 
                temp_partner_resign_date = None

            temp_current_partners.append({
                'name': temp_partner['adtName'],
                'ic_no_new': temp_partner['adtNewIcNo'],
                'ic_no_old': temp_partner['adtOldIcNo'],
                'passport_no': temp_partner['adtPassportNo'],
                'license_no': temp_partner['licenceNo'],
                'partner_status': temp_partner['partnerStatus'],
                'address_1': temp_partner['resAddr1'],
                'address_2': temp_partner['resAddr2'],
                'address_3': temp_partner['resAddr3'],
                'postcode': temp_partner['resPostcode'],
                'town': temp_partner['resTown'],
                'country': temp_partner_country,
                'state': temp_partner_state,
                'entry_date': temp_partner_entry_date,
                'resign_date': temp_partner_resign_date
            })
    else:
        temp_current_partners = None

    data_ready = {
        'audit_firm_info': {
            'firm_name': data_mdw_1['adtFirmProf']['adtFirmName'],
            'firm_no': data_mdw_1['adtFirmProf']['adtFirmNo'],
            'commence_date': temp_firm_commence_date,
            'registration_date': temp_firm_reg_date,
            'address_1': temp_firm_address_1,
            'address_2': temp_firm_address_2,
            'address_3': temp_firm_address_3,
            'postcode': temp_firm_postcode,
            'town': temp_firm_town,
            'state': temp_firm_state,
            'country': temp_firm_country,
            'tel_no': data_mdw_1['adtFirmProf']['telNo'],
            'fax_no': data_mdw_1['adtFirmProf']['faxNo']
        },
        'branch_info': temp_branches,
        'partner_info': temp_current_partners,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y"), 
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %-H:%M:%S")
    }

    # print(data_ready)

    return data_ready
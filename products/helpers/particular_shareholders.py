import string
import pytz
import json
import subprocess

from datetime import datetime
from django.utils.timezone import make_aware
from products.services.get_new_format_entity import get_new_format_entity

from .mapping import (
    comp_status_mapping,
    time_mapping,
    comp_type_mapping,
    status_of_comp_mapping,
    state_mapping,
    origin_country_mapping
)

def particular_shareholders(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'

    tz = pytz.timezone('Asia/Kuala_Lumpur')
    now = datetime.now(tz=tz) 
    now_string = now.strftime('%Y-%m-%d %H:%M:%S')

    print('____________   ')
    print('particular_shareholder: ', data_mdw_1)
    print('____________   ')

    url_info = 'http://integrasistg.ssm.com.my/InfoService/1'
    auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode('utf-8').rstrip('\n')
    headers = {
        'content-type': 'text/xml;charset=UTF-8',
        'authorization': auth_code
    }

    temp_comp_status = comp_status_mapping(data_mdw_1['rocCompanyInfo']['companyStatus'], lang)
    temp_comp_type = comp_type_mapping(data_mdw_1['rocCompanyInfo']['companyType'], lang)
    temp_status_of_comp = status_of_comp_mapping(data_mdw_1['rocCompanyInfo']['statusOfCompany'])

    if 'incorpDate' in data_mdw_1['rocCompanyInfo']:
        temp_incorp_date = time_mapping(data_mdw_1['rocCompanyInfo']['incorpDate'])
    else: 
        temp_incorp_date = None

    if 'lastUpdateDate' in data_mdw_1['rocCompanyInfo']:
        temp_last_update_date = time_mapping(data_mdw_1['rocCompanyInfo']['lastUpdateDate'])
    else: 
        temp_last_update_date = None
    
    if 'dateOfChange' in data_mdw_1['rocCompanyInfo']:
        temp_change_date = time_mapping(data_mdw_1['rocCompanyInfo']['dateOfChange'])
    else: 
        temp_change_date = None
    
    if data_mdw_1['rocCompanyInfo']['localforeignCompany'] == 'L':
        if data_mdw_1['rocCompanyInfo']['companyStatus'] == 'U':
            if data_mdw_1['rocCompanyInfo']['companyType'] == 'G' or data_mdw_1['rocCompanyInfo']['companyType'] == 'U':
                shareholders = []
            else:
                shareholders = data_mdw_1['currShareholderList']['shareholders']['shareholders']
                shareholders_changes = data_mdw_1['rocShareholderChgListInfo']['rocShareholderCghInfos']['rocShareholderCghInfos']   
        else:
            shareholders = data_mdw_1['currShareholderList']['shareholders']['shareholders']
            shareholders_changes = data_mdw_1['rocShareholderChgListInfo']['rocShareholderCghInfos']['rocShareholderCghInfos']
        
        shareholders_data = []
        shareholder_changes_data = []

        if isinstance(shareholders, list):
            
            for shareholder in shareholders:
                if shareholder['idType'] == 'MK':
                    nric_1 = shareholder['idNo'][0:6]
                    nric_2 = shareholder['idNo'][6:8]
                    nric_3 = shareholder['idNo'][8:]
                    nric = nric_1 + '-' + nric_2 + '-' + nric_3
                    company_no = None
                elif shareholder['idType'] == 'C' or shareholder['idType'] == 'F':
                    # print('----------')
                    # print(shareholder['idType'])
                    # print(shareholder['idNo'])
                    # print('----------')
                    nric = shareholder['idNo']
                    company_no__ = get_new_format_entity(url_info, headers, shareholder['idNo'][:-2], 'ROC')

                    if company_no__['errorMsg']:
                        company_no = ''
                    else:
                        company_no = company_no__['newFormatNo']
                else:
                    # print('----------')
                    # print(shareholders['idType'])
                    # print('----------')
                    nric = shareholder['idNo']
                    company_no = None

                address1 = shareholder['address']['address1']
                address2 = shareholder['address']['address2']
                address3 = shareholder['address']['address3']
                postcode = shareholder['address']['postcode']
                town = shareholder['address']['town']
                state = state_mapping(shareholder['address']['state'])

                if '#text' in shareholder['totalShare']:
                    share = float(shareholder['totalShare']['#text'])
                else:
                    share = None

                shareholders_data.append({
                    'name': shareholder['name'],
                    'id': nric,
                    'companyNo': company_no,
                    'idType': shareholder['idType'],
                    'share': share,
                    'address1': address1,
                    'address2': address2,
                    'address3': address3,
                    'postcode': postcode,
                    'town': town,
                    'state': state
                })
        else: 
            if shareholders['idType'] == 'MK':

                nric_1 = shareholders['idNo'][0:6]
                nric_2 = shareholders['idNo'][6:8]
                nric_3 = shareholders['idNo'][8:]
                nric = nric_1 + '-' + nric_2 + '-' + nric_3
                company_no = None
            elif shareholders['idType'] == 'C' or shareholders['idType'] == 'F':
                # print('----------')
                # print(shareholders['idType'])
                # print(shareholders['idNo'])
                # print('----------')
                nric = shareholders['idNo']
                company_no__ = get_new_format_entity(url_info, headers, shareholders['idNo'][:-2], 'ROC')

                if company_no__['errorMsg']:
                    company_no = ''
                else:
                    company_no = company_no__['newFormatNo']
            else:
                # print('----------')
                # print(shareholders['idType'])
                # print('----------')
                nric = shareholders['idNo']
                company_no = None
            
            address1 = shareholder['address']['address1']
            address2 = shareholder['address']['address2']
            address3 = shareholder['address']['address3']
            postcode = shareholder['address']['postcode']
            town = shareholder['address']['town']
            state = state_mapping(shareholder['address']['state'])

            if '#text' in shareholder['totalShare']:
                share = float(shareholder['totalShare']['#text'])
            else:
                share = None

            shareholders_data.append({
                'name': shareholder['name'],
                'id': nric,
                'companyNo': company_no,
                'idType': shareholder['idType'],
                'share': share,
                'address1': address1,
                'address2': address2,
                'address3': address3,
                'postcode': postcode,
                'town': town,
                'state': state
            })

        act_year_enacted = datetime(year=2017,month=1, day=31).astimezone(pytz.timezone(time_zone))

        if isinstance(shareholders_changes, list):
            shareholders_changes.sort(key = lambda x:('#text' in x['dtTransfer'], x['dtTransfer'].get('#text')), reverse=True) 

            for changes in shareholders_changes:
                transfer_date = make_aware(datetime.strptime(changes['dtTransfer']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))

                current_change_list = []

                if transfer_date >= act_year_enacted:
                    if len(shareholder_changes_data) < 11 and len(shareholder_changes_data) == 0:

                        for current in shareholders_changes:
                            current_transfer_date = make_aware(datetime.strptime(current['dtTransfer']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))

                            # print('TD', transfer_date)
                            # print('CD', current_transfer_date)
                            if current_transfer_date == transfer_date:
                                # print('ADA TAKK')
                                if current['idType'] == 'MK':
                                    shareholder_id_1 = current['shareholderId'][0:6]
                                    shareholder_id_2 = current['shareholderId'][6:8]
                                    shareholder_id_3 = current['shareholderId'][8:]
                                    shareholder_id = shareholder_id_1 + '-' + shareholder_id_2 + '-' + shareholder_id_3
                                else:
                                    shareholder_id = current['shareholderId']

                                address1 = current['address']['address1']
                                address2 = current['address']['address2']
                                address3 = current['address']['address3']
                                postcode = current['address']['postcode']
                                town = current['address']['town']
                                state = state_mapping(current['address']['state'])

                                if '#text' in current['dtTransfer']:
                                    change_date = time_mapping(current['dtTransfer']['#text'])
                                else:
                                    change_date = None
                                
                                current_change_list.append({
                                    'name': current['shareholderName'],
                                    'id': shareholder_id,
                                    'idType': shareholder['idType'],
                                    'share_in': float(current['shareIn']),
                                    'share_out': float(current['shareOut']),
                                    'share_total': float(current['totalShare']),
                                    'address1': address1,
                                    'address2': address2,
                                    'address3': address3,
                                    'postcode': postcode,
                                    'town': town,
                                    'state': state,
                                    'change_date': change_date
                                })

                        shareholder_changes_data.append({
                            'change_date': time_mapping(changes['dtTransfer']['#text']),
                            'shareholding': current_change_list
                        })
                    elif len(shareholder_changes_data) < 11 and len(shareholder_changes_data) != 0:
                        print('CURRENT INDEX', len(shareholder_changes_data))
                        date_check = False
                        print('CD', time_mapping(changes['dtTransfer']['#text']))
                        for list_ in shareholder_changes_data:
                            print('LD', list_['change_date'])
                            
                            if list_['change_date'] == time_mapping(changes['dtTransfer']['#text']):
                                print('DAPAT')
                                date_check = True
                            else:
                                pass

                        if date_check is False:
                            for current in shareholders_changes:
                                current_transfer_date = make_aware(datetime.strptime(current['dtTransfer']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))
                                
                                # print('TD', transfer_date)
                                # print('CD', current_transfer_date)
                                if current_transfer_date == transfer_date:
                                    # print('ADA TAKK')
                                    if current['idType'] == 'MK':
                                        shareholder_id_1 = current['shareholderId'][0:6]
                                        shareholder_id_2 = current['shareholderId'][6:8]
                                        shareholder_id_3 = current['shareholderId'][8:]
                                        shareholder_id = shareholder_id_1 + '-' + shareholder_id_2 + '-' + shareholder_id_3
                                    else:
                                        shareholder_id = current['shareholderId']

                                    address1 = current['address']['address1']
                                    address2 = current['address']['address2']
                                    address3 = current['address']['address3']
                                    postcode = current['address']['postcode']
                                    town = current['address']['town']
                                    state = state_mapping(current['address']['state'])

                                    if '#text' in current['dtTransfer']:
                                        change_date = time_mapping(current['dtTransfer']['#text'])
                                    else:
                                        change_date = None
                                    
                                    current_change_list.append({
                                        'name': current['shareholderName'],
                                        'id': shareholder_id,
                                        'idType': shareholder['idType'],
                                        'share_in': float(current['shareIn']),
                                        'share_out': float(current['shareOut']),
                                        'share_total': float(current['totalShare']),
                                        'address1': address1,
                                        'address2': address2,
                                        'address3': address3,
                                        'postcode': postcode,
                                        'town': town,
                                        'state': state,
                                        'change_date': change_date
                                    })

                            shareholder_changes_data.append({
                                'change_date': time_mapping(changes['dtTransfer']['#text']),
                                'shareholding': current_change_list
                            })
        else:
            transfer_date = make_aware(datetime.strptime(shareholders_changes['dtTransfer']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))

            if transfer_date >= act_year_enacted:
                if shareholders_changes['idType'] == 'MK':
                    shareholder_id_1 = shareholders_changes['shareholderId'][0:6]
                    shareholder_id_2 = shareholders_changes['shareholderId'][6:8]
                    shareholder_id_3 = shareholders_changes['shareholderId'][8:]
                    shareholder_id = shareholder_id_1 + '-' + shareholder_id_2 + '-' + shareholder_id_3
                else:
                    shareholder_id = shareholders_changes['shareholderId']

                address1 = shareholders_changes['address']['address1']
                address2 = shareholders_changes['address']['address2']
                address3 = shareholders_changes['address']['address3']
                postcode = shareholders_changes['address']['postcode']
                town = shareholders_changes['address']['town']
                state = state_mapping(shareholders_changes['address']['state'])
                
                if '#text' in shareholder_changes_data['dtTransfer']:
                    change_date = time_mapping(shareholder_changes_data['dtTransfer']['#text'])
                else:
                    change_date = None

                shareholder_changes_data.append({
                    'name': changes['shareholderName'],
                    'id': shareholder_id,
                    'idType': shareholder['idType'],
                    'share_in': float(shareholders_changes['shareIn']),
                    'share_out': float(shareholders_changes['shareOut']),
                    'share_total': float(shareholders_changes['totalShare']),
                    'address1': address1,
                    'address2': address2,
                    'address3': address3,
                    'postcode': postcode,
                    'town': town,
                    'state': state,
                    'change_date': change_date
                })

    else:
        shareholders_data = []
        shareholder_changes_data = []

    data_ready = {
        'mdw1': data_mdw_1,
        'mdw2': data_mdw_2,
        'company_info': {
            'name': data_mdw_1['rocCompanyInfo']['companyName'],
            'old_name': data_mdw_1['rocCompanyInfo']['companyOldName'],
            'change_date': temp_change_date,
            'registration_no': data_mdw_2['newFormatNo'] + ' (' + data_mdw_2['oldFormatNo'] + ')',
            'incorp_date': temp_incorp_date,
            'company_type': temp_comp_type,
            'company_status': temp_comp_status,
            'status_of_company': temp_status_of_comp,
            'address1': data_mdw_1['rocRegAddressInfo']['address1'],
            'address2': data_mdw_1['rocRegAddressInfo']['address2'],
            'address3': data_mdw_1['rocRegAddressInfo']['address3'],
            'postcode': data_mdw_1['rocRegAddressInfo']['postcode'],
            'town': data_mdw_1['rocRegAddressInfo']['town'],
            'state': state_mapping(data_mdw_1['rocRegAddressInfo']['state']),
            'origin': origin_country_mapping(data_mdw_1['rocCompanyInfo']['companyCountry'])
        },
        'business_info': {
            'address1': data_mdw_1['rocBusinessAddressInfo']['address1'],
            'address2': data_mdw_1['rocBusinessAddressInfo']['address2'],
            'address3': data_mdw_1['rocBusinessAddressInfo']['address3'],
            'postcode': data_mdw_1['rocBusinessAddressInfo']['postcode'],
            'town': data_mdw_1['rocBusinessAddressInfo']['town'],
            'state': state_mapping(data_mdw_1['rocBusinessAddressInfo']['state']),
            'description': data_mdw_1['rocCompanyInfo']['businessDescription']
        },
        'latest': shareholders_data,
        'changes': shareholder_changes_data,
        'latest_update_date': temp_last_update_date,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y"), 
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %-H:%M:%S")
    }

    # print(data_ready)

    return data_ready
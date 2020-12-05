import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import (
    state_mapping,
    nationality_code,
    status_biz_mapping
)

def biz_profile(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'
    # print(mdw_1)

    print('_____________')
    print('biz_profile:   ', data_mdw_1)
    print('_____________')

    temp_main_address_1 = data_mdw_1['robBusinessInfo']['mainAddress1']
    temp_main_address_2 = data_mdw_1['robBusinessInfo']['mainAddress2']
    temp_main_address_3 = data_mdw_1['robBusinessInfo']['mainAddress3']
    temp_main_postcode = data_mdw_1['robBusinessInfo']['mainPostcode']
    temp_main_town = data_mdw_1['robBusinessInfo']['mainTown']
    temp_main_state = data_mdw_1['robBusinessInfo']['mainState']

    # print('status', data_mdw_1['robBusinessInfo']['status'])
    if data_mdw_1['robBusinessInfo']['status'] == 'B':
        temp_llp_name = data_mdw_1['robBusinessInfo']['llpName']
        temp_llp_no = data_mdw_1['robBusinessInfo']['llpNo']
        temp_llp_date_long = make_aware(datetime.strptime(data_mdw_1['robBusinessInfo']['llpconvertDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
        temp_llp_date = temp_llp_date_long.astimezone(pytz.timezone(time_zone)).strftime(date_format)
    else:
        temp_llp_name = None
        temp_llp_no = None
        temp_llp_date = None
    
    temp_llp_info = {
        'llpName': temp_llp_name,
        'llpNo': temp_llp_no,
        'llpDate': temp_llp_date
    }

    if temp_main_address_1 == 'TIADA FAIL':
        temp_main_address_1 = None
    elif temp_main_address_1 == None:
        temp_main_address_1 = None
    else:
        temp_main_address_1 = temp_main_address_1

    if temp_main_address_2 == 'TIADA FAIL':
        temp_main_address_2 = None
    elif temp_main_address_2 == None:
        temp_main_address_2 = None
    else:
        temp_main_address_2 = temp_main_address_2

    if temp_main_address_3 == 'TIADA FAIL':
        temp_main_address_3 = None
    elif temp_main_address_3 == None:
        temp_main_address_3 = None
    else:
        temp_main_address_3 = temp_main_address_3
    
    if temp_main_postcode == 'TIADA FAIL':
        temp_main_postcode = None
    elif temp_main_postcode == None:
        temp_main_postcode = None
    else:
        temp_main_postcode = temp_main_postcode

    if temp_main_town == 'TIADA FAIL':
        temp_main_town = None
    elif temp_main_town == None:
        temp_main_town = None
    else:
        temp_main_town = temp_main_town

    if temp_main_state == 'TIADA FAIL':
        temp_main_state = None
    elif temp_main_state == None:
        temp_main_state = None
    else:
        temp_main_state = state_mapping(temp_main_state)

    if int(data_mdw_1['robBusinessInfo']['ownerCount']) == 1 and lang == 'ms':
        temp_biz_ownership  = 'PEMILIKAN TUNGGAL'
    elif int(data_mdw_1['robBusinessInfo']['ownerCount']) > 1 and lang == 'ms':
        temp_biz_ownership  = 'PERKONGSIAN'
    elif int(data_mdw_1['robBusinessInfo']['ownerCount']) == 1 and lang == 'en':
        temp_biz_ownership  = 'SOLE PROPRIETORSHIP'
    elif int(data_mdw_1['robBusinessInfo']['ownerCount']) > 1 and lang == 'en':
        temp_biz_ownership  = 'PARTNERSHIP'

    temp_biz_start_date = data_mdw_1['robBusinessInfo']['startBusinessDate']
    temp_biz_start_date = make_aware(datetime.strptime(temp_biz_start_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_biz_start_date = temp_biz_start_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
    temp_reg_date = data_mdw_1['robBusinessInfo']['registrationDate']
    temp_reg_date = make_aware(datetime.strptime(temp_reg_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_reg_date = temp_reg_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
    temp_end_biz_date = data_mdw_1['robBusinessInfo']['endBusinessDate']
    temp_end_biz_date = make_aware(datetime.strptime(temp_end_biz_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_end_biz_date = temp_end_biz_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    if 'ammendmentDate' in data_mdw_1['robBusinessInfo']:
        temp_ammend_date = data_mdw_1['robBusinessInfo']['ammendmentDate']
        temp_ammend_date = make_aware(datetime.strptime(temp_ammend_date, '%Y-%m-%dT%H:%M:%S.000Z'))
        temp_ammend_date = temp_ammend_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
    else:
        temp_ammend_date = None

    temp_status = status_biz_mapping(data_mdw_1['robBusinessInfo']['status'], lang)
    
    temp_current_owner = []

    if isinstance(data_mdw_1['robOwnershipListInfo']['robOwnerShipInfos']['robOwnerShipInfos'], list):
        _list_ = data_mdw_1['robOwnershipListInfo']['robOwnerShipInfos']['robOwnerShipInfos']
    else: 
        _list_ = []
        _list_.append(data_mdw_1['robOwnershipListInfo']['robOwnerShipInfos']['robOwnerShipInfos'])

    for owner in _list_:
        # print(owner)
        if owner['status'] == 'A':
            temp_current_owner_address_1 = owner['address1']
            temp_current_owner_address_2 = owner['address2']
            temp_current_owner_address_3 = owner['address3']
            temp_current_owner_postcode = owner['postcode']
            temp_current_owner_town = owner['town']
            temp_current_owner_state = owner['state']

            if temp_current_owner_address_1 == 'TIADA FAIL':
                temp_current_owner_address_1 = None
            elif temp_current_owner_address_1 == None:
                temp_current_owner_address_1 = None
            else:
                temp_current_owner_address_1 = temp_current_owner_address_1

            if temp_current_owner_address_2 == 'TIADA FAIL':
                temp_current_owner_address_2 = None
            elif temp_current_owner_address_2 == None:
                temp_current_owner_address_2 = None
            else:
                temp_current_owner_address_2 = temp_current_owner_address_2

            if temp_current_owner_address_3 == 'TIADA FAIL':
                temp_current_owner_address_3 = None
            elif temp_current_owner_address_3 == None:
                temp_current_owner_address_3 = None
            else:
                temp_current_owner_address_3 = temp_current_owner_address_3
            
            if temp_current_owner_postcode == 'TIADA FAIL':
                temp_current_owner_postcode = None
            elif temp_current_owner_postcode == None:
                temp_current_owner_postcode = None
            else:
                temp_current_owner_postcode = temp_current_owner_postcode

            if temp_current_owner_town == 'TIADA FAIL':
                temp_current_owner_town = None
            elif temp_current_owner_town == None:
                temp_current_owner_town = None
            else:
                temp_current_owner_town = temp_current_owner_town

            if temp_current_owner_state == 'TIADA FAIL':
                temp_current_owner_state = None
            elif temp_current_owner_state == None:
                temp_current_owner_state = None
            else:
                temp_current_owner_state = state_mapping(temp_current_owner_state)

            
            
            temp_new_ic_no = owner['newIcNo']

            temp_race = owner['race']

            if temp_race == 'M':
                temp_race = 'MELAYU'
            elif temp_race == 'C':
                temp_race = 'CINA'
            elif temp_race == 'I':
                temp_race = 'INDIA'
            elif temp_race == 'R':
                temp_race = 'PERSENDIRIAN (SDN BHD)'
            elif temp_race == 'U':
                temp_race = 'UMUM (SYKT AWAM)'
            elif temp_race == 'F':
                temp_race = 'FOREIGNER'
            elif temp_race == 'S':
                temp_race = 'PERNIAGAAN'
            elif temp_race == 'A':
                temp_race = 'PERBADANAN'
            elif temp_race == 'K':
                temp_race = 'KADAZAN'
            elif temp_race == 'D':
                temp_race = 'DUSUN'
            elif temp_race == 'J':
                temp_race = 'BAJAU'
            elif temp_race == 'Y':
                temp_race = 'BIDAYUH'
            elif temp_race == 'T':
                temp_race = 'IBAN'
            elif temp_race == 'E':
                temp_race = 'MELANAU'
            elif temp_race == 'O':
                temp_race = 'LAIN-LAIN BANGSA'
            elif temp_race == 'N':
                temp_race = 'NATIVE'
            elif temp_race == 'B':
                temp_race = 'BUMIPUTERA SABAH'
            elif temp_race == 'W':
                temp_race = 'BUMIPUTERA SARAWAK'
            
            temp_nationality = owner['nationality']
            temp_nationality = nationality_code(temp_nationality, lang)

            temp_gender = owner['gender']

            if temp_gender == 'L' and lang == 'en':
                temp_gender = 'MALE'
            elif temp_gender == 'P' and lang == 'en':
                temp_gender = 'FEMALE'
            elif temp_gender == 'L' and lang == 'ms':
                temp_gender = 'LELAKI'
            elif temp_gender == 'P' and lang == 'ms':
                temp_gender = 'PEREMPUAN'
            else:
                temp_gender = None

            temp_birth_date = owner['dob']
            temp_birth_date = make_aware(datetime.strptime(temp_birth_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_birth_date = temp_birth_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_entry_date = owner['entryDate']
            temp_entry_date = make_aware(datetime.strptime(temp_entry_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_entry_date = temp_entry_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
            last_update_date = owner['updateDate']
            last_update_date = make_aware(datetime.strptime(last_update_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            last_update_date = last_update_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
            
            temp_current_owner.append({
                'name': owner['ownerName'],
                'address_1': temp_current_owner_address_1,
                'address_2': temp_current_owner_address_2,
                'address_3': temp_current_owner_address_3,
                'postcode': temp_current_owner_postcode,
                'town': temp_current_owner_town,
                'state': temp_current_owner_state,
                'bizName': owner['address1'],
                'bizRegNoOld': owner['address1'],
                'bizRegNoNew': owner['address1'],
                'checkDigit': owner['address1'],
                'name': owner['ownerName'],
                'icNoNew': temp_new_ic_no,
                'icNoOld': owner['idCardNumber'],
                'race': temp_race,
                'gender': temp_gender,
                'nationality': temp_nationality,
                'birthDate': temp_birth_date,
                'entryDate': temp_entry_date
            })
        
    temp_previous_owner = []

    for owner in _list_:
        # print('stat', owner['status'])
        # print ('  ')
        # print(owner)
        # print('   ')
        if owner['status'] == 'T':
            temp_previous_owner_address_1 = owner['address1']
            temp_previous_owner_address_2 = owner['address2']
            temp_previous_owner_address_3 = owner['address3']
            temp_previous_owner_postcode = owner['postcode']
            temp_previous_owner_town = owner['town']
            temp_previous_owner_state = owner['state']

            if temp_previous_owner_address_1 == 'TIADA FAIL':
                temp_previous_owner_address_1 = None
            elif temp_previous_owner_address_1 == None:
                temp_previous_owner_address_1 = None
            else:
                temp_previous_owner_address_1 = temp_previous_owner_address_1

            if temp_previous_owner_address_2 == 'TIADA FAIL':
                temp_previous_owner_address_2 = None
            elif temp_previous_owner_address_2 == None:
                temp_previous_owner_address_2 = None
            else:
                temp_previous_owner_address_2 = temp_previous_owner_address_2

            if temp_previous_owner_address_3 == 'TIADA FAIL':
                temp_previous_owner_address_3 = None
            elif temp_previous_owner_address_3 == None:
                temp_previous_owner_address_3 = None
            else:
                temp_previous_owner_address_3 = temp_previous_owner_address_3
            
            if temp_previous_owner_postcode == 'TIADA FAIL':
                temp_previous_owner_postcode = None
            elif temp_previous_owner_postcode == None:
                temp_previous_owner_postcode = None
            else:
                temp_previous_owner_postcode = temp_previous_owner_postcode

            if temp_previous_owner_town == 'TIADA FAIL':
                temp_previous_owner_town = None
            elif temp_previous_owner_town == None:
                temp_previous_owner_town = None
            else:
                temp_previous_owner_town = temp_previous_owner_town

            if temp_previous_owner_state == 'TIADA FAIL':
                temp_previous_owner_state = None
            elif temp_previous_owner_state == None:
                temp_previous_owner_state = None
            else:
                temp_previous_owner_state = state_mapping(temp_previous_owner_state)
            
            temp_new_ic_no = owner['newIcNo']

            temp_race = owner['race']

            if temp_race == 'M':
                temp_race = 'MELAYU'
            elif temp_race == 'C':
                temp_race = 'CINA'
            elif temp_race == 'I':
                temp_race = 'INDIA'
            elif temp_race == 'R':
                temp_race = 'PERSENDIRIAN (SDN BHD)'
            elif temp_race == 'U':
                temp_race = 'UMUM (SYKT AWAM)'
            elif temp_race == 'F':
                temp_race = 'FOREIGNER'
            elif temp_race == 'S':
                temp_race = 'PERNIAGAAN'
            elif temp_race == 'A':
                temp_race = 'PERBADANAN'
            elif temp_race == 'K':
                temp_race = 'KADAZAN'
            elif temp_race == 'D':
                temp_race = 'DUSUN'
            elif temp_race == 'J':
                temp_race = 'BAJAU'
            elif temp_race == 'Y':
                temp_race = 'BIDAYUH'
            elif temp_race == 'T':
                temp_race = 'IBAN'
            elif temp_race == 'E':
                temp_race = 'MELANAU'
            elif temp_race == 'O':
                temp_race = 'LAIN-LAIN BANGSA'
            elif temp_race == 'N':
                temp_race = 'NATIVE'
            elif temp_race == 'B':
                temp_race = 'BUMIPUTERA SABAH'
            elif temp_race == 'W':
                temp_race = 'BUMIPUTERA SARAWAK'
            
            temp_nationality = owner['nationality']

            temp_nationality = nationality_code(temp_nationality, lang)

            temp_gender = owner['gender']
            # print('gender', temp_gender)
            if temp_gender == 'L' and lang == 'en':
                temp_gender = 'MALE'
            elif temp_gender == 'P' and lang == 'en':
                temp_gender = 'FEMALE'
            elif temp_gender == 'L' and lang == 'ms':
                temp_gender = 'LELAKI'
            elif temp_gender == 'P' and lang == 'ms':
                temp_gender = 'PEREMPUAN'
            else:
                temp_gender = None

            temp_birth_date = owner['dob']
            temp_birth_date = make_aware(datetime.strptime(temp_birth_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_birth_date = temp_birth_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_entry_date = owner['entryDate']
            # print('edate', temp_entry_date)
            temp_entry_date = make_aware(datetime.strptime(temp_entry_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_entry_date = temp_entry_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_withdraw_date = owner['updateDate']
            # print('wdate', temp_withdraw_date)
            temp_withdraw_date = make_aware(datetime.strptime(temp_withdraw_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_withdraw_date = temp_withdraw_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
            # print('wdate', temp_withdraw_date)

            temp_ammend_type = owner['ammendmentType']

            if temp_ammend_type == 'B' and lang == 'en':
                temp_ammend_type = 'NEW OWNER'
            elif temp_ammend_type == 'D' and lang == 'en':
                temp_ammend_type = 'PULL-OUT'
            elif temp_ammend_type == 'M' and lang == 'en':
                temp_ammend_type = 'DECEASED'
            elif temp_ammend_type == 'A' and lang == 'en':
                temp_ammend_type = 'ADDRESS UPDATE'
            elif temp_ammend_type == 'P' and lang == 'en':
                temp_ammend_type = 'OWNERSHIP CHANGES'
            elif temp_ammend_type == 'K' and lang == 'en':
                temp_ammend_type = 'ID CARD NUMBER CHANGES'
            elif temp_ammend_type == 'N' and lang == 'en':
                temp_ammend_type = 'OWNER NAME CHANGES'
            elif temp_ammend_type == 'S' and lang == 'en':
                temp_ammend_type = 'PARTNERSHIP DISSOLVE'
            elif temp_ammend_type == 'O' and lang == 'en':
                temp_ammend_type = 'COURT ORDER'
            elif temp_ammend_type == 'B' and lang == 'ms':
                temp_ammend_type = 'PEMILIK BARU'
            elif temp_ammend_type == 'D' and lang == 'ms':
                temp_ammend_type = 'TARIK DIRI'
            elif temp_ammend_type == 'M' and lang == 'ms':
                temp_ammend_type = 'KEMATIAN'
            elif temp_ammend_type == 'A' and lang == 'ms':
                temp_ammend_type = 'PERUBAHAN ALAMAT'
            elif temp_ammend_type == 'P' and lang == 'ms':
                temp_ammend_type = 'PERUBAHAN NAMA PEMILIK'
            elif temp_ammend_type == 'K' and lang == 'ms':
                temp_ammend_type = 'PERUBAHAN NO KP'
            elif temp_ammend_type == 'N' and lang == 'ms':
                temp_ammend_type = 'PERUBAHAN NAMA PEMILIK'
            elif temp_ammend_type == 'S' and lang == 'ms':
                temp_ammend_type = 'PEMBUBARAN PERKONGSIAN'
            elif temp_ammend_type == 'O' and lang == 'ms':
                temp_ammend_type = 'PERINTAH MAHKAMAH'
                        
            temp_previous_owner.append({
                'address_1': temp_previous_owner_address_1,
                'address_2': temp_previous_owner_address_2,
                'address_3': temp_previous_owner_address_3,
                'postcode': temp_previous_owner_postcode,
                'town': temp_previous_owner_town,
                'state': temp_previous_owner_state,
                'bizName': owner['address1'],
                'bizRegNoOld': owner['address1'],
                'bizRegNoNew': owner['address1'],
                'checkDigit': owner['address1'],
                'name': owner['ownerName'],
                'icNoNew': temp_new_ic_no,
                'icNoOld': owner['idCardNumber'],
                'race': temp_race,
                'gender': temp_gender,
                'nationality': temp_nationality,
                'birthDate': temp_birth_date,
                'entryDate': temp_entry_date,
                'withdrawDate': temp_withdraw_date,
                'ammendmentType': temp_ammend_type
            })
    
    # if len(temp_previous_owner) == 0:
    #     temp_previous_owner = None

    # print ('argggggg', len(temp_previous_owner))
    temp_branches = []

    if data_mdw_1['robBranchListInfo']['errorMsg']:
        temp_branches = []
    else:
        if isinstance(data_mdw_1['robBranchListInfo']['robBranchInfos']['robBranchInfos'], list):
            temp_branch_list = data_mdw_1['robBranchListInfo']['robBranchInfos']['robBranchInfos']
            for temp_branch in temp_branch_list:
                temp_branch['state'] = state_mapping(temp_branch['state'])
                temp_branch['status'] = status_biz_mapping(temp_branch['status'], lang)
                temp_branches.append(temp_branch)
        else:
            temp_branch = data_mdw_1['robBranchListInfo']['robBranchInfos']['robBranchInfos']
            temp_branch['state'] = state_mapping(temp_branch['state'])
            temp_branch['status'] = status_biz_mapping(temp_branch['status'], lang)
            temp_branches.append(temp_branch)

    data_ready = {
        'bizInfo': {
            'registrationName': data_mdw_1['robBusinessInfo']['registrationName'],
            'registrationNo': data_mdw_2['newFormatNo'] + ' (' + data_mdw_2['oldFormatNo'] + ')',
            'address_1': temp_main_address_1,
            'address_2': temp_main_address_2,
            'address_3': temp_main_address_3,
            'postcode': temp_main_postcode,
            'town': temp_main_town,
            'state': temp_main_state,
            'bizOwnership': temp_biz_ownership,
            'bizStartDate': temp_biz_start_date,
            'regDate': temp_reg_date,
            'endBusinessDate': temp_end_biz_date,
            'ammendmentDate': temp_ammend_date,
            'status': temp_status,
        },
        'bizType': {
            'description': data_mdw_1['robBusinessInfo']['description']
        },
        'branchInfo': temp_branches,
        'llpInfo': temp_llp_info,
        'ownerCurrentInfo': temp_current_owner,
        'ownerPreviousInfo': temp_previous_owner,
        'last_update_date': last_update_date,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y"),
        'generated_date': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %-H:%M:%S")
    }

    # print(data_ready)

    return data_ready
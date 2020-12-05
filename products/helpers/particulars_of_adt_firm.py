import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import (
    state_mapping,
    race_mapping,
    nationality_code,
    gender_mapping,
    time_mapping,
    business_ownership_mapping,
    status_biz_mapping,
    ammend_type_mapping
)

def particulars_of_adt_firm(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = '%d-%m-%Y'
    time_zone = 'Asia/Kuala_Lumpur'

    temp_main_address_1 = data_mdw_1['robBusinessInfo']['mainAddress1']
    temp_main_address_2 = data_mdw_1['robBusinessInfo']['mainAddress2']
    temp_main_address_3 = data_mdw_1['robBusinessInfo']['mainAddress3']
    temp_main_postcode = data_mdw_1['robBusinessInfo']['mainPostcode']
    temp_main_town = data_mdw_1['robBusinessInfo']['mainTown']
    temp_main_state = data_mdw_1['robBusinessInfo']['mainState']

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

    temp_biz_ownership = business_ownership_mapping(int(data_mdw_1['robBusinessInfo']['ownerCount']), lang)

    temp_biz_start_date = time_mapping(data_mdw_1['robBusinessInfo']['startBusinessDate'])
    temp_reg_date = time_mapping(data_mdw_1['robBusinessInfo']['registrationDate'])
    temp_end_biz_date = time_mapping(data_mdw_1['robBusinessInfo']['endBusinessDate'])
    temp_ammend_date = time_mapping(data_mdw_1['robBusinessInfo']['ammendmentDate'])

    temp_status = data_mdw_1['robBusinessInfo']['status']
    temp_status = status_biz_mapping(temp_status, lang)
    
    temp_current_owner = []

    for owner in data_mdw_1['robOwnershipListInfo']['robOwnerShipInfos']['robOwnerShipInfos']:
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

            temp_race = race_mapping(temp_race, lang)
            
            temp_nationality = owner['nationality']


            if temp_nationality:
                temp_nationality = nationality_code(temp_nationality, lang)
            else:
                temp_nationality = None

            temp_gender = owner['gender']
            if temp_gender:
                temp_gender = gender_mapping(temp_gender, lang)
            else:
                temp_gender = None

            temp_birth_date = owner['dob']
            temp_birth_date = make_aware(datetime.strptime(temp_birth_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_birth_date = temp_birth_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_entry_date = owner['entryDate']
            temp_entry_date = make_aware(datetime.strptime(temp_entry_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_entry_date = temp_entry_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
            
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

    for owner in data_mdw_1['robOwnershipListInfo']['robOwnerShipInfos']['robOwnerShipInfos']:
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
                temp_previous_owner_state = state_mapping(temp_previous_owner_state, lang)

            temp_new_ic_no = owner['newIcNo']

            temp_race = race_mapping(owner['race'])
            
            temp_nationality = owner['nationality']

            if temp_nationality:
                temp_nationality = nationality_code(temp_nationality, lang)
            else:
                temp_nationality = None

            temp_gender = owner['gender']
            if temp_gender:
                temp_gender = gender_mapping(temp_gender, lang)
            else:
                temp_gender = None

            temp_birth_date = owner['dob']
            temp_birth_date = make_aware(datetime.strptime(temp_birth_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_birth_date = temp_birth_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_entry_date = owner['entryDate']
            temp_entry_date = make_aware(datetime.strptime(temp_entry_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_entry_date = temp_entry_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_withdraw_date = owner['updateDate']
            temp_withdraw_date = make_aware(datetime.strptime(temp_withdraw_date, '%Y-%m-%dT%H:%M:%S.000Z'))
            temp_withdraw_date = temp_withdraw_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            temp_ammend_type = owner['ammendmentType']
            temp_ammend_type = ammend_type_mapping(temp_ammend_type, lang)
                        
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
        'branchInfo': {

        },
        'ownerCurrentInfo': temp_current_owner,
        'ownerPreviousInfo': temp_previous_owner
    }

    print(data_ready)

    return data_ready
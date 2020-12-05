import string
import pytz
import json
import locale

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import (
    state_mapping,
    month_mapping,
    time_mapping_aware,
    time_mapping_string
)

def acgs(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    # print(data_mdw_1['compName'])

    date_format = '%d %B %Y'
    time_zone = 'Asia/Kuala_Lumpur'

    temp_comp_status_old = data_mdw_1['compStatus']
    
    if temp_comp_status_old == 'E':
        temp_comp_status_new = 'Existing'
    elif temp_comp_status_old == 'W':
        temp_comp_status_new = 'Winding Up'
    elif temp_comp_status_old == 'D':
        temp_comp_status_new = 'Dissolved'

    print('_____________')
    print('acgs:   ', mdw_1)
    print('_____________')

    incorp_date = data_mdw_1['incorpDate']
    incorp_date = time_mapping_aware(incorp_date)
    incorp_date_str = time_mapping_string(incorp_date)
    incorp_month = month_mapping(incorp_date.month, lang)

    latest_doc_date = data_mdw_1['latest_doc_date']
    latest_doc_date = time_mapping_aware(latest_doc_date)
    latest_doc_date_str = time_mapping_string(latest_doc_date)
    latest_doc_month = month_mapping(latest_doc_date.month, lang)

    temp_regAddress_address_1_old = data_mdw_1['regAddress']['address1']
    temp_regAddress_address_2_old = data_mdw_1['regAddress']['address2']
    temp_regAddress_address_3_old = data_mdw_1['regAddress']['address3']
    temp_regAddress_postcode_old = data_mdw_1['regAddress']['postcode']
    temp_regAddress_town_old = data_mdw_1['regAddress']['town']
    temp_regAddress_state_old = data_mdw_1['regAddress']['state']

    if temp_regAddress_address_1_old == 'TIADA FAIL':
        temp_regAddress_address_1_new = None
    elif temp_regAddress_address_1_old == None:
        temp_regAddress_address_1_new = None
    else:
        temp_regAddress_address_1_new = string.capwords(temp_regAddress_address_1_old)

    if temp_regAddress_address_2_old == 'TIADA FAIL':
        temp_regAddress_address_2_new = None
    elif temp_regAddress_address_2_old == None:
        temp_regAddress_address_2_new = None
    else:
        temp_regAddress_address_2_new = string.capwords(temp_regAddress_address_2_old)

    if temp_regAddress_address_3_old == 'TIADA FAIL':
        temp_regAddress_address_3_new = None
    elif temp_regAddress_address_3_old == None:
        temp_regAddress_address_3_new = None
    else:
        temp_regAddress_address_3_new = string.capwords(temp_regAddress_address_3_old)

    if temp_regAddress_postcode_old == 'TIADA FAIL':
        temp_regAddress_postcode_new = None
    elif temp_regAddress_postcode_old == None:
        temp_regAddress_postcode_new = None
    else:
        temp_regAddress_postcode_new = temp_regAddress_postcode_old

    if temp_regAddress_town_old == 'TIADA FAIL':
        temp_regAddress_town_new = None
    elif temp_regAddress_town_old == None:
        temp_regAddress_town_new = None
    else:
        temp_regAddress_town_new = string.capwords(temp_regAddress_town_old)

    if temp_regAddress_state_old == 'TIADA FAIL':
        temp_regAddress_state_new = None
    elif temp_regAddress_state_old == None:
        temp_regAddress_state_new = None
    else:
        temp_regAddress_state_new = state_mapping(temp_regAddress_state_old)

    data_ready = {
        'compName': data_mdw_1['compName'],
        'compNo': data_mdw_1['compNo'],
        'compStatus': data_mdw_1['compStatus'],
        'compNoNew': data_mdw_2['newFormatNo'],
        'compNoOld': data_mdw_2['oldFormatNo'],
        'compType': data_mdw_1['compType'],
        'isAuditedFs': data_mdw_1['isAuditedFs'],
        'isBlacklist': data_mdw_1['isBlacklist'],
        'isDirNoOutsCompound': data_mdw_1['isDirNoOutsCompound'],
        'isDirNoPerseCase': data_mdw_1['isDirNoPerseCase'],
        'isDormant': data_mdw_1['isDormant'],
        'isExemptComp': data_mdw_1['isExemptComp'],
        'isIncorp18Months': data_mdw_1['isIncorp18Months'],
        'isLatestArLodged': data_mdw_1['isLatestArLodged'],
        'isRegAddrExist': data_mdw_1['isRegAddrExist'],
        'incorpDate': incorp_date_str,
        'incorporate_day': incorp_date.day,
        'incorporate_month': incorp_month,
        'incorporate_year': incorp_date.year,
        'regAddress_address1': temp_regAddress_address_1_new.title(),
        'regAddress_address2': temp_regAddress_address_2_new,
        'regAddress_address3': temp_regAddress_address_3_new,
        'regAddress_postcode': temp_regAddress_postcode_new,
        'regAddress_state': temp_regAddress_state_new.title(),
        'regAddress_town': temp_regAddress_town_new,
        'extract_date': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d %B %Y'),
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y'),
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S'),
        'latestDocDate': latest_doc_date_str,
        'latest_doc_day': latest_doc_date.day,
        'latest_doc_month': latest_doc_month,
        'latest_doc_year': latest_doc_date.year
    }

    return data_ready
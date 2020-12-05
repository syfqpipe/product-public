import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import state_mapping, origin_country_mapping

def info_acgs(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    # print(data_mdw_1['compName'])

    print('_____________')
    print('info_acgs:   ', data_mdw_1)
    print('_____________')

    date_format = "%d %B %Y"
    time_zone = 'Asia/Kuala_Lumpur'

    temp_comp_status_old = data_mdw_1['compStatus']
    
    if temp_comp_status_old == 'E':
        temp_comp_status_new = 'Existing'
    elif temp_comp_status_old == 'W':
        temp_comp_status_new = 'Winding Up'
    elif temp_comp_status_old == 'D':
        temp_comp_status_new = 'Dissolved'

    temp_incorpDate_old = make_aware(datetime.strptime(data_mdw_1['incorpDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_incorpDate_new = temp_incorpDate_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

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
        'ci_': data_mdw_1['compName'],
        'compNo': data_mdw_1['compNo'],
        'compStatus': data_mdw_1['compStatus'],
        'compNoNew': data_mdw_2['newFormatNo'],
        'compNoOld': data_mdw_2['oldFormatNo'],
        'isAuditedFs': data_mdw_1['isAuditedFs'],
        'isBlacklist': data_mdw_1['isBlacklist'],
        'isDirNoOutsCompound': data_mdw_1['isDirNoOutsCompound'],
        'isDirNoPerseCase': data_mdw_1['isDirNoPerseCase'],
        'isDormant': data_mdw_1['isDormant'],
        'isExemptComp': data_mdw_1['isExemptComp'],
        'isIncorp18Months': data_mdw_1['isIncorp18Months'],
        'isLatestArLodged': data_mdw_1['isLatestArLodged'],
        'isRegAddrExist': data_mdw_1['isRegAddrExist'],
        'incorpDate': temp_incorpDate_new,
        'regAddress_address1': temp_regAddress_address_1_new.title(),
        'regAddress_address2': temp_regAddress_address_2_new,
        'regAddress_address3': temp_regAddress_address_3_new,
        'regAddress_postcode': temp_regAddress_postcode_new,
        'regAddress_state': temp_regAddress_state_new,
        'regAddress_town': temp_regAddress_town_new,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y")
    }

    return data_ready
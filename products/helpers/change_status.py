import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from products.helpers.mapping import (
    comp_status_conversion_mapping,
    comp_type_mapping, 
    comp_status_mapping, 
    branch_code,
    month_mapping
)


def change_status(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = '%-d-%m-%Y'
    time_zone = 'Asia/Kuala_Lumpur'

    print('_____________')
    print('change_status:   ', data_mdw_1)
    print('_____________')

    incorp_date = data_mdw_1['incorpDate']
    incorp_date = make_aware(datetime.strptime(incorp_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    incorp_date_str = incorp_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    incorp_month = month_mapping(incorp_date.month, lang)

    change_status_date = data_mdw_1['dateOfChange']
    change_status_date = make_aware(datetime.strptime(change_status_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    change_status_date_str = change_status_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)   

    change_status_month = month_mapping(change_status_date.month, lang)                     

    branch_name = branch_code(mdw_1['branchCode'])

    act_year_enacted = datetime(year=2017,month=1, day=31).astimezone(pytz.timezone(time_zone))
    
    if incorp_date < act_year_enacted:
        act_year = '1965'
    else:
        act_year = '2016'    

    data_ready = {
        'mdw1': mdw_1,
        'mdw2': mdw_2,
        'companyStatus': comp_status_conversion_mapping(mdw_1['companyStatus'],lang),
        'companyType': comp_type_mapping(mdw_1['companyType'],lang),
        'incorpDate': incorp_date_str,
        'incorporate_day': incorp_date.day,
        'incorporate_month': incorp_month,
        'incorporate_year': incorp_date.year,
        'change_status_date': change_status_date_str,
        'change_status_day': change_status_date.day,
        'change_status_month': change_status_month,
        'change_status_year': change_status.year,        
        'branch_name': branch_name,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %H:%M:%S'),
        'act_year': act_year
    }
    return data_ready
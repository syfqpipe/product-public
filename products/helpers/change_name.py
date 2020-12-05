import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from products.helpers.mapping import (
    comp_type_mapping, 
    comp_status_mapping, 
    comp_status_conversion_mapping, 
    branch_code
)

def change_name(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = "%-d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'

    print('_______')
    print('change_name:     ', mdw_1)
    print('_______')

    incorp_date = data_mdw_1['incorpDate']
    incorp_date = make_aware(datetime.strptime(incorp_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    incorp_date = incorp_date.astimezone(pytz.timezone(time_zone))
    incorp_date_str = incorp_date.strftime(date_format)
    
    

    if lang == 'ms':
        if incorp_date.month == 1:
            incorp_month = "Januari"
        elif incorp_date.month == 2:
            incorp_month = "Februari"
        elif incorp_date.month == 3:
            incorp_month = "Mac"            
        elif incorp_date.month == 4:
            incorp_month = "April"            
        elif incorp_date.month == 5:
            incorp_month = "Mei"            
        elif incorp_date.month == 6:
            incorp_month = "Jun"            
        elif incorp_date.month == 7:
            incorp_month = "Julai"            
        elif incorp_date.month == 8:
            incorp_month = "Ogos"            
        elif incorp_date.month == 9:
            incorp_month = "September"            
        elif incorp_date.month == 10:
            incorp_month = "Oktober"            
        elif incorp_date.month == 11:
            incorp_month = "November"            
        elif incorp_date.month == 12:
            incorp_month = "Disember"  
    else:
        if incorp_date.month == 1:
            incorp_month = "January"
        elif incorp_date.month == 2:
            incorp_month = "February"
        elif incorp_date.month == 3:
            incorp_month = "March"            
        elif incorp_date.month == 4:
            incorp_month = "April"            
        elif incorp_date.month == 5:
            incorp_month = "May"            
        elif incorp_date.month == 6:
            incorp_month = "June"            
        elif incorp_date.month == 7:
            incorp_month = "July"            
        elif incorp_date.month == 8:
            incorp_month = "August"            
        elif incorp_date.month == 9:
            incorp_month = "September"            
        elif incorp_date.month == 10:
            incorp_month = "October"            
        elif incorp_date.month == 11:
            incorp_month = "November"            
        elif incorp_date.month == 12:
            incorp_month = "December"      

    change_date = data_mdw_1['dateOfChange']
    change_date = make_aware(datetime.strptime(change_date, '%Y-%m-%dT%H:%M:%S.000Z'))
    change_date = change_date.astimezone(pytz.timezone(time_zone))
    change_date_str = change_date.strftime(date_format)   

    if lang == 'ms':
        if change_date.month == 1:
            change_month = "Januari"
        elif change_date.month == 2:
            change_month = "Februari"
        elif change_date.month == 3:
            change_month = "Mac"            
        elif change_date.month == 4:
            change_month = "April"            
        elif change_date.month == 5:
            change_month = "Mei"            
        elif change_date.month == 6:
            change_month = "Jun"            
        elif change_date.month == 7:
            change_month = "Julai"            
        elif change_date.month == 8:
            change_month = "Ogos"            
        elif change_date.month == 9:
            change_month = "September"            
        elif change_date.month == 10:
            change_month = "Oktober"            
        elif change_date.month == 11:
            change_month = "November"            
        elif change_date.month == 12:
            change_month = "Disember"  
    else:
        if change_date.month == 1:
            change_month = "January"
        elif change_date.month == 2:
            change_month = "February"
        elif change_date.month == 3:
            change_month = "March"            
        elif change_date.month == 4:
            change_month = "April"            
        elif change_date.month == 5:
            change_month = "May"            
        elif change_date.month == 6:
            change_month = "June"            
        elif change_date.month == 7:
            change_month = "July"            
        elif change_date.month == 8:
            change_month = "August"            
        elif change_date.month == 9:
            change_month = "September"            
        elif change_date.month == 10:
            change_month = "October"            
        elif change_date.month == 11:
            change_month = "November"            
        elif change_date.month == 12:
            change_month = "December"                       

    branch = branch_code(mdw_1['branchCode'])

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
        'change_date': change_date_str,
        'change_day': change_date.day,
        'change_month': change_month,
        'change_year': change_date.year,        
        'branch': branch,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %H:%M:%S"),
        'act_year': act_year
    }

    return data_ready
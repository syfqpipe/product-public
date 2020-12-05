import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import charge_type

def company_charges(mdw_1, mdw_2, mdw_3, lang, entity_type):
    

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'

    charges = mdw_1["SSMRegistrationChargesInfos"]["SSMRegistrationChargesInfos"]
    charges_list = []

    print('_____________')
    print('charges:   ', charges)
    print('_____________')

    # print(mdw_2)
    company_info = mdw_3["rocCompanyInfo"]

    if 'latestDocUpdateDate' in company_info.keys():
        company_info['latestDocUpdateDate'] = make_aware(datetime.strptime(company_info['latestDocUpdateDate'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)
    else:
         company_info['latestDocUpdateDate'] = None

    if isinstance(charges, list): 
        charges = charges
    else:
        charges = [charges]
                

    for charge in charges:
        
        if charge['chargeStatus'] == 'S':
            charge['chargeStatusString'] = 'FULLY SATISFIED'
        elif charge['chargeStatus'] == 'P':
            charge['chargeStatusString'] = 'PARTLY SATISFIED'
        elif charge['chargeStatus'] == 'R':
            charge['chargeStatusString'] = 'FULLY RELEASED'  
        elif charge['chargeStatus'] == 'Q':
            charge['chargeStatusString'] = 'PARTLY RELEASED'     
        elif charge['chargeStatus'] == 'U':
            charge['chargeStatusString'] = 'UNSATISFIED'
        elif charge['chargeStatus'] == 'B':
            charge['chargeStatusString'] = 'CANCELLATION'  
        elif charge['chargeStatus'] == 'C':
            charge['chargeStatusString'] = 'FULLY CEASED' 

        if charge['chargeMortgageType'] == 'O':
            charge['chargeMortgageTypeString'] = 'OPEN TYPE'
        elif charge['chargeMortgageType'] == 'F':
            charge['chargeMortgageTypeString'] = 'FOREIGN CURRENCY' 
        elif charge['chargeMortgageType'] == 'A':
            charge['chargeMortgageTypeString'] = 'AMOUNT'                
        elif charge['chargeMortgageType'] == 'M':
            charge['chargeMortgageTypeString'] = 'MULTIPLE CURRENCIES'   
        
        charge['chargeTypeString'] = charge_type(charge['chargeType'])

        # print(charge['chargeAmount'])
        if 'chargeAmount' in charge and charge['chargeAmount'] != None:
            charge['chargeAmount'] = float(charge['chargeAmount'])
            charge['chargeCreateDateString'] = make_aware(datetime.strptime(charge['chargeCreateDate'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)
        else:
            date_of_change_str = 'NIL'
        
        if 'releaseDate' in charge:
            charge['releaseDateString'] = make_aware(datetime.strptime(charge['releaseDate'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)
                      
        charges_list.append(charge)

        if 'form40Date' in charge:
            charge['form40DateString'] = make_aware(datetime.strptime(charge['form40Date'], '%Y-%m-%dT%H:%M:%S.000Z')).astimezone(pytz.timezone(time_zone)).strftime(date_format)

    data_ready = {
        'mdw1': mdw_1,
        'mdw2': mdw_2,
        'company_info': company_info,
        'charges_list': charges_list,
        'compNoNew': mdw_2['newFormatNo'],
        'compNoOld': mdw_2['oldFormatNo'], 
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %-H:%M:%S"),     
    }


    return data_ready
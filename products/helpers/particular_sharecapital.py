import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import (
    officer_designation_mapping, 
    state_mapping, 
    charge_code,
    comp_status_mapping,
    status_of_comp_mapping,
    time_mapping,
    origin_country_mapping,
    comp_type_mapping,
    time_mapping_aware
)

def particular_sharecapital(mdw_1, mdw_2, lang, entity_type):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = '%d-%m-%Y'
    time_zone = 'Asia/Kuala_Lumpur'

    print('____________   ')
    print('particular_sharecapital: ', data_mdw_1)
    print('____________   ')

    business_address_info = mdw_1['rocBusinessAddressInfo']
    registered_address_info = mdw_1['rocRegAddressInfo']
    share_capital_info = mdw_1['shareCapitalSummary']
    company_info = mdw_1['rocCompanyInfo']

    # Information
    company_info['companyCountry'] = origin_country_mapping(company_info['companyCountry'])
    company_info['companyStatus'] = comp_status_mapping(company_info['companyStatus'], lang)
    company_info['companyType'] = comp_type_mapping(company_info['companyType'], lang)
    company_info['statusOfCompany'] = status_of_comp_mapping(company_info['statusOfCompany'])

    if 'latestDocUpdateDate' in company_info.keys():
        company_info['latestDocUpdateDate'] = time_mapping(company_info['latestDocUpdateDate'])
    else:
        company_info['latestDocUpdateDate'] = None
    
    if 'lastUpdateDate' in company_info.keys():
        company_info['lastUpdateDate'] = time_mapping(company_info['lastUpdateDate'])
    else:
        company_info['lastUpdateDate'] = None

    if 'dateOfChange' in company_info.keys():
        company_info['dateOfChange'] = time_mapping(company_info['dateOfChange'])
    else:
        company_info['dateOfChange'] = None
    
    if 'incorpDate' in company_info.keys():
        company_info['incorpDate'] = time_mapping(company_info['incorpDate'])
    else:
        company_info['incorpDate'] = None

    if 'registrationDate' in company_info.keys():
        company_info['registrationDate'] = time_mapping(company_info['registrationDate'])
    else:
        company_info['registrationDate'] = None

    registered_address_info['state'] = state_mapping(registered_address_info['state'])
    business_address_info['state'] = state_mapping(business_address_info['state'])

    temp_comp_status = status_of_comp_mapping(company_info['companyStatus']) 

    # temp_incorp_date = time_mapping(company_info['incorpDate'])
    
    # Summary of share capital
    total_issued = float(share_capital_info['totalIssued'])
    ordinary_cash = float(share_capital_info['ordinaryCash'])
    ordinary_a_cash = float(share_capital_info['ordinaryACash'])
    ordinary_b_cash = float(share_capital_info['ordinaryBCash'])

    ordinary_non_cash = float(share_capital_info['ordinaryOtherwise'])
    ordinary_a_non_cash = float(share_capital_info['ordinaryAOtherwise'])
    ordinary_b_non_cash = float(share_capital_info['ordinaryBOtherwise'])

    ordinary_issued_share = float(share_capital_info['ordinaryIssued'])
    ordinary_a_issued_share = float(share_capital_info['ordinaryAIssued'])
    ordinary_b_issued_share = float(share_capital_info['ordinaryBIssued'])
    
    preference_cash = float(share_capital_info['preferenceCash'])
    preference_a_cash = float(share_capital_info['preferenceACash'])
    preference_b_cash = float(share_capital_info['preferenceBCash'])

    preference_non_cash = float(share_capital_info['preferenceOtherwise'])
    preference_a_non_cash = float(share_capital_info['preferenceAOtherwise'])
    preference_b_non_cash = float(share_capital_info['preferenceBOtherwise'])

    preference_issued_share = float(share_capital_info['preferenceIssued'])
    preference_a_issued_share = float(share_capital_info['preferenceAIssued'])
    preference_b_issued_share = float(share_capital_info['preferenceBIssued'])

    others_cash = float(share_capital_info['othersCash'])
    others_non_cash = float(share_capital_info['othersOtherwise'])
    others_issued = float(share_capital_info['othersIssued'])

    # Allotments
    list_of_allotments = mdw_1['allotmentOfShare']['allotmentShareList']['allotmentShareList']

    allotments_data = []

    act_year_enacted = datetime(year=2017,month=1, day=31).astimezone(pytz.timezone(time_zone))
    
    if isinstance(list_of_allotments, list):
        list_of_allotments.sort(key = lambda x:('#text' in x['dtAllot'], x['dtAllot'].get('#text')), reverse=True) 

        for allotment in list_of_allotments:
            allot_date_aware = make_aware(datetime.strptime(allotment['dtAllot']['#text'], '%Y-%m-%dT%H:%M:%S.000Z'))
            # print()
            #and allot_date_aware > act_year_enacted
            if len(allotments_data) < 11 and allot_date_aware > act_year_enacted:
                allotment['dtAllot'] = time_mapping(allotment['dtAllot']['#text'])
                allotment['issuedShare'] = float(allotment['issuedShare'])
                allotment['totalIssuedShare'] = float(allotment['totalIssuedShare'])
                allotment['pricePerShare'] = float(allotment['pricePerShare'])

                allotee_list = []
                allotees_ = allotment['particularAlloteesList']['particularAlloteesList']

                if allotees_:
                    if isinstance(allotees_, list):
                        for allotee in allotees_:
                            allotee['address']['state'] = state_mapping(allotee['address']['state'])
                            allotee['noOfShares'] = float(allotee['noOfShares'])
                            
                            if len(allotee['alloteeId']) is 12:
                                id_1 = allotee['alloteeId'][0:6]
                                id_2 = allotee['alloteeId'][6:8]
                                id_3 = allotee['alloteeId'][8:]
                                allotee['alloteeId'] = id_1 + '-' + id_2  + '-'  + id_3
                            else:
                                pass

                            allotee_list.append(allotee)
                    else:
                        allotees_['address']['state'] = state_mapping(allotees_['address']['state'])
                        allotees_['noOfShares'] = float(allotees_['noOfShares'])

                        if len(allotees_['alloteeId']) is 12:
                            id_1 = allotees_['alloteeId'][0:6]
                            id_2 = allotees_['alloteeId'][6:8]
                            id_3 = allotees_['alloteeId'][8:]
                            allotees_['alloteeId'] = id_1 + '-' + id_2  + '-'  + id_3
                        else:
                            pass
                        
                        allotee_list.append(allotees_)
                else:
                    allotee_list = []
                
                allotment['allotee'] = allotee_list
                allotments_data.append(allotment)
    else:
        allotment = list_of_allotments
        allotment['dtAllot'] = time_mapping(allotment['dtAllot']['#text'])
        allotment['issuedShare'] = float(allotment['issuedShare'])
        allotment['totalIssuedShare'] = float(allotment['totalIssuedShare'])
        allotment['pricePerShare'] = float(allotment['pricePerShare'])

        allotee_list = []
        allotees_ = allotment['particularAlloteesList']['particularAlloteesList']

        if allotees_:
            if isinstance(allotees_, list):
                for allotee in allotees_:
                    allotee['address']['state'] = state_mapping(allotee['address']['state'])
                    allotee['noOfShares'] = float(allotee['noOfShares'])

                    if len(allotee['alloteeId']) is 12:
                        id_1 = allotee['alloteeId'][0:6]
                        id_2 = allotee['alloteeId'][6:8]
                        id_3 = allotee['alloteeId'][8:]
                        allotee['alloteeId'] = id_1 + '-' + id_2  + '-'  + id_3
                    else:
                        pass

                    allotee_list.append(allotee)
                    
            else:
                allotees_['address']['state'] = state_mapping(allotees_['address']['state'])
                allotees_['noOfShares'] = float(allotees_['noOfShares'])

                if len(allotees_['alloteeId']) is 12:
                    id_1 = allotees_['alloteeId'][0:6]
                    id_2 = allotees_['alloteeId'][6:8]
                    id_3 = allotees_['alloteeId'][8:]
                    allotees_['alloteeId'] = id_1 + '-' + id_2  + '-'  + id_3
                else:
                    pass

                allotee_list.append(allotees_)
        else:
            allotment['particularAlloteesList'] = None
        
        allotment['allotee'] = allotee_list
        allotments_data.append(allotment)

    data_ready = {
        'mdw1': data_mdw_1,
        'mdw2': data_mdw_2,
        'business_address_info': business_address_info,
        'registered_address_info': registered_address_info,
        'share_capital_info': {
            'ordinaryCash': ordinary_cash,
            'ordinaryACash': ordinary_a_cash,
            'ordinaryBCash': ordinary_b_cash,
            'ordinaryNonCash': ordinary_non_cash,
            'ordinaryANonCash': ordinary_a_non_cash,
            'ordinaryBNonCash': ordinary_b_non_cash,
            'ordinaryIssued': ordinary_issued_share,
            'ordinaryAIssued': ordinary_a_issued_share,
            'ordinaryBIssued': ordinary_b_issued_share,
            'preferenceCash': preference_cash,
            'preferenceACash': preference_a_cash,
            'preferenceBCash': preference_b_cash,
            'preferenceNonCash': preference_non_cash,
            'preferenceANonCash': preference_a_non_cash,
            'preferenceBNonCash': preference_b_non_cash,
            'preferenceIssued': preference_issued_share,
            'preferenceAIssued': preference_a_issued_share,
            'preferenceBIssued': preference_b_issued_share,
            'othersCash': others_cash,
            'othersNonCash': others_non_cash,
            'othersIssued': others_issued,
            'totalIssued': total_issued,
            'totalCash': ordinary_cash + ordinary_a_cash + ordinary_b_cash + preference_cash + preference_a_cash + preference_b_cash + others_cash,
            'totalNonCash': ordinary_non_cash + ordinary_a_non_cash + ordinary_b_non_cash + preference_non_cash + preference_a_non_cash + preference_b_non_cash + others_non_cash,
            'totalIssuedShared': ordinary_issued_share + ordinary_a_issued_share + ordinary_b_issued_share + preference_issued_share + preference_a_issued_share + preference_b_issued_share + others_issued,
        },
        'allotment_info': allotments_data,
        'company_no': data_mdw_2['newFormatNo'] + '(' + data_mdw_2['oldFormatNo'] + ')',
        'company_info': company_info,
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y'), 
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime('%d-%m-%Y %-H:%M:%S')
    }


    return data_ready
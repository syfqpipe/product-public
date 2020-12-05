import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import (
    state_mapping, 
    origin_country_mapping,
    status_of_comp_mapping,
    status_mapping,
    comp_type_mapping,
    time_mapping,
    comp_status_mapping
)

def info_hist_2(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'


    import pprint
    pp = pprint.PrettyPrinter(indent=1)
    #pp.pprint(mdw_1)
    print('____________   ')
    print('historical year 1: ', data_mdw_1)
    print('____________   ')
    
    if 'incorpDate' in data_mdw_1["rocCompanyInfo"]:
        temp_incorp_date = time_mapping(data_mdw_1["rocCompanyInfo"]['incorpDate'])
    else:
        temp_incorp_date = None

    if 'dateOfChange' in data_mdw_1["rocCompanyInfo"]:
        temp_date_of_change = time_mapping(data_mdw_1["rocCompanyInfo"]['dateOfChange'])
    else:
        temp_date_of_change = None

    temp_comp_type = comp_type_mapping(data_mdw_1['rocCompanyInfo']['companyType'], lang)
    
    temp_comp_status = comp_status_mapping(data_mdw_1['rocCompanyInfo']['companyStatus'], lang)

    temp_status_of_comp = status_of_comp_mapping(data_mdw_1['rocCompanyInfo']['statusOfCompany'])
    
    temp_reg_address_1_old = data_mdw_1['rocRegAddressInfo']['address1']
    temp_reg_address_2_old = data_mdw_1['rocRegAddressInfo']['address2']
    temp_reg_address_3_old = data_mdw_1['rocRegAddressInfo']['address3']
    temp_reg_postcode_old = data_mdw_1['rocRegAddressInfo']['postcode']
    temp_reg_town_old = data_mdw_1['rocRegAddressInfo']['town']
    temp_reg_state_old = data_mdw_1['rocRegAddressInfo']['state']

    if temp_reg_address_1_old == 'TIADA FAIL':
        temp_reg_address_1_new = None
    elif temp_reg_address_1_old == None:
        temp_reg_address_1_new = None
    else:
        temp_reg_address_1_new = temp_reg_address_1_old

    if temp_reg_address_2_old == 'TIADA FAIL':
        temp_reg_address_2_new = None
    elif temp_reg_address_2_old == None:
        temp_reg_address_2_new = None
    else:
        temp_reg_address_2_new = temp_reg_address_2_old

    if temp_reg_address_3_old == 'TIADA FAIL':
        temp_reg_address_3_new = None
    elif temp_reg_address_3_old == None:
        temp_reg_address_3_new = None
    else:
        temp_reg_address_3_new = temp_reg_address_3_old

    if temp_reg_state_old == 'TIADA FAIL':
        temp_reg_state_new = None
    elif temp_reg_state_old == None:
        temp_reg_state_new = None
    else:
        temp_reg_state_new = state_mapping(temp_reg_state_old)
    
    if temp_reg_postcode_old == 'TIADA FAIL':
        temp_reg_postcode_new = None
    elif temp_reg_postcode_old == None:
        temp_reg_postcode_new = None
    else:
        temp_reg_postcode_new = temp_reg_postcode_old

    if temp_reg_town_old == 'TIADA FAIL':
        temp_reg_town_new = None
    elif temp_reg_town_old == None:
        temp_reg_town_new = None
    else:
        temp_reg_town_new = temp_reg_town_old
    
    temp_comp_origin_old = data_mdw_1['rocCompanyInfo']['companyCountry']

    if temp_comp_origin_old == 'TIADA FAIL':
        temp_comp_origin_new = None
    elif temp_comp_origin_old == None:
        temp_comp_origin_new = None
    else:
        temp_comp_origin_new = origin_country_mapping(temp_comp_origin_old)
    
    temp_biz_address_1_old = data_mdw_1['rocBusinessAddressInfo']['address1']
    temp_biz_address_2_old = data_mdw_1['rocBusinessAddressInfo']['address2']
    temp_biz_address_3_old = data_mdw_1['rocBusinessAddressInfo']['address3']
    temp_biz_postcode_old = data_mdw_1['rocBusinessAddressInfo']['postcode']
    temp_biz_town_old = data_mdw_1['rocBusinessAddressInfo']['town']
    temp_biz_state_old = data_mdw_1['rocBusinessAddressInfo']['state']

    if temp_biz_address_1_old == 'TIADA FAIL':
        temp_biz_address_1_new = None
    elif temp_biz_address_1_old == None:
        temp_biz_address_1_new = None
    else:
        temp_biz_address_1_new = temp_biz_address_1_old

    if temp_biz_address_2_old == 'TIADA FAIL':
        temp_biz_address_2_new = None
    elif temp_biz_address_2_old == None:
        temp_biz_address_2_new = None
    else:
        temp_biz_address_2_new = temp_biz_address_2_old

    if temp_biz_address_3_old == 'TIADA FAIL':
        temp_biz_address_3_new = None
    elif temp_biz_address_3_old == None:
        temp_biz_address_3_new = None
    else:
        temp_biz_address_3_new = temp_biz_address_3_old

    if temp_biz_state_old == 'TIADA FAIL':
        temp_biz_state_new = None
    elif temp_biz_state_old == None:
        temp_biz_state_new = None
    else:
        temp_biz_state_new = state_mapping(temp_biz_state_old)
    
    if temp_biz_postcode_old == 'TIADA FAIL':
        temp_biz_postcode_new = None
    elif temp_biz_postcode_old == None:
        temp_biz_postcode_new = None
    else:
        temp_biz_postcode_new = temp_biz_postcode_old

    if temp_biz_town_old == 'TIADA FAIL':
        temp_biz_town_new = None
    elif temp_biz_town_old == None:
        temp_biz_town_new = None
    else:
        temp_biz_town_new = temp_biz_town_old

    balance_sheet_list = data_mdw_1['rocBalanceSheetListInfo']['rocBalanceSheetInfos']['rocBalanceSheetInfos']
    print('    ')
    print('cendol!!! >>  ', data_mdw_1)
    print('    ')
    
    if 'rocProfitLossInfos' in data_mdw_1['rocProfitLossListInfo']['rocProfitLossInfos']:
        profit_loss_list = data_mdw_1['rocProfitLossListInfo']['rocProfitLossInfos']['rocProfitLossInfos']
    else:
        profit_loss_list =   data_mdw_1['rocProfitLossListInfo']['rocProfitLossInfos']
    
    # balance_sheet_list.sort(key = lambda x:('financialYearEndDate' in x, x['financialYearEndDate']), reverse=True) 
    # profit_loss_list.sort(key = lambda x:('financialYearEndDate' in x, x['financialYearEndDate']), reverse=True) 
    

    balance_sheet_data = []

    
    temp_audit_address_1_old = balance_sheet_list['auditFirmAddress1']
    temp_audit_address_2_old = balance_sheet_list['auditFirmAddress2']
    temp_audit_address_3_old = balance_sheet_list['auditFirmAddress3']
    temp_audit_postcode_old = balance_sheet_list['auditFirmPostcode']
    temp_audit_town_old = balance_sheet_list['auditFirmTown']
    temp_audit_state_old = balance_sheet_list['auditFirmState']

    if temp_audit_address_1_old == 'TIADA FAIL':
        temp_audit_address_1_new = None
    elif temp_audit_address_1_old == None:
        temp_audit_address_1_new = None
    else:
        temp_audit_address_1_new = temp_audit_address_1_old

    if temp_audit_address_2_old == 'TIADA FAIL':
        temp_audit_address_2_new = None
    elif temp_audit_address_2_old == None:
        temp_audit_address_2_new = None
    else:
        temp_audit_address_2_new = temp_audit_address_2_old

    if temp_audit_address_3_old == 'TIADA FAIL':
        temp_audit_address_3_new = None
    elif temp_audit_address_3_old == None:
        temp_audit_address_3_new = None
    else:
        temp_audit_address_3_new = temp_audit_address_3_old

    if temp_audit_state_old == 'TIADA FAIL':
        temp_audit_state_new = None
    elif temp_audit_state_old == None:
        temp_audit_state_new = None
    else:
        temp_audit_state_new = state_mapping(temp_audit_state_old)

    if temp_audit_postcode_old == 'TIADA FAIL':
        temp_audit_postcode_new = None
    elif temp_audit_postcode_old == None:
        temp_audit_postcode_new = None
    else:
        temp_audit_postcode_new = temp_audit_postcode_old

    if temp_audit_town_old == 'TIADA FAIL':
        temp_audit_town_new = None
    elif temp_audit_town_old == None:
        temp_audit_town_new = None
    else:
        temp_audit_town_new = temp_audit_town_old

    if 'financialYearEndDate' in balance_sheet_list:
        financial_year_end = time_mapping(balance_sheet_list['financialYearEndDate'])
    else:
        financial_year_end = None
    
    if 'dateOfTabling' in balance_sheet_list:
        date_of_tabling = time_mapping(balance_sheet_list['dateOfTabling'])
    else:
        date_of_tabling = None

    year_data = {
        'auditor_name': balance_sheet_list['auditFirmName'],
        'auditor_no': balance_sheet_list['auditFirmNo'],
        'auditor_address1': temp_audit_address_1_new,
        'auditor_address2': temp_audit_address_2_new,
        'auditor_address3': temp_audit_address_3_new,
        'auditor_postcode': temp_audit_postcode_new,
        'auditor_town': temp_audit_town_new,
        'auditor_state': temp_audit_state_new,
        'financial_year_end': financial_year_end,
        'financialReportType': balance_sheet_list['financialReportType'],
        'accrualAccType': balance_sheet_list['accrualAccType'],
        'dateOfTabling': date_of_tabling,
        'nonCurrAsset':float(balance_sheet_list['nonCurrAsset']),
        'currentAsset':float(balance_sheet_list['currentAsset']),
        'nonCurrentLiability':float(balance_sheet_list['nonCurrentLiability']),
        'liability':float(balance_sheet_list['liability']),
        'paidUpCapital':float(balance_sheet_list['paidUpCapital']),
        'reserves':float(balance_sheet_list['reserves']),
        'minorityInterest':float(balance_sheet_list['minorityInterest']),
    }
    
    balance_sheet_data.append(year_data)

    profit_loss_data = []

    if 'financialYearEndDate' in profit_loss_list:
        financial_year_end_pl = time_mapping(profit_loss_list['financialYearEndDate'])
    else:
        financial_year_end_pl = None

    year_data = {
        'extraOrdinaryItem': profit_loss_list['extraOrdinaryItem'],
        'financialReportType': profit_loss_list['financialReportType'],
        'financialYearEndDate': financial_year_end_pl,
        'grossDividendRate': profit_loss_list['grossDividendRate'],
        'inappropriateProfitBf': profit_loss_list['inappropriateProfitBf'],
        'inappropriateProfitCf': profit_loss_list['inappropriateProfitCf'],
        'minorityInterest': float(profit_loss_list['minorityInterest']),
        'netDividend': float(profit_loss_list['netDividend']),
        'others': profit_loss_list['others'],
        'priorAdjustment': profit_loss_list['priorAdjustment'],
        'profitAfterTax': float(profit_loss_list['profitAfterTax']),
        'profitBeforeTax': float(profit_loss_list['profitBeforeTax']),
        'profitShareholder': profit_loss_list['profitShareholder'],
        'revenue': float(profit_loss_list['revenue']),
        'surplusAfterTax': profit_loss_list['surplusAfterTax'],
        'surplusBeforeTax': profit_loss_list['surplusBeforeTax'],
        'surplusDeficitAfterTax': profit_loss_list['surplusDeficitAfterTax'],
        'surplusDeficitBeforeTax': profit_loss_list['surplusDeficitBeforeTax'],
        'totalExpenditure': profit_loss_list['totalExpenditure'],
        'totalIncome': profit_loss_list['totalIncome'],
        'totalRevenue': profit_loss_list['totalRevenue'],
        'transferred': profit_loss_list['transferred'],
        'turnover': profit_loss_list['turnover']
    }

    profit_loss_data.append(year_data)

    data_ready = {
        'corpInfo': {
            'compName': data_mdw_1['rocCompanyInfo']['companyName'],
            'compOldName': data_mdw_1['rocCompanyInfo']['companyOldName'],
            'changeDate': temp_date_of_change,
            'compNoNew': data_mdw_2['newFormatNo'],
            'compNoOld': data_mdw_2['oldFormatNo'],
            'checkDigit': data_mdw_1['rocCompanyInfo']['checkDigit'],
            'incorpDate': temp_incorp_date,
            'companyType': temp_comp_type,
            'companyStatus': temp_comp_status,
            'statusOfCompany': temp_status_of_comp,
            'reg_address1': temp_reg_address_1_new,
            'reg_address2': temp_reg_address_2_new,
            'reg_address3': temp_reg_address_3_new,
            'reg_state': temp_reg_state_new,
            'reg_town': temp_reg_town_new,
            'reg_postcode': temp_reg_postcode_new,
            'reg_origin': temp_comp_origin_new,
            'biz_address1': temp_biz_address_1_new,
            'biz_address2': temp_biz_address_2_new,
            'biz_address3': temp_biz_address_3_new,
            'biz_state': temp_biz_state_new,
            'biz_town': temp_biz_town_new,
            'biz_postcode': temp_biz_postcode_new,
            'biz_nature': data_mdw_1['rocCompanyInfo']['businessDescription']
        },
        'balance_sheet': balance_sheet_data,
        'profit_loss': profit_loss_data,
        'generated_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %-H:%M:%S"),
        'printing_time': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y"),
        'mdw': data_mdw_1
    }

    return data_ready
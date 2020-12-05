import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import state_mapping, origin_country_mapping

def info_fin_2(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'

    print('_____________')
    print('info_fin:   ', data_mdw_1)
    print('_____________')

    import pprint
    pp = pprint.PrettyPrinter(indent=1)
    #pp.pprint(mdw_1)
    # print('asdasd<<<<<', data_mdw_1['rocCompanyInfo'])
    temp_comp_status_old = data_mdw_1['rocCompanyInfo']['companyStatus']
    
    # if temp_comp_status_old == 'E':
    #     temp_comp_status_new = 'Existing'
    # elif temp_comp_status_old == 'W':
    #     temp_comp_status_new = 'Winding Up'
    # elif temp_comp_status_old == 'D':
    #     temp_comp_status_new = 'Dissolved'
    
    if 'dateOfChange' in data_mdw_1["rocCompanyInfo"].keys():
        date_of_change = make_aware(datetime.strptime(data_mdw_1["rocCompanyInfo"]['dateOfChange'], '%Y-%m-%dT%H:%M:%S.000Z'))
        date_of_change_str = date_of_change.astimezone(pytz.timezone(time_zone)).strftime(date_format)
    else:
        date_of_change_str = 'NIL'

    temp_incorpDate_old = make_aware(datetime.strptime(data_mdw_1['rocCompanyInfo']['incorpDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_incorpDate_new = temp_incorpDate_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    temp_comp_info_incorp_date_old = make_aware(datetime.strptime(data_mdw_1['rocCompanyInfo']['incorpDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_comp_info_incorp_date_new = temp_comp_info_incorp_date_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    temp_comp_type_old = data_mdw_1['rocCompanyInfo']['companyType']
    # if temp_comp_type_old == 'R':
    #     temp_comp_type_new = 'PRIVATE LIMITED'
    # elif temp_comp_type_old == 'U':
    #     temp_comp_type_new = 'PUBLIC LIMITED'
    
    temp_comp_status_old = data_mdw_1['rocCompanyInfo']['companyStatus']
    # if temp_comp_status_old == 'S':
    #     temp_comp_status_new = 'LIMITED BY SHARES'
    # elif temp_comp_status_old == 'G':
    #     temp_comp_status_new = 'LIMITED BY GUARANTEE'
    # elif temp_comp_status_old == 'B':
    #     temp_comp_status_new = 'LIMITED BY SHARE AND GUARANTEE'
    # elif temp_comp_status_old == 'U':
    #     temp_comp_status_new = 'UNLIMITED'

    temp_status_of_comp_old = data_mdw_1['rocCompanyInfo']['statusOfCompany']
    # if temp_status_of_comp_old == 'E':
    #     temp_status_of_comp_new = 'Existing'
    # elif temp_status_of_comp_old == 'W':
    #     temp_status_of_comp_new = 'Winding Up'
    # elif temp_status_of_comp_old == 'D':
    #     temp_status_of_comp_new = 'Dissolved'
    
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
    elif temp_comp_origin_old:
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
    profit_loss_list = data_mdw_1['rocProfitLossListInfo']['rocProfitLossInfos']['rocProfitLossInfos']

    balance_sheet_list.sort(key = lambda x:('financialYearEndDate' in x, x['financialYearEndDate']), reverse=True) 
    profit_loss_list.sort(key = lambda x:('financialYearEndDate' in x, x['financialYearEndDate']), reverse=True) 

    balance_sheet_data = []
    # print('bsl >>>>>>>>', balance_sheet_list)
    if isinstance(balance_sheet_list, list):
        for bs_item in balance_sheet_list:
            # print('bsssss >>>', bs_item)
            temp_audit_address_1_old = bs_item['auditFirmAddress1']
            temp_audit_address_2_old = bs_item['auditFirmAddress2']
            temp_audit_address_3_old = bs_item['auditFirmAddress3']
            temp_audit_postcode_old = bs_item['auditFirmPostcode']
            temp_audit_town_old = bs_item['auditFirmTown']
            temp_audit_state_old = bs_item['auditFirmState']

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
        
            financial_year_end_old = make_aware(datetime.strptime(bs_item['financialYearEndDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
            financial_year_end_new = financial_year_end_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            date_of_tabling_old = make_aware(datetime.strptime(bs_item['dateOfTabling'], '%Y-%m-%dT%H:%M:%S.000Z'))
            date_of_tabling_new = date_of_tabling_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            year_data = {
                'auditor_name': bs_item['auditFirmName'],
                'auditor_address1': temp_audit_address_1_new,
                'auditor_address2': temp_audit_address_2_new,
                'auditor_address3': temp_audit_address_3_new,
                'auditor_postcode': temp_audit_postcode_new,
                'auditor_town': temp_audit_town_new,
                'auditor_state': temp_audit_state_new,
                'financial_year_end': financial_year_end_new,
                'financialReportType': bs_item['financialReportType'],
                'accrualAccType': bs_item['accrualAccType'],
                'dateOfTabling': date_of_tabling_new,
                'nonCurrAsset': float(bs_item['nonCurrAsset']),
                'currentAsset': float(bs_item['currentAsset']),
                'nonCurrentLiability': bs_item['longTermLiability'],
                'liability': bs_item['liability'],
                'paidUpCapital': bs_item['paidUpCapital'],
                'reserves': bs_item['reserves'],
                'minorityInterest': bs_item['minorityInterest'],
            }
            
            balance_sheet_data.append(year_data)
    else:
        # print('bsssss >>>', bs_item)
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
    
        financial_year_end_old = make_aware(datetime.strptime(balance_sheet_list['financialYearEndDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
        financial_year_end_new = financial_year_end_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

        date_of_tabling_old = make_aware(datetime.strptime(balance_sheet_list['dateOfTabling'], '%Y-%m-%dT%H:%M:%S.000Z'))
        date_of_tabling_new = date_of_tabling_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

        year_data = {
            'auditor_name': balance_sheet_list['auditFirmName'],
            'auditor_address1': temp_audit_address_1_new,
            'auditor_address2': temp_audit_address_2_new,
            'auditor_address3': temp_audit_address_3_new,
            'auditor_postcode': temp_audit_postcode_new,
            'auditor_town': temp_audit_town_new,
            'auditor_state': temp_audit_state_new,
            'financial_year_end': financial_year_end_new,
            'financialReportType': balance_sheet_list['financialReportType'],
            'accrualAccType': balance_sheet_list['accrualAccType'],
            'dateOfTabling': date_of_tabling_new,
            'nonCurrAsset': float(balance_sheet_list['nonCurrAsset']),
            'currentAsset': float(balance_sheet_list['currentAsset']),
            'nonCurrentLiability': balance_sheet_list['nonCurrentLiability'],
            'liability': balance_sheet_list['liability'],
            'paidUpCapital': balance_sheet_list['paidUpCapital'],
            'reserves': balance_sheet_list['reserves'],
            'minorityInterest': balance_sheet_list['minorityInterest'],
        }
        
        balance_sheet_data.append(year_data)

    profit_loss_data = []

    if isinstance(profit_loss_list, list):
        for pl_item in profit_loss_list:    
        
            financial_year_end_old = make_aware(datetime.strptime(pl_item['financialYearEndDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
            financial_year_end_new = financial_year_end_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

            year_data = {
                'extraOrdinaryItem': pl_item['extraOrdinaryItem'],
                'financialReportType': pl_item['financialReportType'],
                'financialYearEndDate': pl_item['financialYearEndDate'],
                'grossDividendRate': pl_item['grossDividendRate'],
                'inappropriateProfitBf': pl_item['inappropriateProfitBf'],
                'inappropriateProfitCf': pl_item['inappropriateProfitCf'],
                'minorityInterest': pl_item['minorityInterest'],
                'netDividend': pl_item['netDividend'],
                'others': pl_item['others'],
                'priorAdjustment': pl_item['priorAdjustment'],
                'profitAfterTax': pl_item['profitAfterTax'],
                'profitBeforeTax': pl_item['profitBeforeTax'],
                'profitShareholder': pl_item['profitShareholder'],
                'revenue': pl_item['revenue'],
                'surplusAfterTax': pl_item['surplusAfterTax'],
                'surplusBeforeTax': pl_item['surplusBeforeTax'],
                'surplusDeficitAfterTax': pl_item['surplusDeficitAfterTax'],
                'surplusDeficitBeforeTax': pl_item['surplusDeficitBeforeTax'],
                'totalExpenditure': pl_item['totalExpenditure'],
                'totalIncome': pl_item['totalIncome'],
                'totalRevenue': pl_item['totalRevenue'],
                'transferred': pl_item['transferred'],
                'turnover': pl_item['turnover']
            }
            
            profit_loss_data.append(year_data)
    else:    
        financial_year_end_old = make_aware(datetime.strptime(profit_loss_list['financialYearEndDate'], '%Y-%m-%dT%H:%M:%S.000Z'))
        financial_year_end_new = financial_year_end_old.astimezone(pytz.timezone(time_zone)).strftime(date_format)

        year_data = {
            'extraOrdinaryItem': profit_loss_list['extraOrdinaryItem'],
            'financialReportType': profit_loss_list['financialReportType'],
            'financialYearEndDate': profit_loss_list['financialYearEndDate'],
            'grossDividendRate': profit_loss_list['grossDividendRate'],
            'inappropriateProfitBf': profit_loss_list['inappropriateProfitBf'],
            'inappropriateProfitCf': profit_loss_list['inappropriateProfitCf'],
            'minorityInterest': profit_loss_list['minorityInterest'],
            'netDividend': profit_loss_list['netDividend'],
            'others': profit_loss_list['others'],
            'priorAdjustment': profit_loss_list['priorAdjustment'],
            'profitAfterTax': profit_loss_list['profitAfterTax'],
            'profitBeforeTax': profit_loss_list['profitBeforeTax'],
            'profitShareholder': profit_loss_list['profitShareholder'],
            'revenue': profit_loss_list['revenue'],
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
            'changeDate': date_of_change_str,
            'compNoNew': data_mdw_2['newFormatNo'],
            'compNoOld': data_mdw_2['oldFormatNo'],
            'checkDigit': data_mdw_1['rocCompanyInfo']['checkDigit'],
            'incorpDate': temp_comp_info_incorp_date_new,
            'companyType': temp_comp_type_old,
            'companyStatus': temp_comp_status_old,
            'statusOfCompany': temp_status_of_comp_old,
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
        'mdw1': mdw_1
    }

    return data_ready
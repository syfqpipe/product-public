import requests
import json
import xmltodict

def get_info_financial_year(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getInfoFinancialYear>
         <!--Optional:-->
         <header>
            <!--Optional:-->
            <customerId>SSMProduk</customerId>
            <!--Optional:-->
            <customerReferenceNo>SSMProdukTest</customerReferenceNo>
            <!--Optional:-->
            <customerRequestDate></customerRequestDate>
         </header>
         <!--Optional:-->
         <request>
            <!--Optional:-->
            <supplyFinancialReq>
               <!--Optional:-->
               <coNo>""" + str(registration_number) + """</coNo>
               <!--Optional:-->
               <endYear></endYear>
               <!--Optional:-->
               <ipaddress></ipaddress>
               <!--Optional:-->
               <remark></remark>
               <!--Optional:-->
               <startYear></startYear>
               <!--Optional:-->
               <type></type>
            </supplyFinancialReq>
         </request>
      </inf:getInfoFinancialYear>
   </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoFinancialYearResponse']['response']['getInfoFinancialYearReturn']
    # print('fin', parsed_response)
    # print('k', len(parsed_response['rocFinancialYearInfos']['rocFinancialYearInfos']))
    if parsed_response['errorMsg']:
        return {
            'year2': False,
            'year3': False,
            'year5': False,
            'year10': False,
            'years': None
        }
    elif parsed_response['rocFinancialYearInfos'] == None:
        return {
            'year2': False,
            'year3': False,
            'year5': False,
            'year10': False,
            'years': None
        }
    else:
        year_info = parsed_response['rocFinancialYearInfos']['rocFinancialYearInfos']
        year_length = len(year_info)
        years = []

        for year_ in year_info:
            years.append(year_['financialYearEndDate'])

        if year_length > 1 and year_length < 3:
            return {
                'year2': True,
                'year3': False,
                'year5': False,
                'year10': False,
                'years': years
            }
        elif year_length > 1 and year_length < 5:
            return {
                'year2': True,
                'year3': True,
                'year5': False,
                'year10': False,
                'years': years
            }
        elif year_length > 1 and year_length < 10:
            return {
                'year2': True,
                'year3': True,
                'year5': True,
                'year10': False,
                'years': years
            }
        elif year_length > 9:
            return {
                'year2': True,
                'year3': True,
                'year5': True,
                'year10': True,
                'years': years
            }
        else:
            return {
                'year2': True,
                'year3': False,
                'year5': False,
                'year10': False
            }
    
    
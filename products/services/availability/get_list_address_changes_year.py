import requests
import json
import xmltodict

def get_list_address_changes_year(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getListAddressYearChgs>
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
            <req>
               <!--Optional:-->
               <checkDigit></checkDigit>
               <!--Optional:-->
               <companyNo>""" + str(registration_number) + """</companyNo>
               <!--Optional:-->
               <type></type>
            </req>
         </request>
      </inf:getListAddressYearChgs>
   </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getListAddressYearChgsResponse']['response']['getListYearChgsReturn']
    print('list_address_year', parsed_response)
    if parsed_response['errorMsg']:
        return False
    elif parsed_response['year'] == None:
        return False
    else:
        years = []
        years_parsed = parsed_response['year']['year']
        if isinstance(years_parsed, list):
            for year_ in years_parsed:
                years.append(
                    year_['#text']
                )
        else:
            years.append(
                years_parsed['#text']
            )

        return years
        # years = []
        # years_original = parsed_response['year']
        # years_length = len(years_original)
        # print('l', years_length)
        # # return years_original sadjasdsad
        # if years_length == 1:
        #     years.append({
        #         'year': years_original['year']['#text']
        #     })
        #     return years
        # else:
        #     for year_ in years_original['year']:
        #         print(year_)
        #         years.append({
        #             'year': year_['#text']
        #         })
        #     return years

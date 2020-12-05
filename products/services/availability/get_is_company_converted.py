import requests
import json
import xmltodict

def get_is_company_converted(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:isCompanyConverted>
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
               <checkDigit>K</checkDigit>
               <!--Optional:-->
               <companyNo>""" + str(registration_number) + """</companyNo>
               <!--Optional:-->
               <type></type>
            </req>
         </request>
      </inf:isCompanyConverted>
   </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:isCompanyConvertedResponse']['response']['checkIfExistReturn']
   #  print('is_company_converted', parsed_response)
    if parsed_response['answer'] == False or parsed_response['answer'] == 'false':
        return False
    else:
        return parsed_response['formCode']
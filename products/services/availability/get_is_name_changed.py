import requests
import json
import xmltodict

def get_is_name_changed(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:isNameChanged>
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
      </inf:isNameChanged>
   </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:isNameChangedResponse']['response']['checkIfExistReturn']
    print('is_name_changed', parsed_response)
    if parsed_response['answer'] == True or parsed_response['answer'] == 'true':
        return True
    else:
        return False
    









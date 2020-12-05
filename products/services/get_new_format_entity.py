import requests
import json
import xmltodict

def get_new_format_entity(url, headers, registration_number, entity_type):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getNewFormatEntityNo>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <newFormatEntityNoReq>
                    <agencyId>SSMProduk</agencyId>
                    <checkDigit></checkDigit>
                    <formatType></formatType>
                    <regNo>""" + str(registration_number) + """</regNo>
                    <tableId></tableId>
                    <type>""" + entity_type + """</type>
                </newFormatEntityNoReq>
            </request>
        </inf:getNewFormatEntityNo>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
#    print(middleware_response_json)
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getNewFormatEntityNoResponse']['response']['getNewFormatEntityNoReturn']
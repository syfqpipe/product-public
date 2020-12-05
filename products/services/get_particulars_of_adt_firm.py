import requests
import json
import xmltodict

def get_particulars_of_adt_firm(url, headers, registration_number, entity_type):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my"> 
    <soapenv:Header/>
    <soapenv:Body>
        <inf:getParticularsOfAdtFirm> 
            <header>
                <customerId>SSMProduk</customerId> 
                <customerReferenceNo></customerReferenceNo>  
                <customerRequestDate></customerRequestDate>
            </header>  
            <request> 
                <req>
                    <adtFirmNo>""" + str(registration_number) + """</adtFirmNo> 
                </req>
            </request> 
        </inf:getParticularsOfAdtFirm>
    </soapenv:Body> 
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getParticularsOfAdtFirmResponse']['response']['getParticularsOfAdtFirmReturn']
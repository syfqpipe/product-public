import requests
import json
import xmltodict

def get_details_of_shareholders(url, headers, registration_number, entity_type):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header/>
    <soapenv:Body>
        <inf:getDetailsOfShareholders>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header> 
            <request> 
                <req>
                    <checkDigit></checkDigit> 
                    <companyNo>""" + str(registration_number) + """</companyNo> 
                    <gstAmount></gstAmount> 
                    <infoAmount></infoAmount> 
                    <invoiceNo></invoiceNo> 
                    <type>0</type>
                </req> 
            </request>
        </inf:getDetailsOfShareholders> 
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getDetailsOfShareholdersResponse']['response']['getDetailsOfShareholdersReturn']
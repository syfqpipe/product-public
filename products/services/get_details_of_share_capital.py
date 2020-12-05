import requests
import json
import xmltodict

def get_details_of_share_capital(url, headers, registration_number, entity_type):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getDetailsOfShareCapital>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <req>
                    <checkDigit>M</checkDigit>
                    <companyNo>""" + str(registration_number) + """</companyNo>
                    <gstAmount>0</gstAmount>
                    <infoAmount>0</infoAmount>
                    <invoiceNo>0</invoiceNo>
                    <type>0</type>
                </req>
            </request>
        </inf:getDetailsOfShareCapital>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getDetailsOfShareCapitalResponse']['response']['getDetailsOfShareCapitalReturn']
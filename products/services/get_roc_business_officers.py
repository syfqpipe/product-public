import requests
import json
import xmltodict

def get_roc_business_officers(url, headers, registration_number, entity_type):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getRocBusinessOfficers>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <rocCompanyOfficersReq>
                    <checkDigit>V</checkDigit>
                    <fromDate>2000-02-02T00:00:00</fromDate>
                    <gstAmount>0</gstAmount>
                    <infoAmount>0</infoAmount>
                    <invoiceNo></invoiceNo>
                    <ipaddress></ipaddress>
                    <regNo>""" + str(registration_number) + """</regNo>
                    <remark></remark>
                    <type>INFOPROFILE</type>
                </rocCompanyOfficersReq>
            </request>
        </inf:getRocBusinessOfficers>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getRocBusinessOfficersResponse']['response']['getRocBusinessOfficersReturn']
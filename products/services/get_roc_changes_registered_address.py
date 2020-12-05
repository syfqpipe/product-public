import requests
import json
import xmltodict

def get_roc_changes_registered_address(url, headers, registration_number, entity_type):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getRocChangesRegisteredAddress>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <cRegisteredAddr>
                    <checkDigit>T</checkDigit>
                    <fromDate>1990-02-01T00:00:00</fromDate>
                    <gstAmount>0</gstAmount>
                    <infoAmount>0</infoAmount>
                    <invoiceNo></invoiceNo>
                    <ipaddress></ipaddress>
                    <regNo>""" + str(registration_number) + """</regNo>
                    <remark></remark>
                    <type></type>
                </cRegisteredAddr>
            </request>
        </inf:getRocChangesRegisteredAddress>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getRocChangesRegisteredAddressResponse']['response']['getRocChangesRegisteredAddressReturn']
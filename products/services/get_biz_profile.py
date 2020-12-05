import requests
import json
import xmltodict

def get_biz_profile(url, headers, registration_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getBizProfile>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyBizReq>
                    <checkDigit></checkDigit>
                    <gstAmount>0</gstAmount>
                    <infoAmount>0</infoAmount>
                    <invoiceNo>0</invoiceNo>
                    <ipaddress></ipaddress>
                    <lastUpdateDate></lastUpdateDate>
                    <regNo>""" + str(registration_number) + """</regNo>
                    <remark></remark>
                    <tableId>ROBINFO</tableId>
                    <type>INFOPROFILE</type>
                </supplyBizReq>
            </request>
        </inf:getBizProfile>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getBizProfileResponse']['response']['getBizProfileReturn']
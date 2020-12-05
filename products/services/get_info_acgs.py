import requests
import json
import xmltodict

# def get_info_acgs(url, headers, registration_number, date_applied):
def get_info_acgs(url, headers, registration_number, entity_type):

    #date_applied = '2020-08-31T00:00:00'

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoAcgs>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <acgsReq>
                    <chkDigit>V</chkDigit>
                    <compNo>""" + str(registration_number) + """</compNo>
                    <dtApplyAcgs>2020-08-31T00:00:00</dtApplyAcgs>
                </acgsReq>
            </request>
        </inf:getInfoAcgs>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoAcgsResponse']['response']['getInfoAcgsReturn']
import requests
import json
import xmltodict

def get_info_hist2(url, headers, registration_number, entity_type, year):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoFin2>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyFin2Req>
                    <coNo>""" + str(registration_number) + """</coNo>
                    <startYear>""" + str(year) + """</startYear>
                    <ipaddress></ipaddress>
                    <remark></remark>
                    <endYear>""" + str(year) + """</endYear>
                    <type>INFOFINHISTY</type>
                </supplyFin2Req>
            </request>
        </inf:getInfoFin2>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoFin2Response']['response']['getInfoFin2Return']
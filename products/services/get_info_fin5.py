import requests
import json
import xmltodict

def get_info_fin5(url, headers, registration_number, entity_type, start_year, end_year):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoFin5>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyFin5Req>
                    <coNo>""" + str(registration_number) + """</coNo>
                    <startYear>""" + start_year + """</startYear>
                    <ipaddress></ipaddress>
                    <remark></remark>
                    <endYear>""" + end_year + """</endYear>
                    <type>INFOFINHISTY</type>
                </supplyFin5Req>
            </request>
        </inf:getInfoFin5>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoFin5Response']['response']['getInfoFin5Return']
import requests
import json
import xmltodict
import datetime

now = datetime.datetime.now()

def get_info_fin10(url, headers, registration_number, entity_type, start_year, end_year):
   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoFin10>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyFin10Req>
                    <coNo>""" + str(registration_number) + """</coNo>
                    <startYear>""" + str(now.year - 10 )+ """</startYear>
                    <ipaddress></ipaddress>
                    <remark></remark>
                    <endYear>""" + str(now.year) + """</endYear>
                    <type>INFOFINHISTY</type>
                </supplyFin10Req>
            </request>
        </inf:getInfoFin10>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoFin10Response']['response']['getInfoFin10Return']
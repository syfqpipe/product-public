import requests
import json
import xmltodict

def get_info_financial(url, headers, registration_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my"> 
    <soapenv:Header/>
    <soapenv:Body>
        <inf:getInfoFinancialYear> 
            <header>
                <customerId>SSMProduk</customerId> 
                <customerReferenceNo></customerReferenceNo> 
                <customerRequestDate></customerRequestDate>
            </header> 
            <request>
                <supplyFinancialReq> 
                    <coNo>""" + str(registration_number) + """</coNo> 
                    <ipaddress></ipaddress> 
                    <remark></remark> 
                    <type></type>
                </supplyFinancialReq> 
            </request>
        </inf:getInfoFinancialYear> 
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoFinancialYearResponse']['response']['getInfoFinancialYearReturn']
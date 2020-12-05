import requests
import json
import xmltodict

def get_image(url, headers, registration_number, entity_type, check_digit, version_id):

    if entity_type == 'ROC':
        criteria = 'CompanyNo'
        last_digit = int(registration_number) % 10
        document_profile = 'ROC' + str(last_digit)       
        search_value = str(registration_number) + '-' + check_digit 
    else:
        criteria = 'XXX'
        last_digit = registration_number % 10
        document_profile = 'ROC' + str(last_digit) 
        search_value = str(registration_number) + '-' + check_digit
    
    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://integrasistg.ssm.com.my/DocufloService/1/WS">
    <soapenv:Header />
    <soapenv:Body>
        <ws:getImage>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <docufloImg>
                    <companyNo>""" + search_value + """</companyNo>
                    <docProfile>""" + document_profile + """</docProfile>
                    <gstAmount>0</gstAmount>
                    <infoAmount>0</infoAmount>
                    <invoiceNo>0</invoiceNo>
                    <ipaddress></ipaddress>
                    <remark>test</remark>
                    <tableId>""" + document_profile + """</tableId>
                    <type>INFODOCPURC</type>
                    <userName>appadmin</userName>
                    <userPwd>p@ss1234</userPwd>
                    <verId>""" + str(version_id) + """</verId>
                </docufloImg>
            </request>
        </ws:getImage>
    </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json['soapenv:Envelope']['soapenv:Body']['doc:getImageResponse']['response']['getImageReturn']

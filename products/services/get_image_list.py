import requests
import json
import xmltodict

def get_image_list(url, headers, entity_number, entity_type):

    # companyNo 1097967-P

    company_number = ''
    document_profile = ''
    table_id = ''

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://integrasistg.ssm.com.my/DocufloService/1/WS"> 
    <soapenv:Header/>
    <soapenv:Body>
        <ws:getImage>  
            <header>
                <customerId>SSMProduk</customerId> 
                <customerReferenceNo>SSMProduk_123</customerReferenceNo>  
                <customerRequestDate>2020-09-18T04:05:01</customerRequestDate>
            </header>  
            <request> 
                <docufloImg> 
                    <companyNo>""" + company_number + """</companyNo>  
                    <docProfile>""" + document_profile + """</docProfile>  
                    <gstAmount>0</gstAmount>  
                    <infoAmount>0</infoAmount>  
                    <invoiceNo></invoiceNo>  
                    <ipaddress></ipaddress> 
                    <remark></remark> 
                    <tableId></tableId>  
                    <type>INFODOCPURC</type> 
                    <userName>appadmin</userName>  
                    <userPwd>p@ss1234</userPwd> 
                    <verId>3961586</verId>
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
import requests
import json
import xmltodict

def get_biz_cert(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getBizCertCtc>
         <!--Optional:-->
         <header>
            <!--Optional:-->
            <customerId>SSMProduk</customerId>
            <!--Optional:-->
            <customerReferenceNo>SSMProdukTest</customerReferenceNo>
            <!--Optional:-->
            <customerRequestDate></customerRequestDate>
         </header>
         <!--Optional:-->
         <request>
            <!--Optional:-->
            <req>
                <addressId>""" + registration_number + """</addressId>
                <brNo></brNo>
                <ipaddress></ipaddress>
                <remark></remark>
                <type></type>
            </req>
         </request>
      </inf:getBizCertCtc>
   </soapenv:Body>
</soapenv:Envelope>

"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getListAddressYearChgsResponse']['response']['getListYearChgsReturn']
    return parsed_response
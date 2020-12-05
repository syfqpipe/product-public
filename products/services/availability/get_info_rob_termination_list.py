import requests
import json
import xmltodict

def get_info_rob_termination_list(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getInfoRobTerminationList>
         <!--Optional:-->
         <header>
            <!--Optional:-->
            <customerId>SSMProduk</customerId>
            <!--Optional:-->
            <customerReferenceNo>SSMProdukTest</customerReferenceNo>
            <!--Optional:-->
            <customerRequestDate>2020-10-15T09:22:05.359</customerRequestDate>
         </header>
         <!--Optional:-->
         <request>
            <!--Optional:-->
            <supplyInfoReq>
               <!--Optional:-->
               <checkDigit></checkDigit>
               <gstAmount></gstAmount>
               <infoAmount></infoAmount>
               <!--Optional:-->
               <invoiceNo></invoiceNo>
               <!--Optional:-->
               <ipaddress></ipaddress>
               <!--Optional:-->
               <lastUpdateDate></lastUpdateDate>
               <!--Optional:-->
               <regNo>""" + str(registration_number) + """</regNo>
               <!--Optional:-->
               <remark></remark>
               <!--Optional:-->
               <tableId>ROBINFO</tableId>
               <!--Optional:-->
               <type>INFOROBTERLT</type>
            </supplyInfoReq>
         </request>
      </inf:getInfoRobTerminationList>
   </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoRobTerminationListResponse']['response']['getInfoRobTerminationListReturn']
    print('info_rob_termination', parsed_response)
    if parsed_response['errorMsg']:
        return False
    else:
        return True
    









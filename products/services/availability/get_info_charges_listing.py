import requests
import json
import xmltodict

def get_info_charges_listing(url, headers, registration_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getInfoChargeList>
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
            <supplyChargesReq>
               <!--Optional:-->
               <coNo>""" + str(registration_number) + """</coNo>
               <!--Optional:-->
               <gstAmount></gstAmount>
               <!--Optional:-->
               <infoAmount></infoAmount>
               <!--Optional:-->
               <invoiceNo></invoiceNo>
               <!--Optional:-->
               <ipaddress></ipaddress>
               <!--Optional:-->
               <remark></remark>
               <!--Optional:-->
               <tableId>ROCINFO</tableId>
               <!--Optional:-->
               <type>INFOROCCHRGE</type>
            </supplyChargesReq>
         </request>
      </inf:getInfoChargeList>
   </soapenv:Body>
</soapenv:Envelope>
"""
   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   # print(middleware_response_json)
   parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoChargeListResponse']['response']['getInfoChargeListReturn']
   # print('helo', parsed_response['errorMsg'])
   if parsed_response['errorMsg']:
      return False
   else:
      return True
    
    
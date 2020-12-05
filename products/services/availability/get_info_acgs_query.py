import requests
import json
import xmltodict

def get_info_acgs_query(url, headers, registration_number):
   
   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getInfoAcgsQuery>
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
            <acgsQueryReq>
               <!--Optional:-->
               <chkDigit></chkDigit>
               <!--Optional:-->
               <compNo>""" + str(registration_number) + """</compNo>
               <!--Optional:-->
               <dtApplyAcgs>2020-10-15T10:08:55.225</dtApplyAcgs>
            </acgsQueryReq>
         </request>
      </inf:getInfoAcgsQuery>
   </soapenv:Body>
</soapenv:Envelope>
"""
   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoAcgsQueryResponse']['response']['getInfoAcgsQueryReturn']
   
   # print('________')
   # print('acgs', parsed_response)
   # print('________')
   if parsed_response['errorMsg']:
      return False
   else:
      if parsed_response['flag'] == 'NO':
         return True # False
      else:
         True
import requests
import json
import xmltodict

def get_info_incorp(url, headers, registration_number, query_type):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getInfoIncorp>
         <!--Optional:-->
         <header>
            <!--Optional:-->
            <customerId>SSMProduk</customerId>
            <!--Optional:-->
            <customerReferenceNo>SSMProduk</customerReferenceNo>
            <!--Optional:-->
            <customerRequestDate></customerRequestDate>
         </header>
         <!--Optional:-->
         <request>
            <!--Optional:-->
            <supplyIncorpReq>
               <!--Optional:-->
               <checkDigit></checkDigit>
               <!--Optional:-->
               <companyNo>""" + str(registration_number) + """</companyNo>
               <gstAmount></gstAmount>
               <infoAmount></infoAmount>
               <!--Optional:-->
               <invoiceNo></invoiceNo>
               <!--Optional:-->
               <type>rocinfo</type>
            </supplyIncorpReq>
         </request>
      </inf:getInfoIncorp>
   </soapenv:Body>
</soapenv:Envelope> 
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoIncorpResponse']['response']['getInfoIncorpReturn']
   #  print('incorp', parsed_response)
    if query_type == 'share':
      if parsed_response['errorMsg']:
         return False
      elif parsed_response['companyType'] == 'G':
         return False
      else:
         return True
    elif query_type == 'reg':
      if parsed_response['errorMsg']:
         return False
      else:
         return {
         'company_status': parsed_response['companyStatus'],
         'company_type': parsed_response['companyType'],
         'local_or_foreign': parsed_response['localforeignCompany'],
      }
    









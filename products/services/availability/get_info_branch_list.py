import requests
import json
import xmltodict

def get_info_branch_list(url, headers, registration_number):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getInfoBranchListing>
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
            <supplyBranchReq>
               <!--Optional:-->
               <addressId></addressId>
               <!--Optional:-->
               <brNo>""" + str(registration_number) + """</brNo>
               <!--Optional:-->
               <ipaddress></ipaddress>
               <!--Optional:-->
               <remark></remark>
               <!--Optional:-->
               <type>INFOROBFORMD</type>
            </supplyBranchReq>
         </request>
      </inf:getInfoBranchListing>
   </soapenv:Body>
</soapenv:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    parsed_response = middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoBranchListingResponse']['response']['getInfoBranchListingReturn']
   #  print('info_branch', parsed_response)
    if parsed_response['errorMsg']:
        return False
    elif parsed_response['noOfBranches'] == '0':
        return False
    else:
        return True
    









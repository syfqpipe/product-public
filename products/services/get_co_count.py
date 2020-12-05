import requests
import json
import xmltodict

def get_co_count(url, headers, start_date, end_date):

    #sample_date = 2020-08-31T17:05:00Z

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoListingByDateRangeCnt>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyPageCntReq>
                    <endDate>""" + end_date + """</endDate>
                    <regNo />
                    <startDate>""" + start_date + """</startDate>
                    <tableId>ROCINFO</tableId>
                </supplyPageCntReq>
            </request>
        </inf:getInfoListingByDateRangeCnt>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoListingByDateRangeCntResponse']['response']['getInfoListingByDateRangeCntReturn']
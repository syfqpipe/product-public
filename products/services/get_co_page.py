import requests
import json
import xmltodict

def get_co_page(url, headers, start_date, end_date, page_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoListingByDateRangePage>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyPageListReq>
                    <pageNo>""" + page_number + """</pageNo>
                    <regNo></regNo>
                    <endDate>""" + end_date + """</endDate>
                    <regNo />
                    <startDate>""" + start_date + """</startDate>
                    <tableId></tableId>
                </supplyPageListReq>
            </request>
        </inf:getInfoListingByDateRangePage>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoListingByDateRangePageResponse']['response']['getInfoListingByDateRangePageReturn']
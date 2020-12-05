import requests
import json
import xmltodict

# Package C is more about the revenue related of the companies

def get_comp_listing_c(url, headers, 
    company_location, company_origin, company_status, 
    company_type, company_financial_year_end_max, company_financial_year_end_min,
    company_net_profit_max, company_net_profit_min, page_number):
    
    payload = """
<x:Envelope xmlns:x="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://integrasistg.ssm.com.my/ListingService/1/WS">
<x:Header/>
    <x:Body>
        <ws:getCompListingC> 
            <header>
                <customerId>MYDATA</customerId> 
                <customerReferenceNo></customerReferenceNo> 
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <compListingCReq> 
                    <compLocation>"""+ company_location + """</compLocation> 
                    <compOrigin>"""+ company_origin + """</compOrigin> 
                    <compStatus>"""+ company_status + """</compStatus> 
                    <compType>"""+ company_type + """</compType> 
                    <finYrEndMax>"""+ company_financial_year_end_max + """</finYrEndMax> 
                    <finYrEndMin>"""+ company_financial_year_end_min + """</finYrEndMin> 
                    <netProfRangeMax>"""+ company_net_profit_max + """</netProfRangeMax> 
                    <netProfRangeMin>"""+ company_net_profit_min + """</netProfRangeMin> 
                    <pageNo>"""+ page_number + """</pageNo>
                </compListingCReq> 
            </request>
        </ws:getCompListingC> 
    </x:Body>
</x:Envelope>
"""

    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json['sopenv:Envelope']['sopenv:Body']['ws:getCompListingAResponse']['response']['getCompListingAReturn']




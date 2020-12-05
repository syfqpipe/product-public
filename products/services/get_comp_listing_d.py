import requests
import json
import xmltodict

# Package D is related to charges of the companies

def get_comp_listing_d(url, headers, 
    charge_status, charge_type, company_location, 
    company_origin, company_status, company_type,
    page_number):
    
    payload = """
<x:Envelope xmlns:x="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://integrasistg.ssm.com.my/ListingService/1/WS">
    <x:Header/>
        <x:Body>
            <ws:getCompListingD> 
                <header>
                    <customerId>SSMProduk</customerId> 
                    <customerReferenceNo></customerReferenceNo> 
                    <customerRequestDate></customerRequestDate>
                </header> 
                <request>
                    <compListingDReq> 
                        <chargeStatus>""" + charge_status + """</chargeStatus> 
                        <chargeType>""" + charge_type + """</chargeType> 
                        <compLocation>""" + company_location + """</compLocation> 
                        <compOrigin>""" + company_origin + """</compOrigin> 
                        <compStatus>""" + company_status + """</compStatus> 
                        <compType>""" + company_type + """</compType> 
                        <pageNo>""" + page_number + """</pageNo>
                    </compListingDReq> 
                </request>
            </ws:getCompListingD> 
        </x:Body>
</x:Envelope>
"""

    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json['sopenv:Envelope']['sopenv:Body']['ws:getCompListingAResponse']['response']['getCompListingAReturn']




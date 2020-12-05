import requests
import json
import xmltodict


# Package A is more about the incorporation status of the company

def get_comp_listing_a(url, headers, 
    business_code, company_location, company_origin, 
    company_status, company_type, date_from, 
    date_to, page_number):
    
    payload = """
<x:Envelope xmlns:x="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://integrasistg.ssm.com.my/ListingService/1/WS">
    <x:Header />
    <x:Body>
        <ws:getCompListingA>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <compListingAReq>
                    <bizCode>"""+ business_code + """</bizCode>
                    <compLocation>"""+ company_location + """</compLocation>
                    <compOrigin>"""+ company_origin + """</compOrigin>
                    <compStatus>"""+ company_status + """</compStatus>
                    <compType>"""+ company_type + """</compType>
                    <incorpDtFrom>"""+ date_from + """</incorpDtFrom>
                    <incorpDtTo>"""+ date_to + """</incorpDtTo>
                    <pageNo>1</pageNo>
                </compListingAReq>
            </request>
        </ws:getCompListingA>
    </x:Body>
</x:Envelope>
"""
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json["soapenv:Envelope"]["soapenv:Body"]["listing:getCompListingAResponse"]["response"]["getCompListingAReturn"]




"""
<bizCode>10799,10712,20131,22192</bizCode> 
<compLocation>B</compLocation> 
<compOrigin>L</compOrigin> 
<compStatus>E</compStatus> 
<compType>R</compType> 
<incorpDtFrom>2018-01-01T00:00:00</incorpDtFrom> 
<incorpDtTo>2018-01-31T00:00:00</incorpDtTo> 
<pageNo>1</pageNo>
"""    
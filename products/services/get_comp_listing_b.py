import requests
import json
import xmltodict

# Package B is more about the nationality of the shareholder director

def get_comp_listing_b(url, headers, 
    business_code, company_location, company_origin, 
    company_status, company_type, date_from, 
    date_to, page_number, director_nationality, shareholder_nationality):
    
    payload = """
<x:Envelope xmlns:x="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://integrasistg.ssm.com.my/ListingService/1/WS">
    <x:Header/>
    <x:Body>
        <ws:getCompListingB> 
            <header>
                <customerId>SSMProduk</customerId> 
                <customerReferenceNo>?</customerReferenceNo>
                <customerRequestDate>?</customerRequestDate> 
            </header>
            <request>
                <compListingBReq> 
                <compLocation>""" + company_location + """</compLocation> 
                <compOrigin>""" + company_origin + """</compOrigin> 
                <compStatus>""" + company_status + """</compStatus> 
                <compType>""" + company_type + """</compType> 
                <directorNat>""" + director_nationality + """</directorNat> 
                <shareholderNat>""" + shareholder_nationality + """</shareholderNat> 
                <incorpDtFrom>"""+ date_from + """</incorpDtFrom>
                <incorpDtTo>"""+ date_to + """</incorpDtTo>                
                <packageType>B</packageType>
                </compListingBReq> 
            </request>
        </ws:getCompListingB> 
    </x:Body>
</x:Envelope>
"""

    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json["soapenv:Envelope"]["soapenv:Body"]["listing:getCompListingBResponse"]["response"]["getCompListingBReturn"]




"""
<compLocation>C</compLocation> 
<compOrigin>L</compOrigin> 
<compStatus>D</compStatus> 
<compType>U</compType> 
<directorNat>MAL,SIN</directorNat> 
<shareholderNat>MAL,SIN</shareholderNat> 
<packageType>B</packageType>
"""    
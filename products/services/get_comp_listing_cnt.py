import requests
import json
import xmltodict

def get_comp_listing_cnt(url, headers, business_code,charge_status,charge_type,company_location,company_origin,company_status,company_type,director_nationality,year_end_max,year_end_min,date_from,date_to,profit_range_max,profit_range_min,package_type,shareholder_nationality):

    payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:lis="http://listing.ssm.com.my"> 
    <soapenv:Header/>
    <soapenv:Body>
        <lis:getCompListingCnt>  
            <header> 
                <customerId>SSMProduk</customerId>  
                <customerReferenceNo></customerReferenceNo>  
                <customerRequestDate></customerRequestDate>
            </header>  
            <request>
                <compListingCntReq>
                    <bizCode>""" + business_code + """</bizCode>
                    <chargeStatus>""" + charge_status + """</chargeStatus>
                    <chargeType>""" + charge_type + """</chargeType>
                    <compLocation>""" + company_location + """</compLocation> 
                    <compOrigin>""" + company_origin + """</compOrigin> 
                    <compStatus>""" + company_status + """</compStatus> 
                    <compType>""" + company_type + """</compType> 
                    <directorNat>""" + director_nationality + """</directorNat> 
                    <finYrEndMax>""" + year_end_max + """</finYrEndMax>  
                    <finYrEndMin>""" + year_end_min + """</finYrEndMin>  
                    <incorpDtFrom>""" + date_from + """</incorpDtFrom> 
                    <incorpDtTo>""" + date_to + """</incorpDtTo> 
                    <netProfRangeMax>""" + profit_range_max + """</netProfRangeMax>  
                    <netProfRangeMin>""" + profit_range_min + """</netProfRangeMin> 
                    <packageType>""" + package_type + """</packageType>
                    <shareholderNat>""" + shareholder_nationality + """</shareholderNat> 
                </compListingCntReq>
            </request> 
        </lis:getCompListingCnt>
    </soapenv:Body> 
</soapenv:Envelope>"""
    
    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
    return middleware_response_json['soapenv:Envelope']['soapenv:Body']['lis:getCompListingCnt']['response']['getCompListingCntReturn']
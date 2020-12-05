import pytz

from datetime import datetime
from django.utils.timezone import make_aware

def state_mapping(temp_state):

    if temp_state == 'R':
        temp_state = 'PERLIS'
    elif temp_state == 'K':
        temp_state = 'KEDAH'
    elif temp_state == 'P':
        temp_state = 'PULAU PINANG'
    elif temp_state == 'D':
        temp_state = 'KELANTAN'
    elif temp_state == 'T':
        temp_state = 'TERENGGANU'
    elif temp_state == 'A':
        temp_state = 'PERAK'
    elif temp_state == 'B':
        temp_state = 'SELANGOR'
    elif temp_state == 'C':
        temp_state = 'PAHANG'
    elif temp_state == 'M':
        temp_state = 'MELAKA'
    elif temp_state == 'J':
        temp_state = 'JOHOR'
    elif temp_state == 'X':
        temp_state = 'SABAH'
    elif temp_state == 'N':
        temp_state = 'NEGERI SEMBILAN'        
    elif temp_state == 'Y':
        temp_state = 'SARAWAK'
    elif temp_state == 'L':
        temp_state = 'LABUAN'
    elif temp_state == 'W':
        temp_state = 'WILAYAH PERSEKUTUAN'
    elif temp_state == 'Q':
        temp_state = 'SINGAPURA'
    elif temp_state == 'U':
        temp_state = 'WILAYAH PERSEKUTUAN PUTRAJAYA'
    elif temp_state == 'F':
        temp_state = 'FOREIGN'
    elif temp_state == 'I':
        temp_state = 'INTERNET'
    elif temp_state == 'S':
        temp_state = 'SABAH'
    elif temp_state == 'E':
        temp_state = 'SARAWAK'
    
    return temp_state

def time_mapping(temp_time):

    date_format = '%-d-%m-%Y'
    time_zone = 'Asia/Kuala_Lumpur'

    temp_time = make_aware(datetime.strptime(temp_time, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_time = temp_time.astimezone(pytz.timezone(time_zone)).strftime(date_format)

    return temp_time

def time_mapping_aware(temp_time):

    date_format = '%-d %B %Y'
    time_zone = 'Asia/Kuala_Lumpur'

    temp_time = make_aware(datetime.strptime(temp_time, '%Y-%m-%dT%H:%M:%S.000Z'))
    temp_time = temp_time.astimezone(pytz.timezone(time_zone))

    return temp_time

def time_mapping_string(temp_time):

    date_format = '%-d %B %Y'
    time_zone = 'Asia/Kuala_Lumpur'

    temp_time = temp_time.strftime(date_format)

    return temp_time

def month_mapping(temp_month, lang):

    if lang == 'ms':
        if temp_month == 1:
            month_string = 'Januari'
        elif temp_month == 2:
            month_string = 'Februari'
        elif temp_month == 3:
            month_string = 'Mac'            
        elif temp_month == 4:
            month_string = 'April'            
        elif temp_month == 5:
            month_string = 'Mei'            
        elif temp_month == 6:
            month_string = 'Jun'            
        elif temp_month == 7:
            month_string = 'Julai'            
        elif temp_month == 8:
            month_string = 'Ogos'            
        elif temp_month == 9:
            month_string = 'September'            
        elif temp_month == 10:
            month_string = 'Oktober'            
        elif temp_month == 11:
            month_string = 'November'            
        elif temp_month == 12:
            month_string = 'Disember'  
    else:
        if temp_month == 1:
            month_string = 'January'
        elif temp_month == 2:
            month_string = 'February'
        elif temp_month == 3:
            month_string = 'March'            
        elif temp_month == 4:
            month_string = 'April'            
        elif temp_month == 5:
            month_string = 'May'            
        elif temp_month == 6:
            month_string = 'June'            
        elif temp_month == 7:
            month_string = 'July'            
        elif temp_month == 8:
            month_string = 'August'            
        elif temp_month == 9:
            month_string = 'September'            
        elif temp_month == 10:
            month_string = 'October'            
        elif temp_month == 11:
            month_string = 'November'            
        elif temp_month == 12:
            month_string = 'December'
    
    return month_string


def status_mapping(temp_status, lang):

    if temp_status == 'A' and lang == 'ms':
        temp_status = 'AKTIF'
    elif temp_status == 'L' and lang == 'ms':
        temp_status = 'LUPUT'
    elif temp_status == 'T' and lang == 'ms':
        temp_status = 'PENAMATAN'
    elif temp_status == 'B' and lang == 'ms':
        temp_status = 'BUBAR-PERTUKARAN KEPADA PERKONGSIAN LIALIBITI TERHAD (PLT)'
    elif temp_status == 'A' and lang == 'en':
        temp_status = 'ACTIVE'
    elif temp_status == 'L' and lang == 'en':
        temp_status = 'EXPIRED'
    elif temp_status == 'T' and lang == 'en':
        temp_status = 'TERMINATED'
    elif temp_status == 'B' and lang == 'en':
        temp_status = 'LLP CONVERSION'
    
    return temp_status

def status_biz_mapping(temp_status, lang):

    if temp_status == 'A' and lang == 'ms':
        temp_status = 'AKTIF'
    elif temp_status == 'L' and lang == 'ms':
        temp_status = 'LUPUT'
    elif temp_status == 'T' and lang == 'ms':
        temp_status = 'PENAMATAN'
    elif temp_status == 'B' and lang == 'ms':
        temp_status = 'BUBAR-PERTUKARAN KEPADA PERKONGSIAN LIALIBITI TERHAD (PLT)'
    elif temp_status == 'A' and lang == 'en':
        temp_status = 'ACTIVE'
    elif temp_status == 'L' and lang == 'en':
        temp_status = 'EXPIRED'
    elif temp_status == 'T' and lang == 'en':
        temp_status = 'TERMINATED'
    elif temp_status == 'B' and lang == 'en':
        temp_status = 'DISSOLVED-CONVERSION TO LIMITED LIABILITY PARTNERSHIP (LLP)'
    
    return temp_status

def race_mapping(temp_race, lang):

    if lang == 'ms':
        if temp_race == 'M':
            temp_race = 'MELAYU'
        elif temp_race == 'C':
            temp_race = 'CINA'
        elif temp_race == 'I':
            temp_race = 'INDIA'
        elif temp_race == 'R':
            temp_race = 'PERSENDIRIAN (SDN BHD)'
        elif temp_race == 'U':
            temp_race = 'UMUM (SYKT AWAM)'
        elif temp_race == 'F':
            temp_race = 'ASING'
        elif temp_race == 'S':
            temp_race = 'PERNIAGAAN'
        elif temp_race == 'A':
            temp_race = 'PERBADANAN'
        elif temp_race == 'K':
            temp_race = 'KADAZAN'
        elif temp_race == 'D':
            temp_race = 'DUSUN'
        elif temp_race == 'J':
            temp_race = 'BAJAU'
        elif temp_race == 'Y':
            temp_race = 'BIDAYUH'
        elif temp_race == 'T':
            temp_race = 'IBAN'
        elif temp_race == 'E':
            temp_race = 'MELANAU'
        elif temp_race == 'O':
            temp_race = 'LAIN-LAIN BANGSA'
        elif temp_race == 'N':
            temp_race = 'NATIVE'
        elif temp_race == 'B':
            temp_race = 'BUMIPUTERA SABAH'
        elif temp_race == 'W':
            temp_race = 'BUMIPUTERA SARAWAK'
    elif lang == 'en':
        if temp_race == 'M':
            temp_race = 'MALAY'
        elif temp_race == 'C':
            temp_race = 'CHINESE'
        elif temp_race == 'I':
            temp_race = 'INDIAN'
        elif temp_race == 'R':
            temp_race = 'PRIVATE (SDN BHD)'
        elif temp_race == 'U':
            temp_race = 'PUBLIC'
        elif temp_race == 'F':
            temp_race = 'FOREIGNER'
        elif temp_race == 'S':
            temp_race = 'BUSINESS'
        elif temp_race == 'A':
            temp_race = 'INCORPORATION'
        elif temp_race == 'K':
            temp_race = 'KADAZAN'
        elif temp_race == 'D':
            temp_race = 'DUSUN'
        elif temp_race == 'J':
            temp_race = 'BAJAU'
        elif temp_race == 'Y':
            temp_race = 'BIDAYUH'
        elif temp_race == 'T':
            temp_race = 'IBAN'
        elif temp_race == 'E':
            temp_race = 'MELANAU'
        elif temp_race == 'O':
            temp_race = 'OTHER RACE'
        elif temp_race == 'N':
            temp_race = 'NATIVE'
        elif temp_race == 'B':
            temp_race = 'BUMIPUTERA SABAH'
        elif temp_race == 'W':
            temp_race = 'BUMIPUTERA SARAWAK'
    
    return temp_race

def gender_mapping(temp_gender, lang):

    if temp_gender == 'L' and lang == 'en':
        temp_gender = 'MALE'
    elif temp_gender == 'P' and lang == 'en':
        temp_gender = 'FEMALE'
    elif temp_gender == 'L' and lang == 'ms':
        temp_gender = 'LELAKI'
    elif temp_gender == 'P' and lang == 'ms':
        temp_gender = 'PEREMPUAN'
    
    return temp_gender

def ammend_type_mapping(temp_ammend_type, lang):

    if temp_ammend_type == 'B' and lang == 'en':
        temp_ammend_type = 'NEW OWNER'
    elif temp_ammend_type == 'D' and lang == 'en':
        temp_ammend_type = 'PULL-OUT'
    elif temp_ammend_type == 'M' and lang == 'en':
        temp_ammend_type = 'DECEASED'
    elif temp_ammend_type == 'A' and lang == 'en':
        temp_ammend_type = 'ADDRESS UPDATE'
    elif temp_ammend_type == 'P' and lang == 'en':
        temp_ammend_type = 'OWNERSHIP CHANGES'
    elif temp_ammend_type == 'K' and lang == 'en':
        temp_ammend_type = 'ID CARD NUMBER CHANGES'
    elif temp_ammend_type == 'N' and lang == 'en':
        temp_ammend_type = 'OWNER NAME CHANGES'
    elif temp_ammend_type == 'S' and lang == 'en':
        temp_ammend_type = 'PARTNERSHIP DISSOLVE'
    elif temp_ammend_type == 'O' and lang == 'en':
        temp_ammend_type = 'COURT ORDER'
    elif temp_ammend_type == 'B' and lang == 'ms':
        temp_ammend_type = 'PEMILIK BARU'
    elif temp_ammend_type == 'D' and lang == 'ms':
        temp_ammend_type = 'TARIK DIRI'
    elif temp_ammend_type == 'M' and lang == 'ms':
        temp_ammend_type = 'KEMATIAN'
    elif temp_ammend_type == 'A' and lang == 'ms':
        temp_ammend_type = 'PERUBAHAN ALAMAT'
    elif temp_ammend_type == 'P' and lang == 'ms':
        temp_ammend_type = 'PERUBAHAN NAMA PEMILIK'
    elif temp_ammend_type == 'K' and lang == 'ms':
        temp_ammend_type = 'PERUBAHAN NO KP'
    elif temp_ammend_type == 'N' and lang == 'ms':
        temp_ammend_type = 'PERUBAHAN NAMA PEMILIK'
    elif temp_ammend_type == 'S' and lang == 'ms':
        temp_ammend_type = 'PEMBUBARAN PERKONGSIAN'
    elif temp_ammend_type == 'O' and lang == 'ms':
        temp_ammend_type = 'PERINTAH MAHKAMAH'
    
    return temp_ammend_type

def comp_status_mapping(temp_comp_status, lang):

    if temp_comp_status == 'R' and lang == 'en':
        temp_comp_status = 'PRIVATE LIMITED'
    elif temp_comp_status == 'U' and lang == 'en':
        temp_comp_status = 'PUBLIC LIMITED'
    elif temp_comp_status == 'R' and lang == 'ms':
        temp_comp_status = 'SYARIKAT PERSENDIRIAN'
    elif temp_comp_status == 'U' and lang == 'ms':
        temp_comp_status = 'SYARIKAT AWAM'

    return temp_comp_status

def comp_status_conversion_mapping(temp_comp_status, lang):

    if temp_comp_status == 'R' and lang == 'en':
        temp_comp_status = 'PRIVATE'
    elif temp_comp_status == 'U' and lang == 'en':
        temp_comp_status = 'PUBLIC'
    elif temp_comp_status == 'R' and lang == 'ms':
        temp_comp_status = 'PERSENDIRIAN'
    elif temp_comp_status == 'U' and lang == 'ms':
        temp_comp_status = 'AWAM'

    return temp_comp_status

def status_of_comp_mapping(temp_status_of_comp):

    if temp_status_of_comp == 'B':
        temp_status_of_comp = 'DISSOLVED CONVERSION TO LLP'
    elif temp_status_of_comp == 'C':
        temp_status_of_comp = 'CEASED BUSINESS'
    elif temp_status_of_comp == 'D':
        temp_status_of_comp = 'DISSOLVED'
    elif temp_status_of_comp == 'E':
        temp_status_of_comp = 'EXISTING'
    elif temp_status_of_comp == 'R':
        temp_status_of_comp = 'REMOVED'
    elif temp_status_of_comp == 'W':
        temp_status_of_comp = 'WINDING UP'
    elif temp_status_of_comp == 'X':
        temp_status_of_comp = 'NULL AND VOID BY COURT ORDER'
    elif temp_status_of_comp == 'Y':
        temp_status_of_comp = 'STRUCK-OFF & WINDING-UP VIA COURT ORDER'
    elif temp_status_of_comp == 'F':
        temp_status_of_comp = 'WINDING UP (UNDER SVA)'
    elif temp_status_of_comp == 'G':
        temp_status_of_comp = 'EXISTING UNDER JM (UNDER CVA)'
    elif temp_status_of_comp == 'V':
        temp_status_of_comp = 'EXISTING (UNDER CVS)'
    elif temp_status_of_comp == 'J':
        temp_status_of_comp = 'EXISTING (UNDER JM)'

    return temp_status_of_comp

def comp_type_mapping(temp_comp_type, lang):

    if temp_comp_type == 'B' and lang == 'en':
        temp_comp_type = 'LIMITED BY SHARE AND GUARANTEE'
    elif temp_comp_type == 'G' and lang == 'en':
        temp_comp_type = 'LIMITED BY GUARANTEE'
    elif temp_comp_type == 'S' and lang == 'en':
        temp_comp_type = 'LIMITED BY SHARES'
    elif temp_comp_type == 'U' and lang == 'en':
        temp_comp_type = 'UNLIMITED'
    elif temp_comp_type == 'B' and lang == 'ms':
        temp_comp_type = 'BERHAD MENURUT SAHAM DAN JAMINAN'
    elif temp_comp_type == 'G' and lang == 'ms':
        temp_comp_type = 'BERHAD MENURUT JAMINAN'
    elif temp_comp_type == 'S' and lang == 'ms':
        temp_comp_type = 'BERHAD MENURUT SYER'
    elif temp_comp_type == 'U' and lang == 'ms':
        temp_comp_type = 'TIDAK TERHAD'

    return temp_comp_type

def winding_up_mapping(wup_type):

    if wup_type == 'S':
        wup_type = 'EXISTING (STRIKING OFF IN PROCESS)'
        print(wup_type)
    else:
        wup_type = 'EXISTING'

    return wup_type

def origin_country_mapping(temp_origin):

    if temp_origin == 'ADE':
        temp_origin = 'ADEN'
    elif temp_origin == 'AFG':
        temp_origin = 'AFGHANISTAN'
    elif temp_origin == 'AGL':
        temp_origin = 'ANGUILLA'
    elif temp_origin == 'AZB':
        temp_origin = 'REPUBLIC OF AZERBAIJAN'
    elif temp_origin == 'NCD':
        temp_origin = 'NEW CALEDONIA'
    elif temp_origin == 'LVA':
        temp_origin = 'LATVIA'
    elif temp_origin == 'ALG':
        temp_origin = 'ALGERIA'
    elif temp_origin == 'ALM':
        temp_origin = 'ALMAIN'
    elif temp_origin == 'AND':
        temp_origin = 'ANDORRA'
    elif temp_origin == 'ANG':
        temp_origin = 'ANGOLA'
    elif temp_origin == 'ANT':
        temp_origin = 'ANTIGUA'
    elif temp_origin == 'ARG':
        temp_origin = 'ARGENTINA'
    elif temp_origin == 'ASA':
        temp_origin = 'AMERICAN SAMOA'
    elif temp_origin == 'AST':
        temp_origin = 'AUSTRIA'
    elif temp_origin == 'AUS':
        temp_origin = 'AUSTRALIA'
    elif temp_origin == 'AZO':
        temp_origin = 'AZORES'
    elif temp_origin == 'BAH':
        temp_origin = 'BAHRAIN'
    elif temp_origin == 'BAL':
        temp_origin = 'BELEARIC ISLAND'
    elif temp_origin == 'BAN':
        temp_origin = 'BANGLADESH'
    elif temp_origin == 'BAR':
        temp_origin = 'BARBADOS'
    elif temp_origin == 'BEL':
        temp_origin = 'BELGIUM'
    elif temp_origin == 'BER':
        temp_origin = 'BERMUDA'
    elif temp_origin == 'BHM':
        temp_origin = 'BAHAMAS'
    elif temp_origin == 'BIS':
        temp_origin = 'BISSAU'
    elif temp_origin == 'BOS':
        temp_origin = 'BOSNIA HERZOGOVINA'
    elif temp_origin == 'BOL':
        temp_origin = 'BOLIVIA'
    elif temp_origin == 'BRA':
        temp_origin = 'BRAZIL'
    elif temp_origin == 'BRU':
        temp_origin = 'BRUNEI'
    elif temp_origin == 'BUL':
        temp_origin = 'BULGARIA'
    elif temp_origin == 'BUR':
        temp_origin = 'MYAMMAR'
    elif temp_origin == 'BWI':
        temp_origin = 'BRITISH WEST INDIES'
    elif temp_origin == 'CAM':
        temp_origin = 'CAMERON'
    elif temp_origin == 'CAN':
        temp_origin = 'CANADA'
    elif temp_origin == 'CEU':
        temp_origin = 'CEUTA & MELLILA'
    elif temp_origin == 'CHA':
        temp_origin = 'CHAD'
    elif temp_origin == 'CHI':
        temp_origin = 'CHILE'
    elif temp_origin == 'CNI':
        temp_origin = 'CAYMAN ISLAND'
    elif temp_origin == 'CRA':
        temp_origin = 'COSTA RICA'
    elif temp_origin == 'CSI':
        temp_origin = 'CHRISTMAS ISLAND'
    elif temp_origin == 'CUB':
        temp_origin = 'CUBA'
    elif temp_origin == 'CVI':
        temp_origin = 'CAPE VERDE ISLAND'
    elif temp_origin == 'CYI':
        temp_origin = 'CANARY ISLAND'
    elif temp_origin == 'CYP':
        temp_origin = 'CYPRUS'
    elif temp_origin == 'CZE':
        temp_origin = 'CZECHOSLOVAKIA'
    elif temp_origin == 'DEN':
        temp_origin = 'DENMARK'
    elif temp_origin == 'DOM':
        temp_origin = 'COMMONWEALTH OF DOMINICA'
    elif temp_origin == 'DRK':
        temp_origin = 'KOREA (DEM. P.R)'
    elif temp_origin == 'EGY':
        temp_origin = 'EGYPT'
    elif temp_origin == 'EIR':
        temp_origin = 'EIRE'
    elif temp_origin == 'EQU':
        temp_origin = 'EQUADOR'
    elif temp_origin == 'ESR':
        temp_origin = 'EL SALVADOR'
    elif temp_origin == 'ETH':
        temp_origin = 'ETHIOPIA'
    elif temp_origin == 'FEI':
        temp_origin = 'FAEROE ISLAND'
    elif temp_origin == 'FII':
        temp_origin = 'FIJI ISLAND'
    elif temp_origin == 'FIN':
        temp_origin = 'FINLAND'
    elif temp_origin == 'FRA':
        temp_origin = 'FRANCE'
    elif temp_origin == 'FWI':
        temp_origin = 'FRENCH W. INDIES'
    elif temp_origin == 'GAB':
        temp_origin = 'GABON'
    elif temp_origin == 'GAM':
        temp_origin = 'GAMBIA'
    elif temp_origin == 'GER':
        temp_origin = 'GERMANY'
    elif temp_origin == 'GHA':
        temp_origin = 'GHANA'
    elif temp_origin == 'GIB':
        temp_origin = 'GIBRALTAR'
    elif temp_origin == 'GRA':
        temp_origin = 'GRANADA'
    elif temp_origin == 'GRE':
        temp_origin = 'GREECE'
    elif temp_origin == 'GTE':
        temp_origin = 'GUATEMALA'
    elif temp_origin == 'GUA':
        temp_origin = 'GUAM'
    elif temp_origin == 'GUI':
        temp_origin = 'GUINEA'
    elif temp_origin == 'GUY':
        temp_origin = 'GUYANA'
    elif temp_origin == 'HKG':
        temp_origin = 'HONG KONG'
    elif temp_origin == 'HON':
        temp_origin = 'HONDURAS'
    elif temp_origin == 'HUN':
        temp_origin = 'HUNGARY'
    elif temp_origin == 'ICE':
        temp_origin = 'ICELAND'
    elif temp_origin == 'INA':
        temp_origin = 'INDONESIA'
    elif temp_origin == 'IND':
        temp_origin = 'INDIA'
    elif temp_origin == 'IRN':
        temp_origin = 'IRAN'
    elif temp_origin == 'IRQ':
        temp_origin = 'IRAQ'
    elif temp_origin == 'ITA':
        temp_origin = 'ITALY'
    elif temp_origin == 'JAM':
        temp_origin = 'JAMAICA'
    elif temp_origin == 'JAP':
        temp_origin = 'JAPAN'
    elif temp_origin == 'JOR':
        temp_origin = 'JORDAN'
    elif temp_origin == 'KAM':
        temp_origin = 'KAMPUCHEA'
    elif temp_origin == 'KEN':
        temp_origin = 'KENYA'
    elif temp_origin == 'KUW':
        temp_origin = 'KUWAIT'
    elif temp_origin == 'LAO':
        temp_origin = 'LAOS'
    elif temp_origin == 'LEB':
        temp_origin = 'LEBANON'
    elif temp_origin == 'LIB':
        temp_origin = 'LIBERIA'
    elif temp_origin == 'LUX':
        temp_origin = 'LUXEMBORG'
    elif temp_origin == 'MAC':
        temp_origin = 'MACAO'
    elif temp_origin == 'MAD':
        temp_origin = 'MADERIA'
    elif temp_origin == 'IRL':
        temp_origin = 'IRELAND'
    elif temp_origin == 'MAL':
        temp_origin = 'MALAYSIA'
    elif temp_origin == 'MAU':
        temp_origin = 'MAURITANIA'
    elif temp_origin == 'MEX':
        temp_origin = 'MEXICO'
    elif temp_origin == 'MLI':
        temp_origin = 'MALI'
    elif temp_origin == 'MLT':
        temp_origin = 'MALTA'
    elif temp_origin == 'MLW':
        temp_origin = 'MALAWI'
    elif temp_origin == 'MON':
        temp_origin = 'MONTSERRAT'
    elif temp_origin == 'MOR':
        temp_origin = 'MOROCCO'
    elif temp_origin == 'MOZ':
        temp_origin = 'MOZAMBIQUE'
    elif temp_origin == 'MRT':
        temp_origin = 'MAURITIUS'
    elif temp_origin == 'MSI':
        temp_origin = 'MALDIVES ISLAND'
    elif temp_origin == 'NAU':
        temp_origin = 'NAURA'
    elif temp_origin == 'NEP':
        temp_origin = 'NEPAL'
    elif temp_origin == 'NET':
        temp_origin = 'NETHERLANDS'
    elif temp_origin == 'NGR':
        temp_origin = 'NIGER'
    elif temp_origin == 'NHS':
        temp_origin = 'NEW HEBRIDES'
    elif temp_origin == 'NIC':
        temp_origin = 'NICARAGUA'
    elif temp_origin == 'NIG':
        temp_origin = 'NIGERIA'
    elif temp_origin == 'NIU':
        temp_origin = 'NIUE'
    elif temp_origin == 'NKI':
        temp_origin = 'NORFOLD ISLAND'
    elif temp_origin == 'NOR':
        temp_origin = 'NORWAY'
    elif temp_origin == 'NWI':
        temp_origin = 'NETHERLANDS WI'
    elif temp_origin == 'NZD':
        temp_origin = 'NEW ZEALAND'
    elif temp_origin == 'OMA':
        temp_origin = 'OMAN'
    elif temp_origin == 'PAK':
        temp_origin = 'PAKISTAN'
    elif temp_origin == 'PAN':
        temp_origin = 'PANAMA'
    elif temp_origin == 'PAR':
        temp_origin = 'PARAGUAY'
    elif temp_origin == 'PER':
        temp_origin = 'PERU'
    elif temp_origin == 'PHI':
        temp_origin = 'PHILIPPINES'
    elif temp_origin == 'PLD':
        temp_origin = 'POLAND'
    elif temp_origin == 'PNG':
        temp_origin = 'PAPUA NEW GUINEA'
    elif temp_origin == 'POR':
        temp_origin = 'PORTUGAL'
    elif temp_origin == 'PRC':
        temp_origin = 'CHINA (PEOPLES REPUBLIC)'
    elif temp_origin == 'PUE':
        temp_origin = 'PUERTO RICO'
    elif temp_origin == 'RUM':
        temp_origin = 'RUMANIA'
    elif temp_origin == 'SAN':
        temp_origin = 'SANAA (YEMEN ARAB REPUBLIC)'
    elif temp_origin == 'SAU':
        temp_origin = 'SAUDIA ARABIA'
    elif temp_origin == 'SEN':
        temp_origin = 'SENEGAL'
    elif temp_origin == 'SEY':
        temp_origin = 'SEYCHELLES'
    elif temp_origin == 'SIA':
        temp_origin = 'ST. LUCIA'
    elif temp_origin == 'SIN':
        temp_origin = 'SINGAPORE'
    elif temp_origin == 'SKA':
        temp_origin = 'ST. KITTA'
    elif temp_origin == 'ALB':
        temp_origin = 'ALBANIA'
    elif temp_origin == 'SNI':
        temp_origin = 'SOLOMON ISLAND'
    elif temp_origin == 'SOK':
        temp_origin = 'KOREA SOUTH'
    elif temp_origin == 'SOM':
        temp_origin = 'SOMALIA'
    elif temp_origin == 'SPA':
        temp_origin = 'SPAIN'
    elif temp_origin == 'SRI':
        temp_origin = 'SRI LANKA'
    elif temp_origin == 'STP':
        temp_origin = 'ST. THOME & PRINCIPTE'
    elif temp_origin == 'SUD':
        temp_origin = 'SUDAN'
    elif temp_origin == 'SVT':
        temp_origin = 'ST. VINCENT'
    elif temp_origin == 'SWE':
        temp_origin = 'SWEDEN'
    elif temp_origin == 'SWI':
        temp_origin = 'SWITZERLAND'
    elif temp_origin == 'TAH':
        temp_origin = 'TAHITI'
    elif temp_origin == 'TAR':
        temp_origin = 'TANGIER'
    elif temp_origin == 'THA':
        temp_origin = 'THAILAND'
    elif temp_origin == 'TON':
        temp_origin = 'TONGUA'
    elif temp_origin == 'TSI':
        temp_origin = 'TURKS ISLAND'
    elif temp_origin == 'TTO':
        temp_origin = 'TRINIDAD & TABAGO'
    elif temp_origin == 'TUN':
        temp_origin = 'TUNISIA'
    elif temp_origin == 'TUR':
        temp_origin = 'TURKEY'
    elif temp_origin == 'UAE':
        temp_origin = 'UNITED ARAB EMIRATES'
    elif temp_origin == 'UGA':
        temp_origin = 'UGANDA'
    elif temp_origin == 'UKG':
        temp_origin = 'UNITED KINGDOM'
    elif temp_origin == 'URU':
        temp_origin = 'URUGUAY'
    elif temp_origin == 'USA':
        temp_origin = 'UNITED STATES OF AMERICA'
    elif temp_origin == 'USR':
        temp_origin = 'U.S.S.R.'
    elif temp_origin == 'UVA':
        temp_origin = 'UPPER VOLTA'
    elif temp_origin == 'VAT':
        temp_origin = 'VATICAN CITY'
    elif temp_origin == 'VEN':
        temp_origin = 'VENEZUELA'
    elif temp_origin == 'VIB':
        temp_origin = 'VIRGIN ISLAND (BRI)'
    elif temp_origin == 'VIE':
        temp_origin = 'VIETNAM'
    elif temp_origin == 'VIU':
        temp_origin = 'VIRGIN ISLAND (US)'
    elif temp_origin == 'WSA':
        temp_origin = 'WESTERN SAMOA'
    elif temp_origin == 'YUG':
        temp_origin = 'YUGOSLAVIA'
    elif temp_origin == 'ZAI':
        temp_origin = 'ZAIRE'
    elif temp_origin == 'ZAM':
        temp_origin = 'ZAMBIA'
    elif temp_origin == 'ZIM':
        temp_origin = 'ZIMBABWE'
    elif temp_origin == 'KOR':
        temp_origin = 'SOUTH KOREA'
    elif temp_origin == 'IOM':
        temp_origin = 'ISLE OF MAN,BRITAIN'
    elif temp_origin == 'TAI':
        temp_origin = 'TAIWAN'
    elif temp_origin == 'SCO':
        temp_origin = 'SCOTLAND'
    elif temp_origin == 'AFR':
        temp_origin = 'AFRICA'
    elif temp_origin == 'SAF':
        temp_origin = 'SOUTH AFRICA'
    elif temp_origin == 'BVI':
        temp_origin = 'BRITISH VIRGIN ISLANDS'
    elif temp_origin == 'YAM':
        temp_origin = 'YAMAN'
    elif temp_origin == 'LIA':
        temp_origin = 'LIBYA'
    elif temp_origin == 'SYR':
        temp_origin = 'SYRIA'
    elif temp_origin == 'CRO':
        temp_origin = 'CROATIA'
    elif temp_origin == 'UBK':
        temp_origin = 'UZBEKISTAN'
    elif temp_origin == 'CON':
        temp_origin = 'REPUBLIC OF CONGO'
    elif temp_origin == 'KIR':
        temp_origin = 'REP. OF KIRIBATI'
    elif temp_origin == 'COL':
        temp_origin = 'REPUBLIC OF COLOMBIA'
    elif temp_origin == 'TAJ':
        temp_origin = 'REPUBLIK TAJIKISTAN'
    elif temp_origin == 'LCH':
        temp_origin = 'LIECHTENSTEIN'
    elif temp_origin == 'REB':
        temp_origin = 'REPUBLIC OF BELARUS'
    elif temp_origin == 'PSE':
        temp_origin = 'PALESTINE'
    elif temp_origin == 'QAT':
        temp_origin = 'QATAR'
    elif temp_origin == 'KZT':
        temp_origin = 'KAZAKHSTAN'
    elif temp_origin == 'BLZ':
        temp_origin = 'BELIZE'
    
    return temp_origin

def officer_designation_mapping(temp_designation):

    if temp_designation == 'Q':
        temp_designation = 'ALT DIRECTOR'
    elif temp_designation == 'D':
        temp_designation = 'DIRECTOR'
    elif temp_designation == 'M':
        temp_designation = 'MANAGER'
    elif temp_designation == 'S':
        temp_designation = 'SECRETARY'
    elif temp_designation == 'A':
        temp_designation = 'AGENT'
    elif temp_designation == 'P':
        temp_designation = 'SUBSCRIBER'
    elif temp_designation == 'L':
        temp_designation = 'LIQUIDATOR'
    elif temp_designation == 'R':
        temp_designation = 'RECEIVER'
    elif temp_designation == 'T':
        temp_designation = 'AUTH PERSON'
    elif temp_designation == 'O':
        temp_designation = 'OWNER'
    elif temp_designation == 'V':
        temp_designation = 'PROVISIONAL LIQUIDATOR'

    return temp_designation

def branch_code(branch_code):

    if branch_code == 'CT':
        branch_name = 'TEMERLOH'
    elif branch_code == 'MP':
        branch_name = 'MAJLIS PERBANDARAN SELAYANG'
    elif branch_code == 'AS':
        branch_name = 'ALOR SETAR'
    elif branch_code == 'PG':
        branch_name = 'SEBERANG JAYA, PULAU PINANG'
    elif branch_code == 'IP':
        branch_name = 'IPOH'
    elif branch_code == 'SA':
        branch_name = 'SHAH ALAM'
    elif branch_code == 'MA':
        branch_name = 'MELAKA BANDARAYA BERSEJARAH'
    elif branch_code == 'JM':
        branch_name = 'JOHOR BAHRU'
    elif branch_code == 'KT':
        branch_name = 'KOTA BHARU'
    elif branch_code == 'TR':
        branch_name = 'KUALA TERENGGANU'
    elif branch_code == 'CA':
        branch_name = 'KUANTAN'
    elif branch_code == 'KL':
        branch_name = 'KUALA LUMPUR'
    elif branch_code == 'LA':
        branch_name = 'W.P. LABUAN'
    elif branch_code == 'RA':
        branch_name = 'KANGAR'
    elif branch_code == 'NS':
        branch_name = 'SEREMBAN'
    elif branch_code == 'MR':
        branch_name = 'MIRI'
    elif branch_code == 'KV':
        branch_name = 'LANGKAWI'
    elif branch_code == 'RC':
        branch_name = 'PERLIS'
    elif branch_code == 'JR':
        branch_name = 'MUAR'
    elif branch_code == 'JC':
        branch_name = 'JOHOR'
    elif branch_code == 'KC':
        branch_name = 'KEDAH'
    elif branch_code == 'PC':
        branch_name = 'PULAU PINANG'
    elif branch_code == 'AC':
        branch_name = 'PERAK'
    elif branch_code == 'BC':
        branch_name = 'SELANGOR'
    elif branch_code == 'NC':
        branch_name = 'NEGERI SEMBILAN'
    elif branch_code == 'MC':
        branch_name = 'MELAKA'
    elif branch_code == 'CC':
        branch_name = 'PAHANG'
    elif branch_code == 'TC':
        branch_name = 'TERENGGANU'
    elif branch_code == 'DC':
        branch_name = 'KELANTAN'
    elif branch_code == 'SW':
        branch_name = 'KUCHING'
    elif branch_code == 'SB':
        branch_name = 'KOTA KINABALU'
    elif branch_code == 'KP':
        branch_name = 'KL PUTRA'
    elif branch_code == 'DB':
        branch_name = 'DEWAN BANDARAYA KUALA LUMPUR'
    elif branch_code == 'KD':
        branch_name = 'KPDNKK PUTRAJAYA'
    elif branch_code == 'EL':
        branch_name = 'KUALA LUMPUR'
    elif branch_code == 'TW':
        branch_name = 'TAWAU'
    elif branch_code == 'IT':
        branch_name = 'K. LUMPUR'
    elif branch_code == 'IU':
        branch_name = 'INACTIVE USERS'
    elif branch_code == 'MY':
        branch_name = 'MYCOID'
    elif branch_code == 'UT':
        branch_name = 'UTC MELAKA'
    elif branch_code == 'UP':
        branch_name = 'UTC PUDU SENTRAL'
    elif branch_code == 'UK':
        branch_name = 'UTC PAHANG'
    elif branch_code == 'UA':
        branch_name = 'UTC ALOR SETAR'
    elif branch_code == 'MB':
        branch_name = 'SISTEM EZBIZ'
    elif branch_code == 'YC':
        branch_name = 'CYBERJAYA'
    elif branch_code == 'SI':
        branch_name = 'SIBU'
    elif branch_code == 'XB':
        branch_name = 'XBRL'
    elif branch_code == 'BR':
        branch_name = 'BANK RAKYAT'
    elif branch_code == 'BS':
        branch_name = 'BSN'
    elif branch_code == 'MY':
        # repeatative coding
        branch_name = 'KUALA LUMPUR'
    else:
        branch_name = 'KUALA LUMPUR'

    return branch_name

def charge_code(charge_code):

    if charge_code == 'S':
        charge_name = 'FULLY SATISFIED'
    elif charge_code == 'P':
        charge_name = 'PARTLY SATISFIED'    
    elif charge_code == 'R':
        charge_name = 'FULLY RELEASED'        
    elif charge_code == 'Q':
        charge_name = 'PARTLY RELEASED'
    elif charge_code == 'U':
        charge_name = 'UNSATISFIED'    
    elif charge_code == 'B':
        charge_name = 'CANCELLATION'    
    elif charge_code == 'C':
        charge_name = 'FULLY CEASED'   

    return charge_name

def charge_type(charge_code):

    if charge_code == 'C':
        charge_type_ = 'FIXED'
    elif charge_code == 'D':
        charge_type_ = 'FLOATING'
    elif charge_code == 'X':
        charge_type_ = 'FIXED AND FLOATING'
    elif charge_code == 'E':
        charge_type_ = 'EQUITABLE'
    elif charge_code == 'O':
        charge_type_ = 'FIXED AND/OR FLOATING'

    return charge_type_

def nationality_code(nationality_code, lang):

    if nationality_code == 'MAL' and lang == 'ms':
        nationality = 'WARGANEGARA MALAYSIA'
    elif nationality_code == 'MAL' and lang == 'en':
        nationality = 'MALAYSIAN CITIZEN'
    elif nationality_code == 'PMR' and lang == 'ms':
        nationality = 'PENDUDUK TETAP'
    elif nationality_code == 'PMR' and lang == 'en':
        nationality = 'PERMANENT RESIDENT'
    elif nationality_code == 'AZB' and lang == 'ms':
        nationality = 'WARGANEGARA REPUBLIC OF AZERBAIJAN'
    elif nationality_code == 'AZB' and lang == 'en':
        nationality = 'REPUBLIC OF AZERBAIJAN CITIZEN'
    elif nationality_code == 'ADE' and lang == 'ms':
        nationality = 'WARGANEGARA ADEN'
    elif nationality_code == 'ADE' and lang == 'en':
        nationality = 'ADEN CITIZEN'
    elif nationality_code == 'AFG' and lang == 'ms':
        nationality = 'WARGANEGARA AFGHANISTAN'
    elif nationality_code == 'AFG' and lang == 'en':
        nationality = 'AFGHANISTAN CITIZEN'
    elif nationality_code == 'AGL' and lang == 'ms':
        nationality = 'WARGANEGARA ANGUILLA'
    elif nationality_code == 'AGL' and lang == 'en':
        nationality = 'ANGUILLA CITIZEN'
    elif nationality_code == 'ALG' and lang == 'ms':
        nationality = 'WARGANEGARA ALGERIA'
    elif nationality_code == 'ALG' and lang == 'en':
        nationality = 'ALGERIA CITIZEN'
    elif nationality_code == 'ALM' and lang == 'ms':
        nationality = 'WARGANEGARA ALMAIN'
    elif nationality_code == 'ALM' and lang == 'en':
        nationality = 'ALMAIN CITIZEN'
    elif nationality_code == 'AND' and lang == 'ms':
        nationality = 'WARGANEGARA ANDORRA'
    elif nationality_code == 'AND' and lang == 'en':
        nationality = 'ANDORRA CITIZEN'
    elif nationality_code == 'ANG' and lang == 'ms':
        nationality = 'WARGANEGARA ANGOLA'
    elif nationality_code == 'ANG' and lang == 'en':
        nationality = 'ANGOLA CITIZEN'
    elif nationality_code == 'ANT' and lang == 'ms':
        nationality = 'WARGANEGARA ANTIGUA'
    elif nationality_code == 'ANT' and lang == 'en':
        nationality = 'ANTIGUA CITIZEN'
    elif nationality_code == 'ARG' and lang == 'ms':
        nationality = 'WARGANEGARA ARGENTINA'
    elif nationality_code == 'ARG' and lang == 'en':
        nationality = 'ARGENTINA CITIZEN'
    elif nationality_code == 'ASA' and lang == 'ms':
        nationality = 'WARGANEGARA AMERICAN SAMOA'
    elif nationality_code == 'ASA' and lang == 'en':
        nationality = 'AMERICAN SAMOA CITIZEN'
    elif nationality_code == 'AST' and lang == 'ms':
        nationality = 'WARGANEGARA AUSTRIA'
    elif nationality_code == 'AST' and lang == 'en':
        nationality = 'AUSTRIA CITIZEN'
    elif nationality_code == 'AUS' and lang == 'ms':
        nationality = 'WARGANEGARA AUSTRALIA'
    elif nationality_code == 'AUS' and lang == 'en':
        nationality = 'AUSTRALIA CITIZEN'
    elif nationality_code == 'AZO' and lang == 'ms':
        nationality = 'WARGANEGARA AZORES'
    elif nationality_code == 'AZO' and lang == 'en':
        nationality = 'AZORES CITIZEN'
    elif nationality_code == 'BAH' and lang == 'ms':
        nationality = 'WARGANEGARA BAHRAIN'
    elif nationality_code == 'BAH' and lang == 'en':
        nationality = 'BAHRAIN CITIZEN'
    elif nationality_code == 'BAL' and lang == 'ms':
        nationality = 'WARGANEGARA BELEARIC ISLAN '
    elif nationality_code == 'BAL' and lang == 'en':
        nationality = 'BELEARIC ISLAND CITIZEN'
    elif nationality_code == 'BAN' and lang == 'ms':
        nationality = 'WARGANEGARA BANGLADESH'
    elif nationality_code == 'BAN' and lang == 'en':
        nationality = 'BANGLADESH CITIZEN'
    elif nationality_code == 'BAR' and lang == 'ms':
        nationality = 'WARGANEGARA BARBADOS'
    elif nationality_code == 'BAR' and lang == 'en':
        nationality = 'BARBADOS CITIZEN'
    elif nationality_code == 'BBB' and lang == 'ms':
        nationality = 'WARGANEGARA BANGSA-BANGSA ERSATU '
    elif nationality_code == 'BBB' and lang == 'en':
        nationality = 'BANGSA-BANGSA BERSATU CITIZEN'
    elif nationality_code == 'BEL' and lang == 'ms':
        nationality = 'WARGANEGARA BELGIUM'
    elif nationality_code == 'BEL' and lang == 'en':
        nationality = 'BELGIUM CITIZEN'
    elif nationality_code == 'BER' and lang == 'ms':
        nationality = 'WARGANEGARA BERMUDA'
    elif nationality_code == 'BER' and lang == 'en':
        nationality = 'BERMUDA CITIZEN'
    elif nationality_code == 'BHM' and lang == 'ms':
        nationality = 'WARGANEGARA BAHAMAS'
    elif nationality_code == 'BHM' and lang == 'en':
        nationality = 'BAHAMAS CITIZEN'
    elif nationality_code == 'BIS' and lang == 'ms':
        nationality = 'WARGANEGARA BISSAU'
    elif nationality_code == 'BIS' and lang == 'en':
        nationality = 'BISSAU CITIZEN'
    elif nationality_code == 'BOS' and lang == 'ms':
        nationality = 'WARGANEGARA BOSNIA HERZOGOINA '
    elif nationality_code == 'BOS' and lang == 'en':
        nationality = 'BOSNIA HERZOGOVINA CITIZEN'
    elif nationality_code == 'BOL' and lang == 'ms':
        nationality = 'WARGANEGARA BOLIVIA'
    elif nationality_code == 'BOL' and lang == 'en':
        nationality = 'BOLIVIA CITIZEN'
    elif nationality_code == 'BRA' and lang == 'ms':
        nationality = 'WARGANEGARA BRAZIL'
    elif nationality_code == 'BRA' and lang == 'en':
        nationality = 'BRAZIL CITIZEN'
    elif nationality_code == 'BRU' and lang == 'ms':
        nationality = 'WARGANEGARA BRUNEI'
    elif nationality_code == 'BRU' and lang == 'en':
        nationality = 'BRUNEI CITIZEN'
    elif nationality_code == 'BUL' and lang == 'ms':
        nationality = 'WARGANEGARA BULGARIA'
    elif nationality_code == 'BUL' and lang == 'en':
        nationality = 'BULGARIA CITIZEN'
    elif nationality_code == 'BUR' and lang == 'ms':
        nationality = 'WARGANEGARA MYAMMAR'
    elif nationality_code == 'BUR' and lang == 'en':
        nationality = 'MYAMMAR CITIZEN'
    elif nationality_code == 'BWI' and lang == 'ms':
        nationality = 'WARGANEGARA BRITISH WEST IDIES '
    elif nationality_code == 'BWI' and lang == 'en':
        nationality = 'BRITISH WEST INDIES CITIZEN'
    elif nationality_code == 'CAM' and lang == 'ms':
        nationality = 'WARGANEGARA CAMERON'
    elif nationality_code == 'CAM' and lang == 'en':
        nationality = 'CAMERON CITIZEN'
    elif nationality_code == 'CAN' and lang == 'ms':
        nationality = 'WARGANEGARA CANADA'
    elif nationality_code == 'CAN' and lang == 'en':
        nationality = 'CANADA CITIZEN'
    elif nationality_code == 'CEU' and lang == 'ms':
        nationality = 'WARGANEGARA CEUTA & MELLIL '
    elif nationality_code == 'CEU' and lang == 'en':
        nationality = 'CEUTA & MELLILA CITIZEN'
    elif nationality_code == 'CHA' and lang == 'ms':
        nationality = 'WARGANEGARA CHAD'
    elif nationality_code == 'CHA' and lang == 'en':
        nationality = 'CHAD CITIZEN'
    elif nationality_code == 'CHI' and lang == 'ms':
        nationality = 'WARGANEGARA CHILE'
    elif nationality_code == 'CHI' and lang == 'en':
        nationality = 'CHILE CITIZEN'
    elif nationality_code == 'CNI' and lang == 'ms':
        nationality = 'WARGANEGARA CAYMAN ISLAND'
    elif nationality_code == 'CNI' and lang == 'en':
        nationality = 'CAYMAN ISLAND CITIZEN'
    elif nationality_code == 'CRA' and lang == 'ms':
        nationality = 'WARGANEGARA COSTA RICA'
    elif nationality_code == 'CRA' and lang == 'en':
        nationality = 'COSTA RICA CITIZEN'
    elif nationality_code == 'CSI' and lang == 'ms':
        nationality = 'WARGANEGARA CHRISTMAS ISLAD '
    elif nationality_code == 'CSI' and lang == 'en':
        nationality = 'CHRISTMAS ISLAND CITIZEN'
    elif nationality_code == 'CUB' and lang == 'ms':
        nationality = 'WARGANEGARA CUBA'
    elif nationality_code == 'CUB' and lang == 'en':
        nationality = 'CUBA CITIZEN'
    elif nationality_code == 'CVI' and lang == 'ms':
        nationality = 'WARGANEGARA CAPE VERDE ISLND '
    elif nationality_code == 'CVI' and lang == 'en':
        nationality = 'CAPE VERDE ISLAND CITIZEN'
    elif nationality_code == 'CYI' and lang == 'ms':
        nationality = 'WARGANEGARA CANARY ISLAND'
    elif nationality_code == 'CYI' and lang == 'en':
        nationality = 'CANARY ISLAND CITIZEN'
    elif nationality_code == 'CYP' and lang == 'ms':
        nationality = 'WARGANEGARA CYPRUS'
    elif nationality_code == 'CYP' and lang == 'en':
        nationality = 'CYPRUS CITIZEN'
    elif nationality_code == 'CZE' and lang == 'ms':
        nationality = 'WARGANEGARA CZECHOSLOVAKIA'
    elif nationality_code == 'CZE' and lang == 'en':
        nationality = 'CZECHOSLOVAKIA CITIZEN'
    elif nationality_code == 'DEN' and lang == 'ms':
        nationality = 'WARGANEGARA DENMARK'
    elif nationality_code == 'DEN' and lang == 'en':
        nationality = 'DENMARK CITIZEN'
    elif nationality_code == 'DOM' and lang == 'ms':
        nationality = 'WARGANEGARA COMMONWEALTH O DOMINICA '
    elif nationality_code == 'DOM' and lang == 'en':
        nationality = 'COMMONWEALTH OF DOMINICA CITIZEN'
    elif nationality_code == 'DRK' and lang == 'ms':
        nationality = 'WARGANEGARA KOREA (DEM. P.) '
    elif nationality_code == 'DRK' and lang == 'en':
        nationality = 'KOREA (DEM. P.R) CITIZEN'
    elif nationality_code == 'EGY' and lang == 'ms':
        nationality = 'WARGANEGARA EGYPT'
    elif nationality_code == 'EGY' and lang == 'en':
        nationality = 'EGYPT CITIZEN'
    elif nationality_code == 'EIR' and lang == 'ms':
        nationality = 'WARGANEGARA EIRE'
    elif nationality_code == 'EIR' and lang == 'en':
        nationality = 'EIRE CITIZEN'
    elif nationality_code == 'EQU' and lang == 'ms':
        nationality = 'WARGANEGARA EQUADOR'
    elif nationality_code == 'EQU' and lang == 'en':
        nationality = 'EQUADOR CITIZEN'
    elif nationality_code == 'ESR' and lang == 'ms':
        nationality = 'WARGANEGARA EL SALVADOR'
    elif nationality_code == 'ESR' and lang == 'en':
        nationality = 'EL SALVADOR CITIZEN'
    elif nationality_code == 'ETH' and lang == 'ms':
        nationality = 'WARGANEGARA ETHIOPIA'
    elif nationality_code == 'ETH' and lang == 'en':
        nationality = 'ETHIOPIA CITIZEN'
    elif nationality_code == 'FEI' and lang == 'ms':
        nationality = 'WARGANEGARA FAEROE ISLAND'
    elif nationality_code == 'FEI' and lang == 'en':
        nationality = 'FAEROE ISLAND CITIZEN'
    elif nationality_code == 'FII' and lang == 'ms':
        nationality = 'WARGANEGARA FIJI ISLAND'
    elif nationality_code == 'FII' and lang == 'en':
        nationality = 'FIJI ISLAND CITIZEN'
    elif nationality_code == 'FIN' and lang == 'ms':
        nationality = 'WARGANEGARA FINLAND'
    elif nationality_code == 'FIN' and lang == 'en':
        nationality = 'FINLAND CITIZEN'
    elif nationality_code == 'FRA' and lang == 'ms':
        nationality = 'WARGANEGARA FRANCE'
    elif nationality_code == 'FRA' and lang == 'en':
        nationality = 'FRANCE CITIZEN'
    elif nationality_code == 'FWI' and lang == 'ms':
        nationality = 'WARGANEGARA FRENCH W. INDIS '
    elif nationality_code == 'FWI' and lang == 'en':
        nationality = 'FRENCH W. INDIES CITIZEN'
    elif nationality_code == 'GAB' and lang == 'ms':
        nationality = 'WARGANEGARA GABON'
    elif nationality_code == 'GAB' and lang == 'en':
        nationality = 'GABON CITIZEN'
    elif nationality_code == 'GAM' and lang == 'ms':
        nationality = 'WARGANEGARA GAMBIA'
    elif nationality_code == 'GAM' and lang == 'en':
        nationality = 'GAMBIA CITIZEN'
    elif nationality_code == 'GER' and lang == 'ms':
        nationality = 'WARGANEGARA GERMANY (WEST)'
    elif nationality_code == 'GER' and lang == 'en':
        nationality = 'GERMANY (WEST) CITIZEN'
    elif nationality_code == 'GHA' and lang == 'ms':
        nationality = 'WARGANEGARA GHANA'
    elif nationality_code == 'GHA' and lang == 'en':
        nationality = 'GHANA CITIZEN'
    elif nationality_code == 'GIB' and lang == 'ms':
        nationality = 'WARGANEGARA GIBRALTAR'
    elif nationality_code == 'GIB' and lang == 'en':
        nationality = 'GIBRALTAR CITIZEN'
    elif nationality_code == 'GRA' and lang == 'ms':
        nationality = 'WARGANEGARA GRANADA'
    elif nationality_code == 'GRA' and lang == 'en':
        nationality = 'GRANADA CITIZEN'
    elif nationality_code == 'GRE' and lang == 'ms':
        nationality = 'WARGANEGARA GREECE'
    elif nationality_code == 'GRE' and lang == 'en':
        nationality = 'GREECE CITIZEN'
    elif nationality_code == 'GTE' and lang == 'ms':
        nationality = 'WARGANEGARA GUATEMALA'
    elif nationality_code == 'GTE' and lang == 'en':
        nationality = 'GUATEMALA CITIZEN'
    elif nationality_code == 'GUA' and lang == 'ms':
        nationality = 'WARGANEGARA GUAM'
    elif nationality_code == 'GUA' and lang == 'en':
        nationality = 'GUAM CITIZEN'
    elif nationality_code == 'GUI' and lang == 'ms':
        nationality = 'WARGANEGARA GUINEA'
    elif nationality_code == 'GUI' and lang == 'en':
        nationality = 'GUINEA CITIZEN'
    elif nationality_code == 'GUY' and lang == 'ms':
        nationality = 'WARGANEGARA GUYANA'
    elif nationality_code == 'GUY' and lang == 'en':
        nationality = 'GUYANA CITIZEN'
    elif nationality_code == 'HKG' and lang == 'ms':
        nationality = 'WARGANEGARA HONG KONG'
    elif nationality_code == 'HKG' and lang == 'en':
        nationality = 'HONG KONG CITIZEN'
    elif nationality_code == 'HON' and lang == 'ms':
        nationality = 'WARGANEGARA HONDURAS'
    elif nationality_code == 'HON' and lang == 'en':
        nationality = 'HONDURAS CITIZEN'
    elif nationality_code == 'HUN' and lang == 'ms':
        nationality = 'WARGANEGARA HUNGARY'
    elif nationality_code == 'HUN' and lang == 'en':
        nationality = 'HUNGARY CITIZEN'
    elif nationality_code == 'ICE' and lang == 'ms':
        nationality = 'WARGANEGARA ICELAND'
    elif nationality_code == 'ICE' and lang == 'en':
        nationality = 'ICELAND CITIZEN'
    elif nationality_code == 'INA' and lang == 'ms':
        nationality = 'WARGANEGARA INDONESIA'
    elif nationality_code == 'INA' and lang == 'en':
        nationality = 'INDONESIA CITIZEN'
    elif nationality_code == 'IND' and lang == 'ms':
        nationality = 'WARGANEGARA INDIA'
    elif nationality_code == 'IND' and lang == 'en':
        nationality = 'INDIA CITIZEN'
    elif nationality_code == 'IRN' and lang == 'ms':
        nationality = 'WARGANEGARA IRAN'
    elif nationality_code == 'IRN' and lang == 'en':
        nationality = 'IRAN CITIZEN'
    elif nationality_code == 'IRQ' and lang == 'ms':
        nationality = 'WARGANEGARA IRAQ'
    elif nationality_code == 'IRQ' and lang == 'en':
        nationality = 'IRAQ CITIZEN'
    elif nationality_code == 'ISR' and lang == 'ms':
        nationality = 'WARGANEGARA ISRAEL'
    elif nationality_code == 'ISR' and lang == 'en':
        nationality = 'ISRAEL CITIZEN'
    elif nationality_code == 'ITA' and lang == 'ms':
        nationality = 'WARGANEGARA ITALY'
    elif nationality_code == 'ITA' and lang == 'en':
        nationality = 'ITALY CITIZEN'
    elif nationality_code == 'JAM' and lang == 'ms':
        nationality = 'WARGANEGARA JAMAICA'
    elif nationality_code == 'JAM' and lang == 'en':
        nationality = 'JAMAICA CITIZEN'
    elif nationality_code == 'JAP' and lang == 'ms':
        nationality = 'WARGANEGARA JAPAN'
    elif nationality_code == 'JAP' and lang == 'en':
        nationality = 'JAPAN CITIZEN'
    elif nationality_code == 'JOR' and lang == 'ms':
        nationality = 'WARGANEGARA JORDAN'
    elif nationality_code == 'JOR' and lang == 'en':
        nationality = 'JORDAN CITIZEN'
    elif nationality_code == 'KAM' and lang == 'ms':
        nationality = 'WARGANEGARA KAMPUCHEA'
    elif nationality_code == 'KAM' and lang == 'en':
        nationality = 'KAMPUCHEA CITIZEN'
    elif nationality_code == 'KEN' and lang == 'ms':
        nationality = 'WARGANEGARA KENYA'
    elif nationality_code == 'KEN' and lang == 'en':
        nationality = 'KENYA CITIZEN'
    elif nationality_code == 'KUW' and lang == 'ms':
        nationality = 'WARGANEGARA KUWAIT'
    elif nationality_code == 'KUW' and lang == 'en':
        nationality = 'KUWAIT CITIZEN'
    elif nationality_code == 'LAO' and lang == 'ms':
        nationality = 'WARGANEGARA LAOS'
    elif nationality_code == 'LAO' and lang == 'en':
        nationality = 'LAOS CITIZEN'
    elif nationality_code == 'LEB' and lang == 'ms':
        nationality = 'WARGANEGARA LEBANON'
    elif nationality_code == 'LEB' and lang == 'en':
        nationality = 'LEBANON CITIZEN'
    elif nationality_code == 'LIB' and lang == 'ms':
        nationality = 'WARGANEGARA LIBERIA'
    elif nationality_code == 'LIB' and lang == 'en':
        nationality = 'LIBERIA CITIZEN'
    elif nationality_code == 'LUX' and lang == 'ms':
        nationality = 'WARGANEGARA LUXEMBORG'
    elif nationality_code == 'LUX' and lang == 'en':
        nationality = 'LUXEMBORG CITIZEN'
    elif nationality_code == 'MAC' and lang == 'ms':
        nationality = 'WARGANEGARA MACAO'
    elif nationality_code == 'MAC' and lang == 'en':
        nationality = 'MACAO CITIZEN'
    elif nationality_code == 'MAD' and lang == 'ms':
        nationality = 'WARGANEGARA MADERIA'
    elif nationality_code == 'MAD' and lang == 'en':
        nationality = 'MADERIA CITIZEN'
    elif nationality_code == 'IRL' and lang == 'ms':
        nationality = 'WARGANEGARA IRELAND'
    elif nationality_code == 'IRL' and lang == 'en':
        nationality = 'IRELAND CITIZEN'
    elif nationality_code == 'MAU' and lang == 'ms':
        nationality = 'WARGANEGARA MAURITANIA'
    elif nationality_code == 'MAU' and lang == 'en':
        nationality = 'MAURITANIA CITIZEN'
    elif nationality_code == 'MEX' and lang == 'ms':
        nationality = 'WARGANEGARA MEXICO'
    elif nationality_code == 'MEX' and lang == 'en':
        nationality = 'MEXICO CITIZEN'
    elif nationality_code == 'MLI' and lang == 'ms':
        nationality = 'WARGANEGARA MALI'
    elif nationality_code == 'MLI' and lang == 'en':
        nationality = 'MALI CITIZEN'
    elif nationality_code == 'MLT' and lang == 'ms':
        nationality = 'WARGANEGARA MALTA'
    elif nationality_code == 'MLT' and lang == 'en':
        nationality = 'MALTA CITIZEN'
    elif nationality_code == 'MLW' and lang == 'ms':
        nationality = 'WARGANEGARA MALAWI'
    elif nationality_code == 'MLW' and lang == 'en':
        nationality = 'MALAWI CITIZEN'
    elif nationality_code == 'MON' and lang == 'ms':
        nationality = 'WARGANEGARA MONTSERRAT'
    elif nationality_code == 'MON' and lang == 'en':
        nationality = 'MONTSERRAT CITIZEN'
    elif nationality_code == 'MOR' and lang == 'ms':
        nationality = 'WARGANEGARA MOROCCO'
    elif nationality_code == 'MOR' and lang == 'en':
        nationality = 'MOROCCO CITIZEN'
    elif nationality_code == 'MOZ' and lang == 'ms':
        nationality = 'WARGANEGARA MOZAMBIQUE'
    elif nationality_code == 'MOZ' and lang == 'en':
        nationality = 'MOZAMBIQUE CITIZEN'
    elif nationality_code == 'MRT' and lang == 'ms':
        nationality = 'WARGANEGARA MAURITIUS'
    elif nationality_code == 'MRT' and lang == 'en':
        nationality = 'MAURITIUS CITIZEN'
    elif nationality_code == 'MSI' and lang == 'ms':
        nationality = 'WARGANEGARA MALDIVES ISLAN '
    elif nationality_code == 'MSI' and lang == 'en':
        nationality = 'MALDIVES ISLAND CITIZEN'
    elif nationality_code == 'NAU' and lang == 'ms':
        nationality = 'WARGANEGARA NAURA'
    elif nationality_code == 'NAU' and lang == 'en':
        nationality = 'NAURA CITIZEN'
    elif nationality_code == 'NEP' and lang == 'ms':
        nationality = 'WARGANEGARA NEPAL'
    elif nationality_code == 'NEP' and lang == 'en':
        nationality = 'NEPAL CITIZEN'
    elif nationality_code == 'NET' and lang == 'ms':
        nationality = 'WARGANEGARA NETHERLANDS'
    elif nationality_code == 'NET' and lang == 'en':
        nationality = 'NETHERLANDS CITIZEN'
    elif nationality_code == 'NGR' and lang == 'ms':
        nationality = 'WARGANEGARA NIGER'
    elif nationality_code == 'NGR' and lang == 'en':
        nationality = 'NIGER CITIZEN'
    elif nationality_code == 'NHS' and lang == 'ms':
        nationality = 'WARGANEGARA NEW HEBRIDES'
    elif nationality_code == 'NHS' and lang == 'en':
        nationality = 'NEW HEBRIDES CITIZEN'
    elif nationality_code == 'NIA' and lang == 'ms':
        nationality = 'PERNIAGAAN (RO) '
    elif nationality_code == 'NIA' and lang == 'en':
        nationality = 'PERNIAGAAN (ROB)'
    elif nationality_code == 'NIC' and lang == 'ms':
        nationality = 'WARGANEGARA NICARAGUA'
    elif nationality_code == 'NIC' and lang == 'en':
        nationality = 'NICARAGUA CITIZEN'
    elif nationality_code == 'NIG' and lang == 'ms':
        nationality = 'WARGANEGARA NIGERIA'
    elif nationality_code == 'NIG' and lang == 'en':
        nationality = 'NIGERIA CITIZEN'
    elif nationality_code == 'NIU' and lang == 'ms':
        nationality = 'WARGANEGARA NIUE'
    elif nationality_code == 'NIU' and lang == 'en':
        nationality = 'NIUE CITIZEN'
    elif nationality_code == 'NKI' and lang == 'ms':
        nationality = 'WARGANEGARA NORFOLD ISLAND'
    elif nationality_code == 'NKI' and lang == 'en':
        nationality = 'NORFOLD ISLAND CITIZEN'
    elif nationality_code == 'NOR' and lang == 'ms':
        nationality = 'WARGANEGARA NORWAY'
    elif nationality_code == 'NOR' and lang == 'en':
        nationality = 'NORWAY CITIZEN'
    elif nationality_code == 'NWI' and lang == 'ms':
        nationality = 'WARGANEGARA NETHERLANDS WI'
    elif nationality_code == 'NWI' and lang == 'en':
        nationality = 'NETHERLANDS WI CITIZEN'
    elif nationality_code == 'NZD' and lang == 'ms':
        nationality = 'WARGANEGARA NEW ZEALAND'
    elif nationality_code == 'NZD' and lang == 'en':
        nationality = 'NEW ZEALAND CITIZEN'
    elif nationality_code == 'OMA' and lang == 'ms':
        nationality = 'WARGANEGARA OMAN'
    elif nationality_code == 'OMA' and lang == 'en':
        nationality = 'OMAN CITIZEN'
    elif nationality_code == 'PAK' and lang == 'ms':
        nationality = 'WARGANEGARA PAKISTAN'
    elif nationality_code == 'PAK' and lang == 'en':
        nationality = 'PAKISTAN CITIZEN'
    elif nationality_code == 'PAN' and lang == 'ms':
        nationality = 'WARGANEGARA PANAMA'
    elif nationality_code == 'PAN' and lang == 'en':
        nationality = 'PANAMA CITIZEN'
    elif nationality_code == 'PAR' and lang == 'ms':
        nationality = 'WARGANEGARA PARAGUAY'
    elif nationality_code == 'PAR' and lang == 'en':
        nationality = 'PARAGUAY CITIZEN'
    elif nationality_code == 'PER' and lang == 'ms':
        nationality = 'WARGANEGARA PERU'
    elif nationality_code == 'PER' and lang == 'en':
        nationality = 'PERU CITIZEN'
    elif nationality_code == 'PHI' and lang == 'ms':
        nationality = 'WARGANEGARA PHILIPPINES'
    elif nationality_code == 'PHI' and lang == 'en':
        nationality = 'PHILIPPINES CITIZEN'
    elif nationality_code == 'PLD' and lang == 'ms':
        nationality = 'WARGANEGARA POLAND'
    elif nationality_code == 'PLD' and lang == 'en':
        nationality = 'POLAND CITIZEN'
    elif nationality_code == 'PNG' and lang == 'ms':
        nationality = 'WARGANEGARA PAPUA NEW GUINA '
    elif nationality_code == 'PNG' and lang == 'en':
        nationality = 'PAPUA NEW GUINEA CITIZEN'
    elif nationality_code == 'POL' and lang == 'ms':
        nationality = 'WARGANEGARA POLIS'
    elif nationality_code == 'POL' and lang == 'en':
        nationality = 'POLIS CITIZEN'
    elif nationality_code == 'POR' and lang == 'ms':
        nationality = 'WARGANEGARA PORTUGAL'
    elif nationality_code == 'POR' and lang == 'en':
        nationality = 'PORTUGAL CITIZEN'
    elif nationality_code == 'PRC' and lang == 'ms':
        nationality = 'WARGANEGARA CHINA (PEOPLESREPUBLIC) '
    elif nationality_code == 'PRC' and lang == 'en':
        nationality = 'CHINA (PEOPLES REPUBLIC) CITIZEN'
    elif nationality_code == 'PSN' and lang == 'ms':
        nationality = 'WARGANEGARA PERSATUAN'
    elif nationality_code == 'PSN' and lang == 'en':
        nationality = 'PERSATUAN CITIZEN'
    elif nationality_code == 'PUE' and lang == 'ms':
        nationality = 'WARGANEGARA PUERTO RICO'
    elif nationality_code == 'PUE' and lang == 'en':
        nationality = 'PUERTO RICO CITIZEN'
    elif nationality_code == 'RUM' and lang == 'ms':
        nationality = 'WARGANEGARA RUMANIA'
    elif nationality_code == 'RUM' and lang == 'en':
        nationality = 'RUMANIA CITIZEN'
    elif nationality_code == 'SAN' and lang == 'ms':
        nationality = 'WARGANEGARA SANAA (YEMEN AAB REPUBLIC) '
    elif nationality_code == 'SAN' and lang == 'en':
        nationality = 'SANAA (YEMEN ARAB REPUBLIC) CITIZEN'
    elif nationality_code == 'SAU' and lang == 'ms':
        nationality = 'WARGANEGARA SAUDIA ARABIA'
    elif nationality_code == 'SAU' and lang == 'en':
        nationality = 'SAUDIA ARABIA CITIZEN'
    elif nationality_code == 'SEN' and lang == 'ms':
        nationality = 'WARGANEGARA SENEGAL'
    elif nationality_code == 'SEN' and lang == 'en':
        nationality = 'SENEGAL CITIZEN'
    elif nationality_code == 'SEY' and lang == 'ms':
        nationality = 'WARGANEGARA SEYCHELLES'
    elif nationality_code == 'SEY' and lang == 'en':
        nationality = 'SEYCHELLES CITIZEN'
    elif nationality_code == 'SIA' and lang == 'ms':
        nationality = 'WARGANEGARA ST. LUCIA'
    elif nationality_code == 'SIA' and lang == 'en':
        nationality = 'ST. LUCIA CITIZEN'
    elif nationality_code == 'SIN' and lang == 'ms':
        nationality = 'WARGANEGARA SINGAPORE'
    elif nationality_code == 'SIN' and lang == 'en':
        nationality = 'SINGAPORE CITIZEN'
    elif nationality_code == 'SKA' and lang == 'ms':
        nationality = 'WARGANEGARA ST. KITTA'
    elif nationality_code == 'SKA' and lang == 'en':
        nationality = 'ST. KITTA CITIZEN'
    elif nationality_code == 'ALB' and lang == 'ms':
        nationality = 'WARGANEGARA ALBANIA'
    elif nationality_code == 'ALB' and lang == 'en':
        nationality = 'ALBANIA CITIZEN'
    elif nationality_code == 'SNI' and lang == 'ms':
        nationality = 'WARGANEGARA SOLOMON ISLAND'
    elif nationality_code == 'SNI' and lang == 'en':
        nationality = 'SOLOMON ISLAND CITIZEN'
    elif nationality_code == 'SOK' and lang == 'ms':
        nationality = 'WARGANEGARA KOREA SOUTH'
    elif nationality_code == 'SOK' and lang == 'en':
        nationality = 'KOREA SOUTH CITIZEN'
    elif nationality_code == 'SOM' and lang == 'ms':
        nationality = 'WARGANEGARA SOMALIA'
    elif nationality_code == 'SOM' and lang == 'en':
        nationality = 'SOMALIA CITIZEN'
    elif nationality_code == 'SPA' and lang == 'ms':
        nationality = 'WARGANEGARA SPAIN'
    elif nationality_code == 'SPA' and lang == 'en':
        nationality = 'SPAIN CITIZEN'
    elif nationality_code == 'SRI' and lang == 'ms':
        nationality = 'WARGANEGARA SRI LANGKA'
    elif nationality_code == 'SRI' and lang == 'en':
        nationality = 'SRI LANGKA CITIZEN'
    elif nationality_code == 'STP' and lang == 'ms':
        nationality = 'WARGANEGARA ST. THOME & PRNCIPTE '
    elif nationality_code == 'STP' and lang == 'en':
        nationality = 'ST. THOME & PRINCIPTE CITIZEN'
    elif nationality_code == 'SUD' and lang == 'ms':
        nationality = 'WARGANEGARA SUDAN'
    elif nationality_code == 'SUD' and lang == 'en':
        nationality = 'SUDAN CITIZEN'
    elif nationality_code == 'SVT' and lang == 'ms':
        nationality = 'WARGANEGARA ST. VINCENT'
    elif nationality_code == 'SVT' and lang == 'en':
        nationality = 'ST. VINCENT CITIZEN'
    elif nationality_code == 'SWE' and lang == 'ms':
        nationality = 'WARGANEGARA SWEDEN'
    elif nationality_code == 'SWE' and lang == 'en':
        nationality = 'SWEDEN CITIZEN'
    elif nationality_code == 'SWI' and lang == 'ms':
        nationality = 'WARGANEGARA SWITZERLAND'
    elif nationality_code == 'SWI' and lang == 'en':
        nationality = 'SWITZERLAND CITIZEN'
    elif nationality_code == 'TAH' and lang == 'ms':
        nationality = 'WARGANEGARA TAHITI'
    elif nationality_code == 'TAH' and lang == 'en':
        nationality = 'TAHITI CITIZEN'
    elif nationality_code == 'TAR' and lang == 'ms':
        nationality = 'WARGANEGARA TANGIER'
    elif nationality_code == 'TAR' and lang == 'en':
        nationality = 'TANGIER CITIZEN'
    elif nationality_code == 'TEN' and lang == 'ms':
        nationality = 'WARGANEGARA TENTERA'
    elif nationality_code == 'TEN' and lang == 'en':
        nationality = 'TENTERA CITIZEN'
    elif nationality_code == 'THA' and lang == 'ms':
        nationality = 'WARGANEGARA THAILAND'
    elif nationality_code == 'THA' and lang == 'en':
        nationality = 'THAILAND CITIZEN'
    elif nationality_code == 'TON' and lang == 'ms':
        nationality = 'WARGANEGARA TONGUA'
    elif nationality_code == 'TON' and lang == 'en':
        nationality = 'TONGUA CITIZEN'
    elif nationality_code == 'TSI' and lang == 'ms':
        nationality = 'WARGANEGARA TURKS ISLAND'
    elif nationality_code == 'TSI' and lang == 'en':
        nationality = 'TURKS ISLAND CITIZEN'
    elif nationality_code == 'TTO' and lang == 'ms':
        nationality = 'WARGANEGARA TRINIDAD & TABGO '
    elif nationality_code == 'TTO' and lang == 'en':
        nationality = 'TRINIDAD & TABAGO CITIZEN'
    elif nationality_code == 'TUN' and lang == 'ms':
        nationality = 'WARGANEGARA TUNISIA'
    elif nationality_code == 'TUN' and lang == 'en':
        nationality = 'TUNISIA CITIZEN'
    elif nationality_code == 'TUR' and lang == 'ms':
        nationality = 'WARGANEGARA TURKEY'
    elif nationality_code == 'TUR' and lang == 'en':
        nationality = 'TURKEY CITIZEN'
    elif nationality_code == 'UAE' and lang == 'ms':
        nationality = 'WARGANEGARA UNITED ARAB EMRATWES '
    elif nationality_code == 'UAE' and lang == 'en':
        nationality = 'UNITED ARAB EMIRATWES CITIZEN'
    elif nationality_code == 'UGA' and lang == 'ms':
        nationality = 'WARGANEGARA UGANDA'
    elif nationality_code == 'UGA' and lang == 'en':
        nationality = 'UGANDA CITIZEN'
    elif nationality_code == 'UKG' and lang == 'ms':
        nationality = 'WARGANEGARA UNITED KINGDOM'
    elif nationality_code == 'UKG' and lang == 'en':
        nationality = 'UNITED KINGDOM CITIZEN'
    elif nationality_code == 'URU' and lang == 'ms':
        nationality = 'WARGANEGARA URUGUAY'
    elif nationality_code == 'URU' and lang == 'en':
        nationality = 'URUGUAY CITIZEN'
    elif nationality_code == 'USA' and lang == 'ms':
        nationality = 'WARGANEGARA UNITED STATES F AMERICA '
    elif nationality_code == 'USA' and lang == 'en':
        nationality = 'UNITED STATES OF AMERICA CITIZEN'
    elif nationality_code == 'USR' and lang == 'ms':
        nationality = 'WARGANEGARA U.S.S.R.'
    elif nationality_code == 'USR' and lang == 'en':
        nationality = 'U.S.S.R. CITIZEN'
    elif nationality_code == 'UVA' and lang == 'ms':
        nationality = 'WARGANEGARA UPPER VOLTA'
    elif nationality_code == 'UVA' and lang == 'en':
        nationality = 'UPPER VOLTA CITIZEN'
    elif nationality_code == 'VAT' and lang == 'ms':
        nationality = 'WARGANEGARA VATICAN CITY'
    elif nationality_code == 'VAT' and lang == 'en':
        nationality = 'VATICAN CITY CITIZEN'
    elif nationality_code == 'VEN' and lang == 'ms':
        nationality = 'WARGANEGARA VENEZUELA'
    elif nationality_code == 'VEN' and lang == 'en':
        nationality = 'VENEZUELA CITIZEN'
    elif nationality_code == 'VIB' and lang == 'ms':
        nationality = 'WARGANEGARA VIRGIN ISLAND BRI) '
    elif nationality_code == 'VIB' and lang == 'en':
        nationality = 'VIRGIN ISLAND (BRI) CITIZEN'
    elif nationality_code == 'VIE' and lang == 'ms':
        nationality = 'WARGANEGARA VIETNAM'
    elif nationality_code == 'VIE' and lang == 'en':
        nationality = 'VIETNAM CITIZEN'
    elif nationality_code == 'VIU' and lang == 'ms':
        nationality = 'WARGANEGARA VIRGIN ISLAND US) '
    elif nationality_code == 'VIU' and lang == 'en':
        nationality = 'VIRGIN ISLAND (US) CITIZEN'
    elif nationality_code == 'WSA' and lang == 'ms':
        nationality = 'WARGANEGARA WESTERN SAMOA'
    elif nationality_code == 'WSA' and lang == 'en':
        nationality = 'WESTERN SAMOA CITIZEN'
    elif nationality_code == 'YUG' and lang == 'ms':
        nationality = 'WARGANEGARA YUGOSLAVIA'
    elif nationality_code == 'YUG' and lang == 'en':
        nationality = 'YUGOSLAVIA CITIZEN'
    elif nationality_code == 'ZAI' and lang == 'ms':
        nationality = 'WARGANEGARA ZAIRE'
    elif nationality_code == 'ZAI' and lang == 'en':
        nationality = 'ZAIRE CITIZEN'
    elif nationality_code == 'ZAM' and lang == 'ms':
        nationality = 'WARGANEGARA ZAMBIA'
    elif nationality_code == 'ZAM' and lang == 'en':
        nationality = 'ZAMBIA CITIZEN'
    elif nationality_code == 'ZIM' and lang == 'ms':
        nationality = 'WARGANEGARA ZIMBABWE'
    elif nationality_code == 'ZIM' and lang == 'en':
        nationality = 'ZIMBABWE CITIZEN'
    elif nationality_code == 'KOR' and lang == 'ms':
        nationality = 'WARGANEGARA SOUTH KOREA'
    elif nationality_code == 'KOR' and lang == 'en':
        nationality = 'SOUTH KOREA CITIZEN'
    elif nationality_code == 'IOM' and lang == 'ms':
        nationality = 'WARGANEGARA ISLE OF MAN,BRTAIN '
    elif nationality_code == 'IOM' and lang == 'en':
        nationality = 'ISLE OF MAN,BRITAIN CITIZEN'
    elif nationality_code == 'TAI' and lang == 'ms':
        nationality = 'WARGANEGARA TAIWAN'
    elif nationality_code == 'TAI' and lang == 'en':
        nationality = 'TAIWAN CITIZEN'
    elif nationality_code == 'SCO' and lang == 'ms':
        nationality = 'WARGANEGARA SCOTLAND'
    elif nationality_code == 'SCO' and lang == 'en':
        nationality = 'SCOTLAND CITIZEN'
    elif nationality_code == 'AFR' and lang == 'ms':
        nationality = 'WARGANEGARA AFRICA'
    elif nationality_code == 'AFR' and lang == 'en':
        nationality = 'AFRICA CITIZEN'
    elif nationality_code == 'SAF' and lang == 'ms':
        nationality = 'WARGANEGARA AFRIKA SELATAN'
    elif nationality_code == 'SAF' and lang == 'en':
        nationality = 'AFRIKA SELATAN CITIZEN'
    elif nationality_code == 'BVI' and lang == 'ms':
        nationality = 'WARGANEGARA BRITISH VIRGINISLANDS '
    elif nationality_code == 'BVI' and lang == 'en':
        nationality = 'BRITISH VIRGIN ISLANDS CITIZEN'
    elif nationality_code == 'YAM' and lang == 'ms':
        nationality = 'WARGANEGARA YAMAN'
    elif nationality_code == 'YAM' and lang == 'en':
        nationality = 'YAMAN CITIZEN'
    elif nationality_code == 'LIA' and lang == 'ms':
        nationality = 'WARGANEGARA LIBYA'
    elif nationality_code == 'LIA' and lang == 'en':
        nationality = 'LIBYA CITIZEN'
    elif nationality_code == 'SYR' and lang == 'ms':
        nationality = 'WARGANEGARA SYRIA'
    elif nationality_code == 'SYR' and lang == 'en':
        nationality = 'SYRIA CITIZEN'
    elif nationality_code == 'CRO' and lang == 'ms':
        nationality = 'WARGANEGARA CROATIA'
    elif nationality_code == 'CRO' and lang == 'en':
        nationality = 'CROATIA CITIZEN'
    elif nationality_code == 'UBK' and lang == 'ms':
        nationality = 'WARGANEGARA UZBEKISTAN'
    elif nationality_code == 'UBK' and lang == 'en':
        nationality = 'UZBEKISTAN CITIZEN'
    elif nationality_code == 'CON' and lang == 'ms':
        nationality = 'WARGANEGARA REPUBLIC OF COGO '
    elif nationality_code == 'CON' and lang == 'en':
        nationality = 'REPUBLIC OF CONGO CITIZEN'
    elif nationality_code == 'KIR' and lang == 'ms':
        nationality = 'WARGANEGARA REP. OF KIRIBAI '
    elif nationality_code == 'KIR' and lang == 'en':
        nationality = 'REP. OF KIRIBATI CITIZEN'
    elif nationality_code == 'COL' and lang == 'ms':
        nationality = 'WARGANEGARA REPUBLIC OF COOMBIA '
    elif nationality_code == 'COL' and lang == 'en':
        nationality = 'REPUBLIC OF COLOMBIA CITIZEN'
    elif nationality_code == 'TAJ' and lang == 'ms':
        nationality = 'WARGANEGARA REPULIC TAJIKITAN '
    elif nationality_code == 'TAJ' and lang == 'en':
        nationality = 'REPULIC TAJIKISTAN CITIZEN'
    elif nationality_code == 'LCH' and lang == 'ms':
        nationality = 'WARGANEGARA LIECHTENSTEIN'
    elif nationality_code == 'LCH' and lang == 'en':
        nationality = 'LIECHTENSTEIN CITIZEN'
    elif nationality_code == 'PSE' and lang == 'ms':
        nationality = 'WARGANEGARA PALESTINE'
    elif nationality_code == 'PSE' and lang == 'en':
        nationality = 'PALESTINE CITIZEN'
    elif nationality_code == 'QAT' and lang == 'ms':
        nationality = 'WARGANEGARA QATAR'
    elif nationality_code == 'QAT' and lang == 'en':
        nationality = 'QATAR CITIZEN'
    elif nationality_code == 'KZT' and lang == 'ms':
        nationality = 'WARGANEGARA KAZAKHSTAN'
    elif nationality_code == 'KZT' and lang == 'en':
        nationality = 'KAZAKHSTAN CITIZEN'
    
    return nationality

def business_ownership_mapping(owner_count, lang):
    if owner_count == 1 and lang == 'ms':
        temp_biz_ownership  = 'PEMILIKAN TUNGGAL'
    elif owner_count > 1 and lang == 'ms':
        temp_biz_ownership  = 'PERKONGSIAN'
    elif owner_count == 1 and lang == 'en':
        temp_biz_ownership  = 'SOLE PROPRIETORSHIP'
    elif owner_count > 1 and lang == 'en':
        temp_biz_ownership  = 'PARTNERSHIP'
    
    return temp_biz_ownership


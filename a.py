import hashlib

encoding_string = (
    'sm212345' 
    + 'SM2'
    + 'AFE001'
    + 'https://afeezaziz.ngrok.io/v1/transactions/pg_return/' #+ encode_request['merchantReturnUrl']
    + '10.00' #+ encode_request['amount'] 
    + 'MYR' #+ encode_request['currencyCode'] 
    + '1.1.1.1'#+ encode_request['custIP'] 
    + '780'#+ encode_request['pageTimeout']
)

encoding_string = encoding_string.encode('utf-8')
encoded_string = hashlib.sha256(encoding_string).hexdigest()

#print(encoded_string)

def get_auth_code():
    from datetime import datetime
    import pytz
    import subprocess
    
    now = datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur')) 

    now_string = now.strftime("%Y-%m-%d %H:%M:%S")
    auth_code = subprocess.check_output(['java', '-jar', 'authgen.jar', 'SSMProduk', now_string, '27522718']).decode("utf-8").rstrip("\n")
    print(auth_code)

get_auth_code()
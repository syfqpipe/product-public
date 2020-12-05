import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware

from .mapping import state_mapping, origin_country_mapping

def info_rob_termination(mdw_1, mdw_2, lang):

    date_format = "%d-%m-%Y"
    time_zone = 'Asia/Kuala_Lumpur'

    print('____________   ')
    print('rob_termination: ', mdw_1)
    print('____________   ')

    now = datetime.now().astimezone(pytz.timezone(time_zone)).strftime(date_format)
    end_date = make_aware(datetime.strptime(mdw_1["robBusinessInfo"]["endBusinessDate"]["#text"], '%Y-%m-%dT%H:%M:%S.000Z'))
    end_date = end_date.astimezone(pytz.timezone(time_zone)).strftime(date_format)
    
    data_ready = {
        'mdw1': mdw_1,
        'mdw2': mdw_2,
        'currentDate': now,
        'endDate': end_date,
        'printing_date': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y"),
        'generated_date': datetime.now().astimezone(pytz.timezone(time_zone)).strftime("%d-%m-%Y %-H:%M:%S")
    }

    print(data_ready)

    return data_ready
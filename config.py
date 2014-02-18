import datetime
import time


def get_timestamp_from_date_string(date_string):

    return time.mktime(datetime.datetime.strptime(date_string, "%d/%m/%Y").timetuple())

percent_to_sell_immediately = 50

currency_exchanges = {
    get_timestamp_from_date_string('07/10/2013'): 8.17,
    get_timestamp_from_date_string('07/11/2013'): 8.19,
    get_timestamp_from_date_string('06/12/2013'): 8.24,
    get_timestamp_from_date_string('19/12/2013'): 8.26,
    get_timestamp_from_date_string('31/12/2013'): 8.205,
    get_timestamp_from_date_string('01/11/2013'): 8.17,
    get_timestamp_from_date_string('03/12/2013'): 10,
    get_timestamp_from_date_string('17/12/2013'): 8.27,
    'remainder': 8.205
}

incoming = {
    get_timestamp_from_date_string('07/10/2013'): 1000,
    get_timestamp_from_date_string('07/11/2013'): 0,
    get_timestamp_from_date_string('06/12/2013'): 0,
    get_timestamp_from_date_string('19/12/2013'): 0
}

sold = {
    get_timestamp_from_date_string('01/11/2013'): 100,
    get_timestamp_from_date_string('03/12/2013'): 200,
    get_timestamp_from_date_string('17/12/2013'): 200
}


def get_config_for_calculations():
    return {
        'incoming': incoming,
        'sold': sold,
        'sell_immediately': percent_to_sell_immediately,
        'currency_exchanges': currency_exchanges,
        'tax_percent': 5
    }

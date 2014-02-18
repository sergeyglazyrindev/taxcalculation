#!/usr/bin/env python

import datetime
import time

from customs.tasks import calculate_customs


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
    get_timestamp_from_date_string('03/12/2013'): 8.223,
    get_timestamp_from_date_string('17/12/2013'): 8.27,
    'remainder': 8.205
}

incoming = {
    get_timestamp_from_date_string('07/10/2013'): 0,
    get_timestamp_from_date_string('07/11/2013'): 0,
    get_timestamp_from_date_string('06/12/2013'): 0,
    get_timestamp_from_date_string('19/12/2013'): 0
}

sold = {
    get_timestamp_from_date_string('01/11/2013'): 0,
    get_timestamp_from_date_string('03/12/2013'): 0,
    get_timestamp_from_date_string('17/12/2013'): 0
}


def run():
    calculate_customs({
        'incoming': incoming,
        'sold': sold,
        'sell_immediately': percent_to_sell_immediately,
        'currency_exchanges': currency_exchanges,
        'custom_percent': 5
    })


if __name__ == '__main__':
    run()

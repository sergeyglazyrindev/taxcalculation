from collections import deque

from .models import Incoming, Outcoming


def calculate_customs(data):
    def get_currency_exchange(date):
        return data['currency_exchanges'][date]

    # build queues
    incoming_queue = deque((Incoming(data['incoming'][date], get_currency_exchange(date)) for date in sorted(data['incoming'].keys())))
    sold_queue = deque((Outcoming(data['sold'][date], get_currency_exchange(date)) for date in sorted(data['sold'].keys())))

    revenue = 0.
    # let's iterate through incoming queue
    while True:
        if not incoming_queue:
            break
        i_item = incoming_queue.popleft()
        # let's immediately add to revenue how much we sold money when we got money to our bank account
        if data.get('sell_immediately'):
            use_amount_immediately = round(data['sell_immediately'] * i_item.amount / 100., 2)
            revenue = revenue + i_item.use(use_amount_immediately)[0]
        # let's iterate through sold queue
        while True:
            if not sold_queue:
                break
            sold_item = sold_queue.popleft()
            _revenue, really_used = i_item.use(sold_item.amount, currency_exchange=sold_item.currency_exchange)
            # let's use sell amount as well
            sold_item.use(really_used)
            revenue = revenue + _revenue
            if i_item.is_used():
                # if we used whole incoming money, let's break the loop
                if not sold_item.is_used():
                    # but if we are not used whole sold_item, let's put it again to queue
                    sold_queue.appendleft(sold_item)
                break
        # insert incoming item as not used
        if not i_item.is_used():
            incoming_queue.appendleft(i_item)
            # if we have no sold events in queue, simply break the loop
            if not sold_queue:
                break

    # let's calculate how much money left in our bank account in the end of the accounting period
    for i_item in incoming_queue:
        revenue = revenue + i_item.use(i_item.amount, get_currency_exchange('remainder'))[0]
    print "Total revenue {} grn, customs is {}".format(revenue, round(revenue * data['custom_percent'] / 100., 2))

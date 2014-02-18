class MoneyObject(object):
    amount = 0
    currency_exchange = 0

    def __init__(self, amount, currency_exchange):
        self.amount = amount
        self.currency_exchange = currency_exchange

    def use(self, amount, currency_exchange=None):
        really_used = min(self.amount, amount)
        self.amount = round(self.amount - really_used, 2)
        return round(really_used * max(self.currency_exchange, currency_exchange), 2), really_used

    def is_used(self):
        return not self.amount


class Incoming(MoneyObject):
    pass


class Outcoming(MoneyObject):
    pass

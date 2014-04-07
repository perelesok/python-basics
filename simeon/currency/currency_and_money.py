class Currency(object):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.exchange_rate = {}
        
    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)
    

class Money(object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __str__(self):
        return "{}{}".format(self.amount, self.currency.symbol)
    
    def __add__(self, money):
        return Money(self.amount + money.convert_to(self.currency).amount, self.currency)    

    def __sub__(self, money):
        return Money(self.amount - money.convert_to(self.currency).amount, self.currency)  
    
    def convert_to(self, currency):
        return Money(self.amount * self.currency.exchange_rate[currency.name], currency)
    
RUBLE = Currency("RUBLE", "rub")
RUBLE.exchange_rate = {"DOLLAR" : 1.0/36, "EURO" : 1.0/50, "RUBLE" : 1}
DOLLAR = Currency("DOLLAR", "$")
DOLLAR.exchange_rate = {"RUBLE" : 36, "EURO" : 36.0/50, "DOLLAR" : 1}
EURO = Currency("EURO", "eur")
EURO.exchange_rate = {"RUBLE" : 50, "DOLLAR" : 50.0/36, "EURO" : 1}

def rubles(n):
    return Money(n, RUBLE)


def dollars(n):
    return Money(n, DOLLAR)


def euros(n):
    return Money(n, EURO)

print rubles(40).convert_to(DOLLAR)
print dollars(3).convert_to(RUBLE)
print euros(10).convert_to(RUBLE).convert_to(DOLLAR).convert_to(RUBLE).convert_to(EURO)

print rubles(100) + euros(10) + dollars(10)
print rubles(1000) - rubles(100) - euros(10) - dollars(10)
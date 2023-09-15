class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    def get_name(self):
        return self._name
    def set_name(self):
        self._name = name

    def get_balance(self):
        return self._balance

    def moneyX(self, amount):
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _add_balance(self, other_account):
        self._balance += other_account.get_balance()
        other_account._kill()



client1 = Bank('Bekbolot', 100)
client2 = Bank('Umar', 200)



print('клиент 1:', client1.get_name())
print('Баланс клиента 1:', client1.get_balance())
print('клиент 2:', client2.get_name())
print('Баланс клиента 2:', client2.get_balance())

client1.moneyX(50)
print('клиент 1 + 50:', client1.get_balance())

client1._jackpot()
print('джекпот:', client1.get_balance())

client1._add_balance(client2)   # защ метод доб на баланс
print('клиент 1 объединение:', client1.get_balance())
print('клиент 2 объединениe:', client2.get_balance())






class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other ):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other



kalkulator = Calculator(30)


print('+', kalkulator + 10)
print('-', kalkulator - 10)
print('*', kalkulator * 10)
print('/', kalkulator / 10)
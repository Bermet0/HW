class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        money = float(input('Add:'))
        self._balance += money
        print(f'Сумма {money}. New balance: {self._balance}')

    def _kill(self):
        self._balance = 0

    def _jeckpot(self):
        self._balance *= 10

    def _merge_balance(self, o_balance):
        self._balance += o_balance
        print(f'Баланс объединен. Новый баланс: {self._balance}')


client1 = Bank('Lolita', 500)
client2 = Bank('Tigril', 1500)

client1.moneyX()
client1._jeckpot()
client1._merge_balance(client2._balance)
client2._kill()



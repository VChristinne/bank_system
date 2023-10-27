from bank_system.account import Account


class CheckingAccount(Account):

    def __init__(self, holder, number, balance, limit):
        super().__init__(holder, number, balance, limit)

    def update(self, tax):
        super().update(tax * 2.0)

    def get_tax_value(self):
        return self._balance * 0.01


class SavingAccount(Account):

    def __init__(self, holder, number, balance, limit):
        super().__init__(holder, number, balance, limit)

    def update(self, tax):
        super().update(tax * 2.5)

    def get_tax_value(self):
        return self._balance * 0.02


class InvestmentAccount(Account):

    def __init__(self, holder, number, balance, limit):
        super().__init__(holder, number, balance, limit)

    def update(self, tax):
        super().update(tax * 2.8)

    def get_tax_value(self):
        return self._balance * 0.03

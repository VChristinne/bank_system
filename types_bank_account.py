from bank_system.account import Account


class CheckingAccount(Account):

    def __init__(self, holder, number, balance, limit, password):
        super().__init__(holder, number, balance, limit, password)

    def update(self, tax=None):
        super().update(0.001 * 2.0)


class SavingAccount(Account):

    def __init__(self, holder, number, balance, limit, password):
        super().__init__(holder, number, balance, limit, password)

    def update(self, tax=None):
        super().update(0.005 * 2.5)


class InvestmentAccount(Account):

    def __init__(self, holder, number, balance, limit, password):
        super().__init__(holder, number, balance, limit, password)

    def update(self, tax=None):
        super().update(0.1 * 3.0)


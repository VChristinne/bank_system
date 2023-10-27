from bank_system.account import Account


class CheckingAccount(Account):

    def __init__(self, holder, number, balance, limit):
        super().__init__(holder, number, balance, limit)

    def update(self):
        super().update(0.01 * 2.0)


class SavingAccount(Account):

    def __init__(self, holder, number, balance, limit):
        super().__init__(holder, number, balance, limit)

    def update(self):
        super().update(0.05 * 2.5)


class InvestmentAccount(Account):

    def __init__(self, holder, number, balance, limit):
        super().__init__(holder, number, balance, limit)

    def update(self):
        super().update(0.08 * 2.8)


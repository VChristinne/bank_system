from bank_system.insurance import Insurance


class LifeInsurance(Insurance):

    def __init__(self, policy_id, holder, price=2000):
        super().__init__(policy_id, holder, price)

    def update(self, tax):
        self._price += self._price * tax * 0.05

    def get_tax_value(self):
        return self._price * 0.03

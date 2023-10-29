import abc
from colorama import Fore


class Insurance(abc.ABC):

    def __init__(self, policy_id, holder, price):
        self._price = price
        self._holder = holder
        self._policy_id = policy_id

    def insurance_info(self):
        return (Fore.GREEN + f"Account Info:"
                             f"\nPolicy ID -> {self._policy_id}"
                             f"\nHolder -> {self._holder}"
                             f"\nPrice -> {self._price}" + Fore.RESET)

    @property
    def price(self):
        return self._price

    @abc.abstractmethod
    def update(self, tax):
        pass

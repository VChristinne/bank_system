import datetime


class Date:
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        print(f"\nDay: {self.day}"
              f"\nMonth: {self.month}"
              f"\nYear: {self.month}")


class History:
    def __init__(self):
        self.opening_date = datetime.datetime.today()
        self.transactions = []

    def print_transactions(self):
        print(f"Account opening date: {self.opening_date}")
        print("Transactions: ")
        for t in self.transactions:
            print("-", t)

class History:
    def __init__(self, account_id):
        self.transactions = []
        self.file_path = f"history_{account_id}.txt"
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.file_path, "r") as file:
                self.transactions = file.readlines()
        except FileNotFoundError:
            pass

    def save_transactions(self):
        with open(self.file_path, "w") as file:
            for transaction in self.transactions:
                file.write(transaction + "\n")

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        with open(self.file_path, "a") as file:
            file.write(transaction + "\n")

    def get_transactions(self):
        self.load_transactions()
        return self.transactions

    def __str__(self):
        self.load_transactions()
        result = "\nTransactions:\n"

        withdraw_count = 0
        deposit_count = 0
        transfer_count = 0

        for t in self.transactions:
            result += f"- {t}"

            if "Withdraw" in t:
                withdraw_count += 1

            if "Deposit" in t:
                deposit_count += 1

            if "Transfer" in t:
                transfer_count += 1

        result += (f"\nTotal Withdraws: {withdraw_count}"
                   f"\nTotal Deposits: {deposit_count}"
                   f"\nTotal Transfer: {transfer_count}")

        return result

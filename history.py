import os
import json


class History:

    def __init__(self, account_id):
        self.transactions = []
        folder_path = "files_json"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.file_path = os.path.join(folder_path, f"history_{account_id}.json")
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.file_path, "r") as file:
                data = file.read()
                if data:
                    self.transactions = json.loads(data)
        except FileNotFoundError:
            pass

    def save_transactions(self):
        with open(self.file_path, "w") as file:
            json.dump(self.transactions, file)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_transactions()

    def get_transactions(self):
        self.load_transactions()
        return self.transactions

    def __str__(self):
        self.load_transactions()
        result = "\nTransactions:"

        for t in self.transactions:
            result += f"\n- {t}"

        return result

    def get_transactions(self):
        self.load_transactions()
        return [str(transaction) for transaction in self.transactions]
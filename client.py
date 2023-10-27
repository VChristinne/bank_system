class Client:
    def __init__(self, name, surname, cpf):
        self.name = name
        self.surname = surname
        self.cpf = cpf
        self.clients = []
        self.file_path = f"client_list.txt"
        self.load_clients()

    def load_clients(self):
        try:
            with open(self.file_path, "r") as file:
                self.clients = file.readlines()
        except FileNotFoundError:
            pass

    def save_clients(self):
        with open(self.file_path, "w") as file:
            for client in self.clients:
                file.write(client + "\n")

    def add_clients(self, client):
        self.clients.append(client)
        with open(self.file_path, "a") as file:
            file.write(client + "\n")

    def get_client(self):
        self.load_clients()
        return self.clients

    def __str__(self):
        self.load_clients()
        result = "\nClients:\n"

        for c in self.clients:
            result += f"- {c}"

        return result

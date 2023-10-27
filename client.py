class FileManager:
    @staticmethod
    def load_data(file_path):
        try:
            with open(file_path, "r") as file:
                return [line.strip().split("|") for line in file]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_data(file_path, data):
        with open(file_path, "w") as file:
            for item in data:
                file.write("|".join(item) + "\n")


class Client:
    def __init__(self, name, surname, cpf):
        self.name = name
        self.surname = surname
        self.cpf = cpf
        self.file_path = f"client_list.txt"
        self.clients = FileManager.load_data(self.file_path)

    def add_client(self):
        new_client = [self.name, self.surname, self.cpf]
        self.clients.append(new_client)
        FileManager.save_data(self.file_path, self.clients)

    @staticmethod
    def list_clients(clients_list):
        result = "\nClients:\n"

        for c in clients_list:
            result += f"- Name: {c[0]}, Surname: {c[1]}, CPF: {c[2]}\n"

        return result

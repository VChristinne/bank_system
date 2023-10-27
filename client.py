from bank_system.file_manager import FileManager


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

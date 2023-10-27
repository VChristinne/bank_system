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

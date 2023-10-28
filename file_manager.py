import fcntl


# preventing the TOCTOU condition
# o arquivo é aberto antes de aplicar o lock, e ele só será fechado após o lock ser liberado
class FileManager:
    @staticmethod
    def load_data(file_path):
        file = open(file_path, "r")
        try:
            fcntl.lockf(file, fcntl.LOCK_SH)  # add read lock
            return [line.strip().split("|") for line in file]
        except FileNotFoundError:
            return []
        finally:
            fcntl.lockf(file, fcntl.LOCK_UN)  # releasing the lock after reading
            file.close()  # ensure that the file is closed correctly

    @staticmethod
    def save_data(file_path, data):
        file = open(file_path, "w")
        try:
            fcntl.lockf(file, fcntl.LOCK_EX)  # add write lock
            for item in data:
                file.write("|".join(item) + "\n")
        except FileNotFoundError:
            return []
        finally:
            fcntl.lockf(file, fcntl.LOCK_UN)  # releasing the lock after writing
            file.close()  # ensure that the file is closed correctly

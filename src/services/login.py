import hashlib

class Login:
    def __init__(self):
        self._login_file_path = ".login"

    def get_token(self):
        with open(self._login_file_path, encoding="utf-8") as file:
            token = file.read()
        if len(token) == 64:
            return token
        return None

    def log_in(self, username, password):
        if "#" in username:
            return False
        token = hashlib.sha256(f"{username}#{password}")
        with open(self._login_file_path, encoding="utf-8") as file:
            file.write(token)
        return True

    def log_out(self):
        with open(self._login_file_path, encoding="utf-8") as file:
            file.write("")

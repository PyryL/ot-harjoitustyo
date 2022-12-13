import hashlib

class Login:
    def __init__(self, file_path = None):
        self._login_file_path = file_path if file_path is not None else ".login"

    def get_token(self):
        try:
            with open(self._login_file_path, encoding="utf-8") as file:
                token = file.read()
        except FileNotFoundError:
            return None
        if len(token) == 64:
            return token
        return None

    def log_in(self, username, password):
        if "#" in username:
            return False
        token = hashlib.sha256(f"{username}#{password}".encode("utf-8")).hexdigest()
        with open(self._login_file_path, "w", encoding="utf-8") as file:
            file.write(token)
        return True

    def log_out(self):
        with open(self._login_file_path, "w", encoding="utf-8") as file:
            file.write("")

import hashlib

class Login:
    """Class handling user login tokens."""

    def __init__(self, file_path = None):
        """Constructor for a new token handling instance.

        Args:
            file_path (str, optional): Path for a file which stores the token. Defaults to None.
        """
        self._login_file_path = file_path if file_path is not None else ".login"

    def get_token(self):
        """Read the login token from a file, if available.

        Returns:
            str, optional: Returns the token when available, None otherwise
        """
        try:
            with open(self._login_file_path, encoding="utf-8") as file:
                token = file.read()
        except FileNotFoundError:
            return None
        if len(token) == 64:
            return token
        return None

    def log_in(self, username, password):
        """Store a token for the user with given credentials.

        Args:
            username (str): The username of the user. Must not contain # character or be empty.
            password (str): The password of the user. Must not be empty.

        Returns:
            bool: False if given credentials don't meet requirements, True otherwise
        """
        if "#" in username or len(username) == 0 or len(password) == 0:
            return False
        token = hashlib.sha256(f"{username}#{password}".encode("utf-8")).hexdigest()
        with open(self._login_file_path, "w", encoding="utf-8") as file:
            file.write(token)
        return True

    def log_out(self):
        """Forgets the saved login token."""
        with open(self._login_file_path, "w", encoding="utf-8") as file:
            file.write("")

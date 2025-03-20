from pydantic import BaseModel

class User:
    def __init__(self, id, login, password, crypto_key):
        self.id = id
        self.login = login
        self.password = password
        self.crypto_key = crypto_key


class File:
    def __init__(self, client_filename, server_filename, owner_id):
        self.client_filename = client_filename
        self.server_filename = server_filename
        self.owner_id = owner_id



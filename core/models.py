from data_manager.base import BaseModel
from dataclasses import dataclass 

@dataclass
class User(BaseModel):
    CURRENT_USER = None

    username: str
    firstname: str
    lastname: str
    password: str  # TODO!

    @staticmethod
    def __hash(s: str):
        # TODO!
        return s

    def check_password(self, password):
        return self.__hash(password) == self.__hash(self.password)


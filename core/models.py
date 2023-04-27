from data_manager.base import BaseModel
from dataclasses import dataclass 

@dataclass
class User(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str


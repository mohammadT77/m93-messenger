from data_manager.base import BaseModel
from dataclasses import dataclass 
from .settings import manager
import psycopg2.extras
from datetime import datetime
from typing import Optional

@dataclass
class User(BaseModel):
    TABLE_NAME = 'users'
    
    COLUMNS = {
        'username':('username','VARCHAR(20)','UNIQUE'),
        'first_name':('first_name','VARCHAR(10)','NOT NULL'),
        'last_name':('last_name','VARCHAR(10)','NOT NULL'),
        'password':('password','VARCHAR(100)','NOT NULL'),
    }

    CURRENT_USER = None

    username: str
    first_name: str
    last_name: str
    password: str  # TODO: hash

    @staticmethod
    def __hash(s: str):
        # TODO: hash
        return s

    def check_password(self, password):
        return self.__hash(password) == self.__hash(self.password)


    @classmethod
    def get_user_by_username(cls, username):
        with manager.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curs:
            curs.execute(f"SELECT * FROM {cls.TABLE_NAME} WHERE username=%s", (username,))
            data = curs.fetchone()
            return cls.from_dict(data) if data else None
   

@dataclass
class Message(BaseModel):
    TABLE_NAME = "messages"
    COLUMNS = {
        'subject': ('subject','VARCHAR(50)','NOT NULL'),
        'content': ('content','TEXT','NOT NULL'),
        'sender': ('sender','INT','NOT NULL', 'REFERENCES users (_id)'),
        'receiver': ('receiver','INT','NOT NULL', 'REFERENCES users (_id)'),
        'status': ('status','VARCHAR(6)','NOT NULL', "DEFAULT 'DRAFT'"),
        'last_change': ('last_change','TIMESTAMP','DEFAULT CURRENT_TIMESTAMP'),
        'reply_parent': ('reply_parent', 'INT','NULL', 'REFERENCES messages (_id)'),
    }

    subject: str
    content: str
    sender: int
    receiver: int
    status: str = 'DRAFT' # = ('DRAFT', 'DONE', 'SEEN')
    last_change: str = str(datetime.now())
    reply_parent: Optional[int] = None
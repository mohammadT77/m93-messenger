from data_manager.file_manager import FileManager
from data_manager.db_manager import DBManager

db_config = {
    'dbname': 'postgres',
    'host':'localhost',
    'user':'postgres',
    'password': 'postgres'
}

manager = DBManager({'db_config':db_config})
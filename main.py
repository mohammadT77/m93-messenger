from menu.utility import generate_menu
from menu_route import MENU_ROUTE

# menu_root = generate_menu(MENU_ROUTE)
# menu_root()
db_config = {
    'dbname': 'postgres',
    'host':'localhost',
    'user':'postgres',
    'password': 'postgres'
}

from data_manager.db_manager import DBManager
from core.models import User
dbmanager = DBManager({'db_config': db_config})
print(dbmanager.get_create_table_sql(User))
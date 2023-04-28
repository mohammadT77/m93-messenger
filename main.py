from menu.utility import generate_menu
from menu_route import MENU_ROUTE

menu_root = generate_menu(MENU_ROUTE)
menu_root()
# db_config = {
#     'dbname': 'postgres',
#     'host':'localhost',
#     'user':'postgres',
#     'password': 'postgres'
# }

# from data_manager.db_manager import DBManager
# from core.models import User, Message
# dbmanager = DBManager({'db_config': db_config})
# # user1 = dbmanager.read(2, User)
# # user2 = dbmanager.read(3, User)

# # print(*list(dbmanager.read_all(User)), sep="\n")
# # msg = Message("Test", "testest", user1._id, user2._id)
# print(list(dbmanager.read_all(Message)))
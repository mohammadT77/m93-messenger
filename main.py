from menu.utility import generate_menu
from menu_route import MENU_ROUTE

# menu_root = generate_menu(MENU_ROUTE)
# menu_root()

from data_manager.file_manager import FileManager
from core.models import User

manager = FileManager({'ROOT_PATH':'data/'})

user = manager.read(1, User)
print(user)


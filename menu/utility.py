from .exceptions import MenuGenerateError
from .models import MenuView, MenuList, Menu


def generate_menu(menu_dict: dict, parent=None) -> Menu:
    if 'children' in menu_dict:
        menu = MenuList(menu_dict['name'], parent, description=menu_dict.get('description'))
        for c in menu_dict['children']:
            generate_menu(c, parent=menu)
    elif 'function' in menu_dict:
        menu = MenuView(menu_dict['function'], menu_dict.get('name', None), parent=parent,
                        description=menu_dict.get('description'))
    else:
        raise MenuGenerateError()

    return menu
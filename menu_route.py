def todo():
    print("TODO")


MENU_ROUTE = {
    'name': 'Messenger App',
    'description': 'Maktab 93 - python project',
    'children': [
        {
            'name':'Login/Register',
            'description':'',
            'children': [
                {
                    'name':'Login',
                    'description':'',
                    'function': todo,
                },
                {
                    'name':'Register',
                    'description':'',
                    'function': todo,
                },
                {
                    'name':'Logout',
                    'description':'',
                    'function': todo,
                }
            ]
        },
        {
            'name': 'User panel',
            'description': '',
            'children': [
                {
                    'name': 'Create new message',
                    'description': '',
                    'function':todo,
                },
                {
                    'name': 'Inbox',
                    'description': '',
                    'function':todo
                },
                {
                    'name': 'Sent',
                    'description': '',
                    'function':todo,
                },
                {
                    'name': 'Draft',
                    'description': '',
                    'function':todo,
                }
            ]
        }
    ]
}
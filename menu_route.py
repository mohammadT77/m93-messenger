from core import views

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
                    'function': views.login,
                },
                {
                    'name':'Register',
                    'description':'',
                    'function': views.register,
                },
                {
                    'name':'Logout',
                    'description':'',
                    'function': views.logout,
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
                    'function':views.create_new_message,
                },
                {
                    'name': 'Inbox',
                    'description': '',
                    'function':views.inbox
                },
                {
                    'name': 'Sent',
                    'description': '',
                    'function':views.sent,
                },
                {
                    'name': 'Draft',
                    'description': '',
                    'function':views.draft,
                }
            ]
        }
    ]
}
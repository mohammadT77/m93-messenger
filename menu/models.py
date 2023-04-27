from abc import ABC, abstractmethod


class Node:

    def __init__(self, parent=None) -> None:
        self.children = []
        assert parent is None or isinstance(parent, Node), "Parent must be a Node instance"
        self.parent = parent
        if parent:
            self.parent.children.append(self)


class Menu(ABC, Node):
    def __init__(self, name, parent=None, description=""):
        assert parent is None or isinstance(parent, Menu), "Parent must be a Menu instance"
        Node.__init__(self, parent)
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name + (f": {self.description}" if self.description else '')

    @staticmethod
    def get_input(prompt="", validator=None, retry=True):
        i = input(prompt)
        try:
            return validator(i) if validator else None
        except Exception as e:
            if retry:
                print('Error:', e)
                Menu.get_input(prompt, validator, retry)
            else:
                raise e

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class MenuList(Menu):

    def __call__(self, *args, **kwargs):
        print(f"{self.parent.name} > {self.name}" if self.parent else self.name)
        print(f"{self.description}")
        print("\nMenuItems:")
        for i, c in enumerate(self.children):
            print('\t', f'{i+1}.', repr(c))

        def validator(s: str):
            if s.isnumeric():
                s = int(s)
                return self.children[s-1] if s else self.parent
            else:
                for c in self.children:
                    if c.name.strip().casefold() == s.strip().casefold():
                        return c
            assert False, "Invalid input"

        prompt = f"\nSelect (0 to {'return' if self.parent else 'exit'}): "
        x = self.get_input(prompt, validator=validator)
        if not x:
            exit(0)
        else:
            x()


class MenuView(Menu):

    def __init__(self, function, name=None, parent=None, description=""):
        if not name:
            name = function.__name__
        super().__init__(name, parent, description)
        self.function = function

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        print()
        if self.parent:
            self.parent()
        else:
            exit()
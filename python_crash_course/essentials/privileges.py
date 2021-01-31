class Privileges:
    def __init__(self):
        # print('__init__ method') -> initialization without () doesn't run it
        self.privileges = [
            'add post',
            'edit post',
            'remove post'
        ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
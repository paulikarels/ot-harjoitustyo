class User:
    def __init__(self, ids, username, password, admin=False):
        self.id = ids
        self.username = username
        self.password = password
        self.admin    = admin
    

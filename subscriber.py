
class Subscriber:


    def __init__(self, name, userid, password):
        self.name = name
        self.userid = userid
        self.password = password

    def get_name(self):
        return self.name

    def get_id(self):
        return self.userid

    def get_password(self):
        return self.password

    def set_name(self, name):
        self.name = name
    def set_id(self, userid):
        self.userid = userid

    def set_password(self, word):
        self.password = word

    def __repr__(self):
        return f'Subscriber({self.name}, {self.userid}, {self.password})'


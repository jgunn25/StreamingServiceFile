

class Program:

    def __init__(self, title, genre, creator,date):
        self.title = title
        self.genre = genre
        self.creator = creator
        self.date = date

    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def get_creator(self):
       return self.creator
    def get_date(self):
        return self.date
    def set_title(self, title):
        self.title = title
    def set_genre(self, genre):
        self.genre = genre
    def set_creator(self, creator):
        self.creator = creator
    def set_release_date(self, date):
        self.date = date
    def __repr__(self):
        return f'Program({self.title}, {self.genre}, {self.creator}, {self.date})'


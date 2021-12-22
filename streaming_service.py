from program import *
from subscriber import *
#from file_processing import *

#service_name = 'Netflix'
#subscriber1 =[Subscriber("Walt", "thefounder", "133t"), Subscriber("Stan", "thewriter", "lee1922"), Subscriber("Jacob", "user123", "gunsl")]
#list2 = [Program('Halt and Catch Fire', 'Drama', 'Christopher Cantwell and Christopher C. Rogers', '2014'), Program('Arrival', 'Drama', 'Denis Villeneuve', '2016'), Program('Us', 'Horror', 'Jordan Peele', '2018'), Program('Matrix; The', 'Sci-Fi', 'The Wachowskis', '1999')]

class StreamingService:

        def __init__ (self, name, program_list, subscriber):
            self.name = name
            self.program_list = program_list
            self.subscriber_list = subscriber
        def get_name(self):
            return self.name
        def get_programs(self):
            return self.program_list
        def subscribers(self):
            return self.subscriber_list

        def get_program(self, title):

            for x in range(len(self.program_list)):
                if title == self.program_list[x].get_title():
                    return self.program_list[x].__repr__()
                else:
                    pass
            else:
                return None


        def get_subscriber(self, sub):
            y = 0
            while y<= len(self.subscriber_list):
                for x in range(len(self.subscriber_list)):
                    if sub == self.subscriber_list[x].get_name():
                        y = int(len(self.subscriber_list))+1
                        return self.subscriber_list[x].__repr__()
                    else:
                        y +=1
            return None


        def set_name(self, name):
            self.name = name

        def add_program(self,program):
            """
            Adds the given Program object to the service's list of programs. This is done by using the program file
            and __repr__ the information given to create a useable Program object. The new program then gets append into
            self.program_list which will be added to the services list of programs
            """
            title = program[0]
            genre = program[1]
            producer = program[2]
            year = program[3]
            new_object = Program(title, genre, producer, year)
            self.program_list.append(new_object)

        def add_subscriber(self, subscriber):
            """
            Adds a subscriber object to the preexisting list of subscriber objects in the service. This exports the
            information to the subscriber file to determine if all the criterias given are valid. If so the information
            will the be returned through the __repr__ method then appened to the subscriber_list.
            """
            name = subscriber[0]
            user_id = subscriber[1]
            password = subscriber[2]
            new_obejct = Subscriber(name, user_id, password)
            self.subscriber_list.append(new_obejct)

        def remove_program(self,title):


            for x in range(0, len(self.program_list)):
                for program_value in self.program_list:
                    if self.program_list[x].get_title() == title:
                       print(self.program_list)
                       self.program_list.remove(program_value)





                   # self.program_list.remove(self.program_list[x])



        def remove_subscriber(self, name):
            for x in range(len(self.subscriber_list)):
                for y in self.subscriber_list:
                    if name == self.subscriber_list[x].get_name():
                        self.subscriber_list.remove(y)







        def update_program(self, title, genre, creator, date):
            for x in range(len(self.program_list)):
                if title == self.program_list[x].get_title():
                    if genre != "":
                        self.program_list[x].set_genre(genre)
                    if creator != "":
                        self.program_list[x].set_creator(creator)
                    if date != "":
                        self.program_list[x].set_release_date(date)
                else:
                    pass


        def update_subscriber(self,name, userid,password):
            """
            updates a specific subscriber object from information taken from a update csv file. All data which is not
            needed to be updated is taken by an empty string so the if functions each for strings which are not empty
            to proceed. It then goes the Subscriber object and uses the set methods to update the specific object.
            """
            for x in range(len(self.subscriber_list)):
                if name == self.subscriber_list[x].get_name():
                    if userid != "":
                        self.subscriber_list[x].set_id(userid)
                    if password != "":
                        self.subscriber_list[x].set_password(password)


        def sort(self):
            title_list = []
            prog_list = []
            for x in range(len(self.program_list)):
                title_list.append(self.program_list[x].get_title())
            title_list.sort()

            for x in range(len(title_list)):
                for y in range(len(self.program_list)):

                    if self.program_list[y].get_title() == title_list[x]:
                        title = self.program_list[y].get_title()
                        genre = self.program_list[y].get_genre()
                        producer = self.program_list[y].get_creator()
                        year = self.program_list[y].get_date()
                        prog_list.append(Program(title, genre, producer, year))

            self.program_list = prog_list

        def __repr__(self):
            return f'StreamingService({self.name}, {self.program_list}, {self.subscriber_list})'



# File is complete besides the delete part of remove methods. also check the update methods. Return None is not implimented. sort and repr is complete

#StreamingService(service_name, list2, subscriber1).remove_program("Halt and Catch Fire")
#print(StreamingService(service_name, list2, subscriber1).__repr__())

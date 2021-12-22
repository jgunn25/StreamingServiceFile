import csv

from streaming_service import *
from subscriber import *
from program import *

update_file = "update_netflix.csv"
add_file = "netflix.csv"
list_of_programs_class = []
list_of_subscribers_class = []
streaming_name = "Netflix"   # Make this into a variable
main_object_list = StreamingService(streaming_name, list_of_programs_class, list_of_subscribers_class)
program_list = []
subscriber_list = []
def build_new_service(add_file):
    try:
        with open(add_file, "r") as reader:
            data_set = csv.reader(reader)
            service = reader.readline()
            state_var = ""
            streaming_name = service



            for x in data_set:

                if x == ["PROGRAMS"]:
                    state_var = "PROGRAMS"
                    program_list.append(x)
                elif x == ['SUBSCRIBERS']:
                    state_var = "SUBSCRIBERS"
                    subscriber_list.append(x)
                else:
                    if state_var == "PROGRAMS":
                        list_of_programs_class.append(Program(x[0],x[1],x[2],x[3]))
                        program_list.append([x[0], x[1], x[2], x[3]])
#                        print(f'Adding program... {x[0]}')


                    elif state_var == "SUBSCRIBERS":
                        list_of_subscribers_class.append(Subscriber(x[0], x[1], x[2]))
#                        print(f'Adding subscriber...{x[0]}')
                        subscriber_list.append([x[0], x[1], x[2]])



            return StreamingService(streaming_name,list_of_programs_class,list_of_subscribers_class)

    except:
        print("NONE")



def update_service(update_file, build_new_service):
    with open(update_file, 'r') as read_value:
        reader = csv.reader(read_value)
        state_var = ""
        for x in reader:

            if x == ["PROGRAMS"]:
                state_var = "PROGRAMS"

            elif x == ['SUBSCRIBERS']:
                state_var = "SUBSCRIBERS"


            else:
                if state_var == "PROGRAMS":
                    if x[0] == "+":
                        program1 = [x[1],x[2],x[3],x[4]]
                        main_object_list.add_program(program1)
                        program_list.append([x[1],x[2],x[3],x[4]])

                    elif x[0] == "-":


                        for y in range(len(program_list)):
                            if x[1] == program_list[y][0]:
                                program_list.remove(program_list[y])
                                main_object_list.remove_program(x[1])




                    elif x[0] == "^":
                        print(f'{x} changing')

                        main_object_list.update_program(x[1],x[2],x[3],x[4])
                        build_new_service.update_program(x[1],x[2],x[3],x[4])

                        for y in range(len(program_list)):

                            if program_list[y][0] == x[1]:
                                program_list[y][0] = x[1]
                                if x[2] != "":

                                    program_list[y][1] = x[2]
                                if x[3] != "":

                                    program_list[y][2] = x[3]
                                if x[4] != "":

                                    program_list[y][3] = x[4]
                            print(f'{program_list[y]} updating Program')
                    else:
                        pass




                elif state_var == "SUBSCRIBERS":
                    if x[0] =="+":
                        print(f'{x} Adding')
                        build_new_service.add_subscriber((x[1],x[2],x[3]))
                        main_object_list.add_subscriber((x[1],x[2],x[3]))
                        subscriber_list.append([x[1],x[2],x[3]])
                        print(f'{x} add sub')
                    elif x[0] == "-":
                        main_object_list.remove_subscriber(x)


                    elif x[0] == "^":
                        build_new_service.update_subscriber(x[1],x[2],x[3])
                        main_object_list.update_subscriber(x[1],x[2],x[3])
                        print(f'{x} mod sub')
                    else:
                        pass
        main_object_list.sort()
        print(main_object_list)



def write_update(new_file, stream_object):
    with open(new_file, 'r') as input_value:
        input = csv.reader(input_value)
        with open(new_file, 'w') as output_file:
            with open (new_file, 'a') as file:
                file.write(f'{str(streaming_name)}\n')
                file.write('PROGRAMS\n')
                for x in stream_object:

                    file.write(f'{stream_object[x]}\n')












"""
def update_service(update_file, build_new_service):
    with open(update_file, 'r') as reader:
        reader = csv.reader(reader)
        state_var = ""
        for x in reader:
#            print(x)
            if x == ["PROGRAMS"]:
                state_var = "PROGRAMS"

            elif x == ['SUBSCRIBERS']:
                state_var = "SUBSCRIBERS"

            else:
                if state_var == "PROGRAMS":
                    if x[0] == "+":
                        title = x[1]
                        genre = x[2]
                        producer = x[3]
                        year = x[4]
                        pro_cl.add_program(Program(title, genre, producer, year))
                        print(f'Program({title},{genre},{producer},{year})')


                elif state_var == "SUBSCRIBERS":
                    pass
                else:
                    pass


"""
"""                    if x[0] == "^":
                        for y in streaming_serv_object:
                            if x[1] == y[1]:
                                print('yes')
                            else:
                                pass
                            
                elif state_var == "SUBSCRIBER":
                    pass
"""
#    except:
#        print("NONE")
"""
#                           print(x[1:])
#                           for y in programs_streaming_serv:
#                                if x[1] == y[1]:
#                                    print(x)
#                                    print(y)

#                        print(f'Adding program... {x[0]}')


                    elif state_var == "SUBSCRIBERS":
                        Subscriber(x[0], x[1], x[2])
                        update_sub_list.append(Subscriber(x[0], x[1], x[2]).__repr__())
                        update_subs.append((x[0], x[1], x[2]))
#                        print(f'Adding subscriber...{x[0]}')
                    else:
                        pass

"""


#build_new_service(add_file)
update_service(update_file,build_new_service(add_file))




#write_update(update_file, main_object_list)

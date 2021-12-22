from file_processing import *
def main():

    while True:
        start = input("Would you like to update a file?  Y/N\n")
        start.upper()
        list_of_programs_class.clear()
        list_of_subscribers_class.clear()
        if start == "Y":
           creation_file = input("Please enter the streaming service creation file (or 'done' to exit)\n")
           build_new_service(creation_file)



        elif start == "N":
            print("Exiting program...\n")
            break


        else:
            print("incorrect value...\n")

        update_file = input(f"Please enter the update file you would like to read(or 'done' to exit)\n")
        update_file.upper()
        try:
            update_service(update_file)

        except:
            pass


main

def data_filtering():
    pass
## NEXT Hospital Interface

class Hospital():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []
        self.patients = []
        self.admins = []
        self.employees_number = 0
        self.patients_number = 0

    def list_patients(self):
        for i in self.patients:
            print(i.name)
        print("")

    def view_records(self, number):
        Found = False
        for i in self.patients:
            if i.number == number:
                print("Patient records is empty!" if i.description == "" else i.description)
                Found = True
        if Found == False:
            print("There's NO SUCH PATIENT NUMBER!")
        print("")

    def add_records(self, number):
        Found = False
        for i in self.patients:
            if i.number == number:
                Found = True
                description = str(input("Add your description here: "))
                i.description.append(description)
                print(f"You have entered a patient {i.number}\'s record")
        if Found == False:
            print("There's NO SUCH PATIENT NUMBER!")
        print("")

    def delete_records(self, number):
        Found = False
        for i in self.patients:
            if i.number == number:
                Found = True

                if len(i.description) == 0:
                    print("Patient records is empty!")
                else: 
                    num = int(input("Type your number to delete record: "))
                    if len(i.description) < 0 or len(i.description) >= num:
                        print("THAT'S OUT OF INDEX BOX!!!!")
                    else:
                        i.description.pop(num)
                        print(f"You have deleted patient {i.number}\'s record!")
        if Found == False:
            print("There's NO SUCH PATIENT NUMBER!")
        print("")

class Patient():
    def __init__(self, name, password, number):
        self.name = name
        self.password = password
        self.description = []
        self.number = number


class Employee():
    def __init__(self, name, post, password):
        self.name = name
        self.post = post
        self.password = password
        self.employee_number = 0

class Admin():
    def __init__(self, name, password):
        self.name = name
        self.password = password

exit_game = False
exit_game_doctor = False

hospital1 = Hospital("Sungai Long Medical Center", "Sungai Long")
hospital1.employees.append(Employee("Ming", "DOCTOR", "haha"))
hospital1.patients.append(Patient("jwleong", "haha", 1))
hospital1.patients.append(Patient("josh", "haha", 2))
hospital1.patients.append(Patient("nic", "haha", 3))
hospital1.admins.append(Admin("admin", "haha"))

# def input_doctor(i, j):
#     switcher={
#                 1: hospital1.list_patients(),
#                 2: hospital1.view_records(j),
#                 3: hospital1.add_records(j),
#                 4:'Thursday',
#                 5: exit_hospital(),
#              }
#     return switcher.get(i,"INVALID INPUT NUMBER")

def welcome():
    print(f"Welcome to {hospital1.name}")
    print("==========================")
    print("1. Patient")
    print("2. Employee")
    print("3. Admin")
    print("4. Exit. bye :(")
    print("")

def patient_login():
    enter_username = str(input("Please enter your username: "))
    Found = False
    for i in hospital1.patients:
        if enter_username == i.name:
            Found = True
            enter_password = str(input("Please enter your password: "))
            if enter_password == i.password:
                print(f'''====================================================
                        Welcome, {i.name}.
                        1. view_records
                        2. exit
                        ====================================================
                        ''')
                while not exit_game_doctor:
                    input_num = int(input("What would you like to do? "))
                    if input_num == 1:
                        print(i.description)
                    elif input_num == 2:
                        break
                    elif input == None:
                        print("NO ITCHY HAND PRESS ENTEr\n")
                    else:
                        print("INVALID INPUT NUMBER\n")
            else:
                print("INCORRECT PASSWORD\n")
    if not Found:
        print("There's no such username exists! SPY\n")

def employee_login():
    Found = False
    enter_username = str(input("Please enter your username: "))
    for i in hospital1.employees:
        Found = True
        if enter_username == i.name:
            enter_password = str(input("Please enter your password: "))
            if enter_password == i.password:
                print(f'''====================================================
                        Welcome, {i.name}. Your access level is: {i.post}
                        1. list_patients
                        2. view_records <patient_id>
                        3. add_record <patient_id>
                        4. remove_record <patient_id> <record_id>
                        5. exit
                        ====================================================
                        ''')
                while not exit_game_doctor:
                    input_num = int(input("What would you like to do? "))
                    if input_num == 1:
                        hospital1.list_patients()
                    elif input_num == 2:
                        input_num2 = int(input("Enter patient number: "))
                        hospital1.view_records(input_num2)
                    elif input_num == 3:
                        input_num2 = int(input("Enter patient number: "))
                        hospital1.add_records(input_num2)
                    elif input_num == 4:
                        input_num2 = int(input("Enter patient number: "))
                        hospital1.delete_records(input_num2)
                    elif input_num == 5:
                        break
                    elif input == None:
                        print("NO ITCHY HAND PRESS ENTEr\n")
                    else:
                        print("INVALID INPUT NUMBER\n")
            else:
                print("INCORRECT PASSWORD\n")
    if not Found:
        print("There's no such username exists! SPY\n")

while not exit_game:
    welcome()
    input_welcome = int(input("Select Options: "))

    ## Patient login
    
    if input_welcome == 1:
        patient_login()

    ## Employee login
    elif input_welcome == 2:
        employee_login()

    ## Admin login to be continued
    elif input_welcome == 3:
        employee_login()

    elif input_welcome == 4:
        exit_game = True

    elif input == " ":
        print("NO ITCHY HAND PRESS ENTEr\n")

    else:
        print("invalid number or character or something")

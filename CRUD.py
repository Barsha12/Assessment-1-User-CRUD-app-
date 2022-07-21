import  smtplib

User = []

# Class Users
class Users:
    
    id_count = 1
    def __init__(self, name,program, contact_number, Email_ID,  id=id_count):
        
        self.__id = Users.id_count + 1
        self.__name = name
        self.__program = program
        self.__contact_number = contact_number
        self.__Email_ID = Email_ID
        
          
    def set_id(self,id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_program(self,program):
        self.__program = program
    def set_contact_number(self,contact_number):
        self.__contact_number = contact_number
    def set_Email_ID(self,Email_ID):
        self.__Email_ID = Email_ID
    
    
    def get_name(self):return self.__name
    def get_program(self): return self.__program
    def get_contact_number(self):return self.__contact_number
    def get_Email_ID(self):return self.__Email_ID
    def get_id(self): return self.__id
    

    
    
    def __repr__(self):
        return self.__id + self.__name  + self.__program + self.__contact_number + self.__Email_ID 



        
# function to display the available programs

def displayPrograms():

    print(""" Available Programs are listed below :
            1. Python
            2. Java
            3. React JS
            4. C #
            
            
                """)


# function to register for the program

def register():
    Programs = ['Python','Java', 'React JS','C#']
    Users.set_id = Users.id_count
    Users.set_name = input("Enter your name :")
    programs = input(""" Enter your program of interest from available options :
            1. Python
            2. Java
            3. React JS
            4. C #
            
            
                """)
    if programs not in Programs : 
                    print("Program not available")
                    programA=input("Re-enter your program :")
                    Users.set_program = programA
    else :
        Users.set_program = programs
    

    Contact_Number = input("Enter your Contact number : ")
    if not (len(Contact_Number) == 10 and Contact_Number.isdigit()): # Contact Number Validation
        print ( "Invalid Number !!!" )
        CorrectNum = input("Re-enter your Number")
        Users.set_contact_number = CorrectNum
    else:
        Users.set_contact_number = Contact_Number

    EmailId = input("Enter your E-mail Address : ")
    Users.set_Email_ID = EmailId
    
    
    User.append([Users.set_id,Users.set_name, Users.set_program,Users.set_contact_number, Users.set_Email_ID])
    file = open("file.txt", 'w')
    for instances in User:
        file.writelines(str(instances) + "\n")
    file.close()

    #### Send the confirmation mail of registration ### 

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('insight.ws56@gmail.com','zyji ugbv uegl rshz')
    server.sendmail('insight.ws56@gmail.com',EmailId,'Your registration confirmed')
    
    print('mail sent')
    print("The records has been saved to a file")


#Function to Update the details     



def update_details():
    update_req = int(input("Enter your contact number for security : "))
    print("""
                    a. Enter "Name" to update your Name
                    b. Enter "Program" to update Program
                    c. Enter "Contact Number" to update Contact Number
                    d. Enter "Email_ID" to update Email_ID
                   
            """)
    update_col = input("What do you want to update : ") 
    
    for values in User:
        if update_req == int(values[3]):
            if update_col == "Name":
                values[1] = input("Enter new name : ")
                print(update_col + " has been updated")
            elif update_col == "Program":
                values[2] = input("Enter new program : ")
                print(update_col + " has been updated")
            elif update_col == "Contact Number":
                values[3] = input("Enter new Contact Number : ")
                print(update_col + " has been updated")
            elif update_col == "Email_ID":
                values[3] = input("Enter new Email_ID : ")
                print(update_col + " has been updated")
            else :
                print('Invalid Details')
            
    
    file = open("file.txt", 'w')
    for r in User:
        file.writelines(str(r) + "\n")        
    file.close()   

#Function to Delete the Record


def delete_details():
    del_Key = int(input("Enter your Contact number for security: "))
    
    
    for row in User:
        
        if del_Key == int(row[3]):
            User.remove(row)
        elif del_Key not in User:
            input("Record doesn't exist, Please enter correct number to continue :")
            continue;

        
    print("Your record has been deleted" )    
    
    file = open("file.txt", 'w')
    for r in User:
        file.writelines(str(r) + "\n")        
    file.close()   





  

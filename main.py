import sys
import CRUD

class UserInterface():
    def __init__(self):
        pass

    def mainMenu(self):
        done = False
        while done == False:
            print("""##################    Welcome to Insight Workshop Registration Page  ##############################
            
            1. Register for the program
            2. Display all programs
            3. Update Details
            4. Delete Details
            5. Exit
            
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                CRUD.register()
            elif choice == 2:
                CRUD.displayPrograms()
            elif choice == 3:
                CRUD.update_details()
            elif choice == 4:
                CRUD.delete_details() 
            elif choice == 5:
                done = True
            
            
            
            
                

obj = UserInterface()
obj.mainMenu()

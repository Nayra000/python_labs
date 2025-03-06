from auth_system import register_user, login_user
from projects_management import create_project, view_projects, edit_project, delete_project,searchByDate

import os

# Clear terminal based on the operating system
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

user ={}

def auth():
    global user  
    print("\n1. Register\n2. Login")
    choice = input("Choose an option: ")

    if choice == "1":
        user = register_user()
        return False
    elif choice == "2":
        user = login_user()
        return False
    else:
        print("Invalid choice!")

def returnToOptions():
    choice = ""
    while choice != "y" :
        choice = input("Do you want to return to options? (y/n): ")
        if choice == "y":
            return True

    


def project_management():
    # global user
    print("\n1.Create Project\n2. View Projects\n3. Edit Project\n4. Delete Project\n5. Search Projects\n6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        clear_terminal()
        create_project(user["id"])
        returnToOptions()
    elif choice == "2":
        clear_terminal()
        view_projects(user["id"])
        returnToOptions()
    elif choice == "3":
        clear_terminal()
        edit_project(user["id"])
        returnToOptions()
    elif choice == "4":
        clear_terminal()
        delete_project(user["id"])
        returnToOptions()
    elif choice == "5":
        clear_terminal()
        searchByDate(user["id"])
        returnToOptions()
    elif choice == "6":
        clear_terminal()
        print("Goodbye!")
        return False
    else:
        print("Invalid choice!")

    return True
def main():

    flag = True
    while flag:
        clear_terminal()
        print("Welcome to Project Management System!")
        flag=auth()
    if(user):
        flag = True
        print(user)
        while flag:
            clear_terminal()
            flag = project_management()
        
    

if __name__ == "__main__":
    main()

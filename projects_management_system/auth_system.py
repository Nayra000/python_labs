import json
import os
import re
import uuid


FILE_PATH = "users.json"

def load_users():
    global FILE_PATH
    """Load existing users from the JSON file."""
    if not os.path.exists(FILE_PATH):  
        return []
    
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)  
        except json.JSONDecodeError:
            return []  

def save_users(users):
    """Save users to the JSON file."""
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def validate_phone(phone):
    pattern = r"^(01)[0-25][0-9]{8}$" 
    return bool(re.match(pattern, phone))  # Ensure it returns True/False

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))  # Ensure it returns True/False

def confirm_password(password, confirm):
    return password == confirm

def validate_password(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*[^A-Za-z0-9]).{8,}$"
    return bool(re.match(pattern, password))

def register_user():
    users = load_users()
    user = {} 
    user["first_name"] = input("First Name: ")
    user["last_name"] = input("Last Name: ")
    user["email"] = input("Email: ")
    user["password"] = input("Password: ")
    confirm = input("Confirm Password: ")  # Renamed variable
    user["mobile_phone"] = input("Mobile Phone: ")

    if not validate_password(user["password"]):
        print("Password length should be at least 8 characters and contain at least one letter and one special character!")
        return None

    if not confirm_password(user["password"], confirm):
        print("Passwords do not match!")
        return None

    if not validate_phone(user["mobile_phone"]):
        print("Invalid phone number!")
        return None
    
    if not validate_email(user["email"]):
        print("Invalid email!")
        return None
    user["id"] =str(uuid.uuid4()) 
    users.append(user)
    save_users(users)
    return user


def login_user():
    users = load_users()
    email = input("Email: ")
    password = input("Password: ")
    for user in users:
        print(user)
        if user["email"] == email and user["password"] == password:
            print("Login successful!")
            return user
    print("Login failed!")





    



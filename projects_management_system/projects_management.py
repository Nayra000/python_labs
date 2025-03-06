import json
import os
from datetime import datetime
import uuid

FILE_PATH = "projects.json"

def load_projects():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_projects(projects):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(projects, file, indent=4)

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please enter dates in YYYY-MM-DD format.")
        return None

def validateFloat(value):
    try:
        return float(value)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None

def create_project(user_id):
    projects = load_projects()
    project = {}

    project["title"] = input("Project Title: ")
    project["details"] = input("Project Details: ")
    project["total_target"] = validateFloat(input("Total Target (EGP): "))
    project["start_date"] = validate_date(input("Start Date (YYYY-MM-DD): "))
    project["end_date"] = validate_date(input("End Date (YYYY-MM-DD): "))

    if project["end_date"] <= project["start_date"]:
        print("End date must be after start date!")
        return
    project["user_id"] = user_id
    project["id"] = str(uuid.uuid4())

    projects.append(project)
    save_projects(projects)
    print("Project created successfully!")

def view_projects(user_id, filter_func=None):
    projects = load_projects()
    if not projects:
        print("No projects available!")
        return
    found = False
    for project in projects:
        if project["user_id"] == user_id and (filter_func is None or filter_func(project)):
            found = True
            print(f"ID: {project['id']}")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']} EGP")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print("-" * 30)
    if not found:
        print("No projects found!")

 

def edit_project(user_id):
    projects = load_projects()
    if not projects:
        print("No projects available!")
        return
    found = False
    for project in projects:
        if project["user_id"] == user_id:
            found = True
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']} EGP")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print("-" * 30)

            choice = input("Do you want to edit this project? (y/n): ").strip().lower()
            if choice == "y":
                new_title = input("Project Title (press Enter to keep current): ").strip()
                new_details = input("Project Details (press Enter to keep current): ").strip()
                new_total_target = validateFloat(input("Total Target (EGP) (press Enter to keep current): ").strip())
                new_start = validate_date(input("Start Date (YYYY-MM-DD) (press Enter to keep current): ").strip())
                new_end = validate_date(input("End Date (YYYY-MM-DD) (press Enter to keep current): ").strip())

                project["total_target"] = new_total_target if new_total_target else project["total_target"]
                project["start_date"] = new_start if new_start else project["start_date"]
                project["end_date"] = new_end if new_end else project["end_date"]
                project["title"] = new_title if new_title else project["title"]
                project["details"] = new_details if new_details else project["details"]

                save_projects(projects)
                print("Project updated successfully!")
                return
    
    if not found:
        print("No projects found!")


def delete_project(user_id):
    projects = load_projects()
    if not projects:
        print("No projects available!")
        return
    view_projects(user_id)
    project_id = input("Enter the ID of the project you want to delete: ")
    if not project_id:
      print("Invalid ID!")
      return
    for project in projects:
        if project["id"] == project_id and project["user_id"] == user_id:
            projects.remove(project)
            save_projects(projects)
            print("Project deleted successfully!")
            return
    print("Project not found or you do not have permission to delete it!")




def searchByDate(user_id):
    projects = load_projects()
    if not projects:
        print("No projects available!")
        return

    
    date = validate_date(input("Enter the date (YYYY-MM-DD) to search for: "))
    if not date:
      return
    view_projects(user_id, lambda p: p["start_date"] == date or p["end_date"] == date)


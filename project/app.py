import json
import os
from rich.console import Console # type: ignore
from rich.table import Table # type: ignore

# Initialize the library
console = Console()
FILE_NAME = "students.json"

# --- 1. FILE HANDLING ---

def load_data():
    """Reads data from the file."""
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(students):
    """Saves the list to the file."""
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# --- 2. FEATURES ---

def add_student():
    console.print("\n--- Add New Student ---")
    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")

    new_student = {"name": name, "age": age, "course": course}

    students = load_data()
    students.append(new_student)
    save_data(students)
    
    console.print(f"Success! Added {name}.")

def list_students():
    students = load_data()
    
    # Create a simple table without colors
    table = Table(title="Student Records")
    
    table.add_column("Name")
    table.add_column("Age")
    table.add_column("Course")

    for s in students:
        table.add_row(s["name"], s["age"], s["course"])

    console.print(table)

def search_student():
    name_to_find = input("Enter name to search: ").lower()
    students = load_data()
    
    found = False
    for s in students:
        if name_to_find in s["name"].lower():
            console.print(f"Found: {s['name']} (Age: {s['age']}, Course: {s['course']})")
            found = True
    
    if not found:
        console.print("No student found.")

# --- 3. MAIN LOOP ---

def main():
    while True:
        console.print("\nMENU")
        console.print("1. Add Student")
        console.print("2. List Students")
        console.print("3. Search")
        console.print("4. Exit")
        
        choice = input("Choose (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            console.print("Goodbye!")
            break

if __name__ == "__main__":
    main()
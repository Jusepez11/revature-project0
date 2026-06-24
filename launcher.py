import subprocess
import os
programs = {1:["python","employee_app/employee_terminal.py"],2:["java", "manager_app/manager_terminal.java"]}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = input("1. Employee App\n""2. Manager App\n""Choice: ")
    try:
        choice = int(choice)
        if choice == 1 or choice == 2:
            subprocess.run(["python", "employee_app/db/seed.py"])
            language = programs[choice][0]
            location = programs[choice][1]

            os.system('cls' if os.name == 'nt' else 'clear')
            subprocess.run([language, location])
        else:
            print("\nInvalid input. Please enter a valid number.")

    except ValueError:
            print("\nInvalid input. Please enter a valid number.")

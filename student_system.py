import os

'''
Documentation:
students == 2 dimensional list
s == 1 dimensional with each student info, single list inside the student list

'''

#display menu, return user' selection
def print_menu():
    print("*************************************************************")
    print("{:>50}".format("*** Welcome to Students GPA Systems! ***"))
    print("*************************************************************")
    print("Select from the following options")
    print("L- List Students\nA- Add Student\nE- Edit Students\nD- Delete Student\nF- Find A Student\nG- GPA Average\nQ- Quit")
    ask = input(">>> ").upper()
    return ask

#receive a list of a student’s information, return CSV formatted string
def format_student(s):
    return f"{s[0]},{s[1]},{s[2]}\n"

#no parameters, display header, no return
def display_std_header():
    print("=============================================================")
    print("{:>15} {:>18} {:>16}".format("Student Name", "Student ID", "GPA"))
    print("=============================================================")

#receive student info, display student info, no return
def display_student(s):
    print("{:>15} {:>15} {:>20}".format(s[0], s[1], s[2]))

#receive the student ID and the students list, return student info
def find_student(students, id):
    for s in students:
        if id == s[1]:
            return s

#receive student list, no return and check if empty or not
def list_students(students):
    if students == None :
        print("Students list has no students")
    else:
        display_std_header()
        for s in students:
            display_student(s)

#receive file name and student list, no return, ask user id and check then update to text file
def add_student(file_name, students):
    with open(file_name, "a") as file: 
        print("Adding a student .....")
        id = int(input("Enter student id: ")) 

        s = find_student(students, id)

        if s != None and id == s[1]:
            print(f"A student with ID {id} already exists")
        else:
            name = input("Enter student name: ")
            gpa = float(input("Enter student GPA: "))
            students.append([name, id, gpa])
            update_students(file_name, students)
            print(f"The student with id {id} is added.")

#receive student id and student list, no return
def edit_student(id, students): 
    #find the student using find_student function, then ask for info to change
    s = find_student(students, id)   
    e_name = input("Enter student name: ")
    e_id = int(input("Enter student ID: "))
    e_gpa = float(input("Enter GPA: "))
    s[0] = e_name
    s[1] = e_id
    s[2] = e_gpa

#receive student info and student list, no return
def delete_student(s, students):
    students.remove(s)

#receive student list, return calculated average rounded
def calculate_average(students):
    #calc
    sum = 0
    for s in students:
        gpa = s[2]
        sum += gpa
    average = sum/len(students)
    return round(average, 2)

#receive text file, return 2 dimensional students list
def load_students(file_name):
    s = []
    with open(file_name, "r") as file:
        for line in file:
            student = line.strip().split(",")
            student[1] = int(student[1])
            student[2] = float(student[2])
            s.append(student)
    return s

#receive text file name, format to CSV then write to text file, no return
def update_students(file_name, students):
        with open(file_name, 'w') as file:
            for s in students:
                line = format_student(s)
                file.write(line)

#call all other functions
def main():
    #check for the file exist or not
    while True:
        file_name = input("Please enter the file name to load students' information: ")
        if os.path.exists(file_name):
            students = load_students(file_name)
            print("Students information has been loaded from the file")
            break
        else:
            print(f"{file_name} does not exist - Bye")
            continue

    #loop for all program with selection
    while True:
        choice = print_menu()
        if choice == "L": 
            list_students(students)
            continue
        elif choice == "A":
            add_student(file_name, students)
            continue
        elif choice == "E":
            #check whether the student exists or not before calling function.
            id = int(input("Enter student id: "))
            s = find_student(students, id)
            #call function if student exists
            if s in students:
                edit_student(id, students)
                update_students(file_name, students)
                continue
            else:
                print(f"No student with ID {id}")
                continue
        elif choice == "D":
            #check whether the student exists or not before calling function.
            id = int(input("Enter student id: "))
            s = find_student(students, id)
            #call function if student exists
            if s in students:
                delete_student(s, students)
                update_students(file_name, students)
                print(f"Student with ID {id} is deleted")
                continue
            else:
                print(f"No student with ID {id}")
                continue
        elif choice == "F":
            id = int(input("Enter student id: "))
            s = find_student(students, id)
            #call function if student exists
            if s in students:
                display_std_header()
                display_student(s)
                continue
            else:
                print(f"No student with ID {id}")
                continue
        elif choice == "G":
            average_gpa = calculate_average(students)
            print(f"GPA Average is {average_gpa}")
            continue
        elif choice == "Q":
            print("Thanks and Good Bye!")
            print("Please press enter to continue....")
            break
        else:
            print("Invalid Input")
            continue

if __name__ == "__main__":
    main()
sl = []

class students:
    def __init__(self, n, a, s, r):
        self.name = n
        self.age = a
        self.sec = s
        self.rollno = r

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Class:", self.sec)
        print("Roll no:", self.rollno)
        print("---------------------")

print("                             Welcome")
print("          -Here you can add the details of the students-\n")

ns = int(input("-Number of students you want to add details of: "))

for i in range(ns):
    print(f"Enter details for student {i + 1}:")
    name = input("NAME: ")
    age = int(input("AGE: ")) 
    sec = input("CLASS: ")
    rollno = int(input("ROLL NO: "))  
    print("---------------------")
    s = students(name, age, sec, rollno)
    sl.append(s)

print("\n                  ******All Student Details******")
for student in sl:
    student.display()

c = input("Do you want to change anything?\nIf yes, press 'y'\nIf no, enter 'exit': ")

if c == 'y':
    ws = int(input("Enter the roll number of the student whose details you want to change: "))
    
    for student in sl:
        if student.rollno == ws:
            print("What do you want to change?")
            print("1. Name")
            print("2. Age")
            print("3. Class")
            print("4. Roll number")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                student.name = input("Enter new name: ")
            elif choice == '2':
                student.age = int(input("Enter new age: "))
            elif choice == '3':
                student.sec = input("Enter new class: ")
            elif choice == '4':
                student.rollno = int(input("Enter new roll number: "))
            else:
                print("Invalid choice.")

            print("\n            --- Updated Details ---")
            student.display()
            break
    else:
        print("No student found with that roll number.")

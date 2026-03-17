students = {}
def add_student(name,marks):
    students[name]= marks
    print("student added")
def display_students():
    for name,marks in students.items():
        print(name,":",marks)
add_student("ramya",85)
add_student("joyce",88)
display_students()
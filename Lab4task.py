students_list = []
students_dict = {}

name = input("Enter student's name:")
age = input("Enter student's age:")
grade = input("Enter student's grade:")
students_list.append(name)
students_dict[name] = {'age': age ,'grade': grade }
print("Student information added successfully")


print("Student details:")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

# searching
    name = input("Enter student name to search: ")
    if name in students_dict:
        print(f"Name: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
    else:
        print("Student not found.")

# removing students
    name = input("Enter student name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")


num_students = int(input("Enter number of students: "))

students = {}

for i in range(num_students):
    print(f"\nStudent {i + 1}:")
    name = input("Enter name: ")
 
    grade1 = float(input("Enter grade for subject 1: "))
    grade2 = float(input("Enter grade for subject 2: "))
    grade3 = float(input("Enter grade for subject 3: "))
     

    average = (grade1 + grade2 + grade3) / 3
        
    print(f"{name}'s average is: {average}")

    students[name] = average

    print("\nStudent Average: ", average)
for name, avg in students.items():
    print(f"{name} -> {avg}")
    
highest = max(students, key=students.get)
lowest = min(students, key=students.get)


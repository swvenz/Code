
grades = {"Ana": 90, 
          "Ben": 85, 
          "Carla": 93, 
          "David": 88, 
          "Ella": 95
          }

fruit = {
    'apple': 20,
    'banana': 38,
    'grape': 25,
    'berry': 35
}

#ask for name
print("Student Names: Ana, Ben, Carla, David, Ella")
name = input(str("Enter a student's name given above: "))

print('available fruits: apple, banana, grape, berry')
choice = input(str('Which fruit: '))

#check
if name in grades:
    print(f"{name} 's grade is {grades[name]}")
else:
     print(f'{name} is not on the list')
     
if choice in fruit:
    print(f"{choice} cost {fruit[choice]} pesos per piece")
else:
    print(f"{choice} is not available")
    
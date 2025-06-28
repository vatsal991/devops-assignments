marks ={
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}

def update_marks():

    name = input("Enter the name of the student: ")
    score = input(f"Enter the mark of {name}: ")
  
    marks[name] = score

update_marks()
print(f"Updated list \n {marks}")
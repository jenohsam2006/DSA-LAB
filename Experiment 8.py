TABLE_SIZE = 10
class HashTable:
    def __init__(self):
        self.table = [None] * TABLE_SIZE
    def hash_function(self, key):
        return key % TABLE_SIZE
    def insert(self, emp_id, name):
        index = self.hash_function(emp_id)
        print(f"Insert ({emp_id}, {name}) → h({emp_id}) = {index}", end="")
        if self.table[index] is None:
            self.table[index] = (emp_id, name)
            print(f" → Placed at index {index}")
        else:
            print(f" → Collision at index {index}", end="")
            original_index = index
            while self.table[index] is not None:
                index = (index + 1) % TABLE_SIZE
                if index == original_index:
                    print("\nHash Table Full! Cannot insert.")
                    return
            self.table[index] = (emp_id, name)
            print(f" → Next free index {index} → Placed at index {index}")
    def search(self, emp_id):
        index = self.hash_function(emp_id)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == emp_id:
                print(f"Search({emp_id}) → Found at index {index} → Name: {self.table[index][1]}")
                return
            index = (index + 1) % TABLE_SIZE
            if index == start_index:
                break
        print(f"Search({emp_id}) → Not found")
    def display(self):
        print("\nFinal Hash Table:")
        print("Index\tEmployeeID\tName")
        for i in range(TABLE_SIZE):
            if self.table[i] is not None:
                print(f"{i}\t{self.table[i][0]}\t\t{self.table[i][1]}")
            else:
                print(f"{i}\t-\t\t-")
hash_table = HashTable()
n = int(input("Enter number of employees: "))
print("\nEnter Employee details (ID and Name):")
for i in range(n):
    emp_id = int(input(f"Employee {i+1} ID: "))
    name = input(f"Employee {i+1} Name: ")
    hash_table.insert(emp_id, name)
hash_table.display()
print("\nSearch Operation:")
while True:
    choice = input("Do you want to search for an employee? (yes/no): ").lower()
    if choice == "no":
        break
    emp_id = int(input("Enter Employee ID to search: "))
    hash_table.search(emp_id)




def insertion_sort(students):
    print("\nInsertion Sort Process (Descending Order of Marks):\n")
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0 and students[j][2] < key[2]:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key
        current_marks = [s[2] for s in students[:i+1]]
        print(f"Step {i}: {current_marks}")
n = int(input("Enter number of students: "))
students = []
print("\nEnter student details (RollNo, Name, Marks):")
for i in range(n):
    roll = int(input(f"Student {i+1} RollNo: "))
    name = input(f"Student {i+1} Name: ")
    marks = int(input(f"Student {i+1} Marks: "))
    students.append((roll, name, marks))
print("\nBefore Sorting:")
print("RollNo\tName\tMarks")
for roll, name, marks in students:
    print(f"{roll}\t{name}\t{marks}")
insertion_sort(students)
print("\nAfter Sorting:")
print("RollNo\tName\tMarks")
for roll, name, marks in students:
    print(f"{roll}\t{name}\t{marks}")






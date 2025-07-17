class Stack:
    def __init__(self,size):
        self.top = -1
        self.max = size
        self.list = [None]*size

    def isfull(self):
        return self.top == self.max-1

    def push(self,data):
        if self.isfull():
            print("Stack Overflow")
        else:
            self.top += 1
            self.list[self.top] = data
            print(f"Page '{data}' visited successfully.")

    def isempty(self):
        return self.top == -1

    def pop(self):
        if self.isempty():
            print("Stack Undertaken")
        else:
            a = self.list[self.top]
            del self.list[self.top]
            self.top -= 1
            print(f"Going back from '{a}'.")
   
    def display(self):
        for i in range(self.top+1):
            print(f"{i+1}. {self.list[i]}")
            
s = int(input("Enter maximum navigation history size (stack size) : "))
web = Stack(s)
while True:
    print('\n--- Web Browser Navigation Menu ---')
    print('-------------------------------------')
    print("1. Visit a New Page")
    print("2. Go Back to Previous Page")
    print("3. Display Navigation History")
    print("4. Exit")
    print('-------------------------------------')
    ch = input("Enter your choice from menu : ")

    if ch == '1':
        data = input("Enter the new page : ")
        web.push(data)
    elif ch == '2':
        web.pop()
        web.display()
    elif ch == '3':
        web.display()
    elif ch == '4':
        print("Exiting the browser navigation simulation.")
        break
    else:
        print("Invalid choice. Please select between 1-4.")

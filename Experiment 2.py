
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    return c in "+-*/^"

def infix_to_postfix(expression):
    stack = []  
    postfix = '' 

    for char in expression:
        if char.isalnum(): 
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() 
        elif is_operator(char):
            while (stack and precedence(stack[-1]) >= precedence(char)):
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix

infix_expr = input("Enter infix expression: ") 
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix expression:", postfix_expr)



def text_editor():
    text = ""               
    undo_stack = []       

    while True:
        print("\nCurrent text:", text)
        print("1. Add Text")
        print("2. Delete Last n Characters")
        print("3. Undo Last Operation")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            undo_stack.append(text)  
            new_text = input("Enter text to add: ")
            text += new_text
        elif choice == '2':
            undo_stack.append(text) 
            try:
                n = int(input("Enter number of characters to delete: "))
                text = text[:-n]
            except:
                print("Invalid input")
        elif choice == '3':
            if undo_stack:
                text = undo_stack.pop()
                print("Undo successful.")
            else:
                print("Nothing to undo.")
        elif choice == '4':
            print("Exiting editor...")
            break
        else:
            print("Invalid choice. Try again.")
text_editor()

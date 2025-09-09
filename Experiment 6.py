class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(pos - 1):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if not self.head:
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(pos - 1):
            if not temp.next:
                print("Position out of range")
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def push(self, data):  
        self.insert_at_beginning(data)

    def pop(self):          
        if self.head:
            popped = self.head.data
            self.head = self.head.next
            return popped
        return None

    def enqueue(self, data):   
        self.insert_at_end(data)

    def dequeue(self):        
        if self.head:
            removed = self.head.data
            self.head = self.head.next
            return removed
        return None

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head

    def sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def split(self, pos):
        if pos == 0:
            new_list = SinglyLinkedList()
            new_list.head = self.head
            self.head = None
            return new_list

        temp = self.head
        for _ in range(pos - 1):
            if not temp:
                print("Position out of range")
                return None
            temp = temp.next

        new_list = SinglyLinkedList()
        new_list.head = temp.next
        temp.next = None
        return new_list

if __name__ == "__main__":
    ll = SinglyLinkedList()

    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Position")
        print("7. Delete by Value")
        print("8. Search")
        print("9. Display")
        print("10. Push (Stack)")
        print("11. Pop (Stack)")
        print("12. Enqueue (Queue)")
        print("13. Dequeue (Queue)")
        print("14. Sort List")
        print("15. Split List")
        print("16. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value: "))
            ll.insert_at_beginning(val)

        elif choice == 2:
            val = int(input("Enter value: "))
            ll.insert_at_end(val)

        elif choice == 3:
            val = int(input("Enter value: "))
            pos = int(input("Enter position (0-based): "))
            ll.insert_at_position(val, pos)

        elif choice == 4:
            ll.delete_at_beginning()

        elif choice == 5:
            ll.delete_at_end()

        elif choice == 6:
            pos = int(input("Enter position (0-based): "))
            ll.delete_at_position(pos)

        elif choice == 7:
            val = int(input("Enter value to delete: "))
            ll.delete_by_value(val)

        elif choice == 8:
            val = int(input("Enter value to search: "))
            print("Found!" if ll.search(val) else "Not found!")

        elif choice == 9:
            ll.display()

        elif choice == 10:
            val = int(input("Enter value to push (Stack): "))
            ll.push(val)

        elif choice == 11:
            popped = ll.pop()
            print("Popped:", popped if popped is not None else "Stack is empty")

        elif choice == 12:
            val = int(input("Enter value to enqueue (Queue): "))
            ll.enqueue(val)

        elif choice == 13:
            removed = ll.dequeue()
            print("Dequeued:", removed if removed is not None else "Queue is empty")

        elif choice == 14:
            ll.sort()
            print("List sorted!")

        elif choice == 15:
            pos = int(input("Enter position to split at (0-based): "))
            second_half = ll.split(pos)
            print("First half:")
            ll.display()
            print("Second half:")
            if second_half:
                second_half.display()

        elif choice == 16:
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")

class CanteenQueue:
    def __init__(self, length):
        self.length = length              
        self.queue = []                  
        self.served = []                
        self.front = 0
        self.rear = -1
        self.serve_count = 0
        self.token_number = 1           

    def isempty(self):
        return self.serve_count == 0

    def isfull(self):
        return (self.rear - self.front + 1) >= self.length

    def enqueue(self, count):
        print(f"\nAdding {count} students to queue with auto tokens...")
        for _ in range(count):
            self.rear += 1
            # Expand queue manually since we can't use append()
            if self.rear >= len(self.queue):
                self.queue += [0] * (self.rear - len(self.queue) + 1)
            self.queue[self.rear] = self.token_number
            self.token_number += 1
        print("Students added to queue.")

    def serve_students(self):
        available = self.rear - self.front + 1
        if available < self.length:
            print("Not enough students to serve.")
            return
        self.serve_count = 0
        print("\nServing students:")
        for i in range(self.length):
            # Expand served list manually
            if self.serve_count >= len(self.served):
                self.served += [0] * (self.serve_count - len(self.served) + 1)
            self.served[self.serve_count] = self.queue[self.front]
            print("Served Token:", self.served[self.serve_count])
            self.front += 1
            self.serve_count += 1

    def dequeue(self):
        if self.isempty():
            print("No students served yet.")
        else:
            print("Last served tokens:")
            for i in range(self.serve_count):
                print(self.served[i], end=" ")
            print()

    def display(self):
        if self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Current queue tokens:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

print("=== Canteen Token Queue System ===")
length = int(input("Enter number of students to serve at a time: "))
canteen = CanteenQueue(length)
while True:
    print("\n--- MENU ---")
    print("1. Add students to queue")
    print("2. Serve students")
    print("3. Show last served students")
    print("4. Display current queue")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        n = int(input("Enter number of new students to add: "))
        canteen.enqueue(n)
    elif choice == '2':
        canteen.serve_students()
    elif choice == '3':
        canteen.dequeue()
    elif choice == '4':
        canteen.display()
    elif choice == '5':
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")

class CanteenQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.max_capacity = max_capacity
        self.token_counter = 1

    def initialize_queue(self, n):
        print(f"\nInitializing queue with {n} students...")
        for _ in range(n):
            if len(self.queue) < self.max_capacity:
                self.queue.append(self.token_counter)
                self.token_counter += 1
            else:
                print("Queue is full! Cannot add more students.")
                break
        self.display_queue()

    def serve_students(self, count):
        print(f"\nServing {count} students...")
        for _ in range(count):
            if self.queue:
                served = self.queue.pop(0)
                print(f"Token {served} served.")
            else:
                print("Queue is empty.")
                break
        self.display_queue()

    def add_new_students(self, num_new_students):
        print(f"\nAdding {num_new_students} new students...")
        for _ in range(num_new_students):
            if len(self.queue) < self.max_capacity:
                self.queue.append(self.token_counter)
                print(f"Token {self.token_counter} added.")
                self.token_counter += 1
            else:
                print(f"Queue Overflow! Cannot add token {self.token_counter}.")
                break
        self.display_queue()

    def display_queue(self):
        print("Current Queue:", self.queue if self.queue else "Empty")

def main():
    print("=== Canteen Token Queue System ===")
    max_capacity = int(input("Enter the maximum queue capacity: "))
    canteen = CanteenQueue(max_capacity)

    while True:
        print("\n--- MENU ---")
        print("1. Initialize queue")
        print("2. Serve students")
        print("3. Add new students")
        print("4. Display current queue")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            n = int(input("Enter number of students to initialize: "))
            canteen.initialize_queue(n)

        elif choice == '2':
            count = int(input("Enter number of students to serve: "))
            canteen.serve_students(count)

        elif choice == '3':
            new_students = int(input("Enter number of new students to add: "))
            canteen.add_new_students(new_students)

        elif choice == '4':
            canteen.display_queue()

        elif choice == '5':
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()



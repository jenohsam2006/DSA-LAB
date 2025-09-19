class Node:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority
        self.prev = None
        self.next = None

class TaskScheduler:
    def __init__(self):
        self.head = None
        self.tail = None
        self.priority_order = {"High": 3, "Medium": 2, "Low": 1}

    def add_task(self, task_id, priority):
        new_node = Node(task_id, priority)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_front(self, task_id, priority):
        new_node = Node(task_id, priority)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_task(self, task_id):
        current = self.head
        while current:
            if current.task_id == task_id:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                print(f"Task {task_id} deleted.")
                return
            current = current.next
        print(f"Task {task_id} not found!")

    def display_high_to_low(self):
        if not self.head:
            print("No tasks available.")
            return

        tasks = []
        current = self.head
        while current:
            tasks.append((current.task_id, current.priority))
            current = current.next

        tasks.sort(key=lambda x: self.priority_order[x[1]], reverse=True)

        print("Tasks High to Low:", " -> ".join([f"{tid}-{p}" for tid, p in tasks]))

    def display_low_to_high(self):
        if not self.head:
            print("No tasks available.")
            return

        tasks = []
        current = self.head
        while current:
            tasks.append((current.task_id, current.priority))
            current = current.next

        tasks.sort(key=lambda x: self.priority_order[x[1]])

        print("Tasks Low to High:", " -> ".join([f"{tid}-{p}" for tid, p in tasks]))

if __name__ == "__main__":
    scheduler = TaskScheduler()

    while True:
        print("\n--- Task Scheduler Menu ---")
        print("1. Add a task at the end")
        print("2. Insert high-priority task at the front")
        print("3. Delete a completed task by ID")
        print("4. Display tasks High to Low")
        print("5. Display tasks Low to High")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            tid = input("Enter Task ID: ")
            priority = input("Enter Priority (High/Medium/Low): ")
            scheduler.add_task(tid, priority)
        elif choice == "2":
            tid = input("Enter Task ID: ")
            priority = input("Enter Priority (High/Medium/Low): ")
            scheduler.insert_front(tid, priority)
        elif choice == "3":
            tid = input("Enter Task ID to delete: ")
            scheduler.delete_task(tid)
        elif choice == "4":
            scheduler.display_high_to_low()
        elif choice == "5":
            scheduler.display_low_to_high()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

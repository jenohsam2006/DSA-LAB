class Product:
    def __init__(self, pid, name, price):
        self.id = pid
        self.name = name
        self.price = price
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}"
class Inventory:
    def __init__(self):
        self.products = []
    def AddProduct(self, pid, name, price):
        self.products.append(Product(pid, name, price))
        self.products.sort(key=lambda x: x.id)
    def DisplayInventory(self):
        if not self.products:
            print("\nInventory is empty.")
            return
        print(f"\n{'ProductID':<10} {'Name':<15} {'Price':<10}")
        for p in self.products:
            print(f"{p.id:<10} {p.name:<15} {p.price:<10}")
    def LinearSearch(self, pid):
        comparisons = 0
        for product in self.products:
            comparisons += 1
            if product.id == pid:
                print(f"\nLinear Search:\nComparisons: {comparisons}")
                print(f"Product found: {product}")
                return
        print(f"\nLinear Search:\nComparisons: {comparisons}")
        print("Product not found.")
        
    def BinarySearch(self, pid):
        low, high = 0, len(self.products) - 1
        comparisons = 0
        while low <= high:
            mid = (low + high) // 2
            comparisons += 1
            if self.products[mid].id == pid:
                print(f"\nBinary Search:\nComparisons: {comparisons}")
                print(f"Product found: {self.products[mid]}")
                return
            elif self.products[mid].id < pid:
                low = mid + 1
            else:
                high = mid - 1
        print(f"\nBinary Search:\nComparisons: {comparisons}")
        print("Product not found.")
inv = Inventory()
while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Search Product (Linear & Binary)")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = int(input("Enter Product Price: "))
        inv.AddProduct(pid, name, price)
        print("Product added successfully.")
    elif choice == "2":
        inv.DisplayInventory()
    elif choice == "3":
        if not inv.products:
            print("⚠ Inventory is empty. Add products first.")
        else:
            pid = int(input("Enter Product ID to search: "))
            inv.LinearSearch(pid)
            inv.BinarySearch(pid)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")

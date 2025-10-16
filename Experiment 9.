class Customer:
    def __init__(self, cid, name, amount):
        self.cid = cid
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.cid:<6}\t{self.name:<10}\t{self.amount}"

def merge_sort(customers):
    if len(customers) > 1:
        mid = len(customers) // 2
        left_half = customers[:mid]
        right_half = customers[mid:]

        print(f"Left half: {[c.amount for c in left_half]}")
        print(f"Right half: {[c.amount for c in right_half]}")

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].amount < right_half[j].amount:
                customers[k] = left_half[i]
                i += 1
            else:
                customers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            customers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            customers[k] = right_half[j]
            j += 1
            k += 1

        print(f"Merging {[c.amount for c in left_half]} and {[c.amount for c in right_half]} → {[c.amount for c in customers]}")

customers = []

n = int(input("Enter number of customers: "))
print("\nEnter customer details (CustomerID, Name, PurchaseAmount):")
for i in range(n):
    cid = int(input(f"Customer {i+1} ID: "))
    name = input(f"Customer {i+1} Name: ")
    amount = float(input(f"Customer {i+1} Purchase Amount: "))
    customers.append(Customer(cid, name, amount))
    print()

print("\nBefore Sorting:")
print("CustomerID\tName\t\tPurchaseAmount")
for c in customers:
    print(c)

print("\nMerge Sort Process:")
merge_sort(customers)

print("\nAfter Sorting (Ascending Order of Purchase Amount):")
print("CustomerID\tName\t\tPurchaseAmount")
for c in customers:
    print(c)

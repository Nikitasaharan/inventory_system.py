# Inventory Item class
class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(f"ID: {self.item_id}, Name: {self.name}, Qty: {self.quantity}, Price: {self.price}")


# Inventory Management System
class Inventory:
    def __init__(self):
        self.items = []   # array of items

    # Insert item
    def insert_item(self, item):
        self.items.append(item)
        print("Item added successfully")

    # Delete item by ID
    def delete_item(self, item_id):
        for i in range(len(self.items)):
            if self.items[i].item_id == item_id:
                del self.items[i]
                print("Item deleted successfully")
                return
        print("Item not found")

    # Search item by ID or Name
    def search_item(self, key):
        for item in self.items:
            if item.item_id == key or item.name == key:
                item.display()
                return
        print("Item not found")

    # Row-major and column-major display of price & quantity
    def price_quantity_table(self):
        n = len(self.items)
        table = [[self.items[i].price, self.items[i].quantity] for i in range(n)]

        print("\nRow-Major Order:")
        for row in table:
            print(row)

        print("\nColumn-Major Order:")
        for col in range(2):
            col_values = []
            for row in range(n):
                col_values.append(table[row][col])
            print(col_values)

    # Sparse representation for rarely restocked products (low quantity)
    def sparse_representation(self):
        sparse = []
        for i in range(len(self.items)):
            if self.items[i].quantity <= 2:  # rarely restocked
                sparse.append([i, self.items[i].item_id, self.items[i].quantity])
        print("\nSparse Representation (index, item_id, quantity):")
        for row in sparse:
            print(row)


#  Testing the Inventory System

store = Inventory()

# Add some items
item1 = Item(101, "Milk", 10, 40.5)
item2 = Item(102, "Bread", 2, 25.0)
item3 = Item(103, "Eggs", 1, 6.0)

store.insert_item(item1)
store.insert_item(item2)
store.insert_item(item3)

# Display items
print("\nAll Items:")
for it in store.items:
    it.display()

# Search item
print("\nSearch Result:")
store.search_item(102)
store.search_item("Eggs")

# Delete item
store.delete_item(101)

# Show price-quantity table
store.price_quantity_table()

# Sparse representation
store.sparse_representation()

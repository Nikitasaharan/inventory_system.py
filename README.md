# Inventory Management System – DSA Lab Assignment 1

## Problem Statement
The objective of this project is to design and implement an **Inventory Management System for a Grocery Store** using **array-based data structures** in Python.  

The system should:  
- Store details of each item (**Item ID, Item Name, Quantity, Price**)  
- Support operations like **insertion, deletion, and search**  
- Manage **price–quantity tables** using **row-major** and **column-major ordering**  
- Use a **sparse representation** for rarely restocked products  
- Perform **time and space complexity analysis** for each function  

## Features
- Add a new item to inventory  
- Delete an item by ID  
- Search item by ID or Name  
- Generate price-quantity table (row-major & column-major)  
- Sparse representation for items with very low quantity  
- Simple & beginner-friendly Python implementation  

## Implementation

### Data Structures Used
- **Array (Python List)** → to store items  
- **2D Array (Nested List)** → for price and quantity  
- **Sparse Matrix** → for rarely restocked items  

### Classes and Methods

**Class `Item`**  
- `__init__()` → initialize item details  
- `display()` → print item details  

**Class `Inventory`**  
- `insert_item(item)` → Add new item  
- `delete_item(item_id)` → Delete item by ID  
- `search_item(key)` → Search item by ID or Name  
- `price_quantity_table()` → Row-major & Column-major order display  
- `sparse_representation()` → Sparse storage for rarely restocked items  

## How to Run
1. Clone this repository or download the `.py` file.  
2. Open the project in **PyCharm** or any Python IDE.  
3. Run the file with:

## Screenshots 
<img width="755" height="909" alt="Screenshot 2025-09-27 121742" src="https://github.com/user-attachments/assets/917f7c2f-9324-4654-aa87-89952ac3a0f4" />

## Author
- Nikita Saharan
- 2401840008
- B.Sc. (h) Data Science 
- Introduction to Data Structures Lab Assignment 1 




# Create a FastAPI application for a restaurant menu system.
from fastapi import FastAPI

app = FastAPI()
menu = [
    {"name": "Spring Rolls", "price": 500.00, "category": "appetizer", "is_vegetarian": True},
    {"name": "Garlic Bread", "price": 400.00, "category": "appetizer", "is_vegetarian": True},
    {"name": "Chicken Wings", "price": 600.00, "category": "appetizer", "is_vegetarian": False},
    {"name": "Stuffed Mushrooms", "price": 700.00, "category": "appetizer", "is_vegetarian": True},
   
    {"name": "Grilled Chicken", "price": 1200.00, "category": "main_course", "is_vegetarian": False},
    {"name": "Beef Steak", "price": 1800.00, "category": "main_course", "is_vegetarian": False},
    {"name": "Veggie Burger", "price": 1000.00, "category": "main_course", "is_vegetarian": False},
    {"name": "Pasta Alfredo", "price": 1100.00, "category": "main_course", "is_vegetarian": False},
    {"name": "Fish and Chips", "price": 1300.00, "category": "main_course", "is_vegetarian": False},

    {"name": "Ice Cream", "price": 3000.00, "category": "dessert", "is_vegetarian": True},
    {"name": "Chocolate Cake", "price": 4000.00, "category": "dessert", "is_vegetarian": True},
    {"name": "Fruit Salad", "price": 4000.00, "category": "dessert", "is_vegetarian": True},    
]

# 1. GET /menu - Returns a welcome message for the restaurant
@app.get("/menu")
def get_menu():
    return "Welcome to Final Fantasy"

#2. GET /appetizers - Returns a list of 4 appetizer names
@app.get("/appetizers")
def get_appetizer():
    appetizers=[]
    for item in menu:
        if item["category"] == "appetizer":    
            appetizers.append(item["name"]) 
        if len(appetizers)==4:
            return appetizers    
    
            
#3. GET /main-courses - Returns a list of 5 main course names
@app.get("/main_courses")
def get_main_courses():
    main_course_names=[]
    for item in menu:
        if item["category"] == "main_course":
            main_course_names.append(item['name'])
        if len(main_course_names)==5:
            return main_course_names
        
#4. GET /desserts - Returns a list of 3 dessert names
@app.get("/desserts")
def get_desserts():
    dessert_names=[]
    for item in menu:
        if item["category"] == "dessert":
            dessert_names.append(item['name'])
        if len(dessert_names)==3:
            return dessert_names
    
#5. GET /item/{item_name} - Returns a dictionary with:
#name
#price
#category (appetizer/main/dessert)
#is_vegetarian (boolean)

@app.get("/item/{item_name}")
def get_item(item_name: str):
    for item in menu:
        if item['name'].lower()== item_name.lower():
            return item
    return {"error": "item not found"}

#6. GET /category/{category_name} - Returns all items in that category as a list
@app.get("/category/{category_name}")
def get_category(category_name: str):
    category=[]
    for item in menu:
        if item['category']== category_name:
            category.append(item)
    return category

#7. GET /price/{item_name} - Returns the price of a specific item as a string
@app.get("price/{item_name}")
def get_item_price(item_name: str):
    for item in menu:
        if item["name"].lower() == item_name.lower():
            return item["price"] 
    return {"error": "item not found"}

#8. GET /vegetarian-options - Returns a list of all vegetarian items
@app.get("/vegetarian")
def get_vegetarian_items():
    vegetarian_items = []
    for item in menu:
        if item["is_vegetarian"] == True:
            vegetarian_items.append(item)
    return vegetarian_items

#9. GET /most-expensive - Returns details of the most expensive item as a dictionary
@app.get("/most_expensive")
def get_most_expensive_item():
    most_expensive_item = max(menu, key= lambda x: x["price"])
    return most_expensive_item

#10. GET /total-items - Returns a dictionary with counts:
#total_appetizers
#total_mains
#total_desserts
#total_all

@app.get("/total_items")
def get_total_items():
    total_appetizers=[]
    total_main_courses=[]
    total_desserts=[]
    for item in menu:
        if item["category"] == "appetizer":
            total_appetizers.append(item)
        if item["category"] == "main_course":
            total_main_courses.append(item)
        if item["category"]== "dessert":
            total_desserts.append(item)
    return len(total_appetizers), len(total_main_courses), len(total_desserts)
    


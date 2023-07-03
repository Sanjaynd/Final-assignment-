import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)  # Generating a random 4-digit FoodID
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")

    def edit_food_item(self, food_id, new_name, new_quantity, new_price, new_discount, new_stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = new_name
                food_item.quantity = new_quantity
                food_item.price = new_price
                food_item.discount = new_discount
                food_item.stock = new_stock
                print("Food item updated successfully!")
                return
        print("Food item not found.")

    def view_food_items(self):
        print("List of all food items:")
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print()

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                return
        print("Food item not found.")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_new_order(self, food_items):
        selected_items = []
        total_amount = 0

        print("Selected food items:")
        for index, food_id in enumerate(food_items, start=1):
            for food_item in admin.food_items:
                if food_item.food_id == food_id:
                    selected_items.append(food_item)
                    total_amount += food_item.price
                    print(f"{index}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

        print(f"Total Amount: INR {total_amount}")
        choice = input("Do you want to place the order? (y/n): ")
        if choice.lower() == 'y':
            order = {
                'items': selected_items,
                'amount': total_amount
            }
            self.orders.append(order)
            print("Order placed successfully!")
        else:
            print("Order canceled.")

    def view_order_history(self):
        print("Order History:")
        if len(self.orders) == 0:
            print("No orders found.")
        else:
            for index, order in enumerate(self.orders, start=1):
                print(f"Order {index}:")
                for food_item in order['items']:
                    print(f"Food ID: {food_item.food_id}")
                    print(f"Name: {food_item.name}")
                    print(f"Quantity:")
                    

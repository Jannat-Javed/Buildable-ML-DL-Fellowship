# Question 2 – Mutable vs Immutable (Data Structures & Variables)

# 1. Tuple Example (Immutable)
numbers_tuple = (5, 10, 15)
print("Original Tuple:", numbers_tuple)

try:
    numbers_tuple[0] = 99   # Attempting to change tuple element
except TypeError as error:
    print("Error while modifying tuple:", error)

# Explanation:
# Tuples are immutable, which means their elements cannot be modified
# once the tuple has been created.


# 2. List Example (Mutable)
fruits_list = ["apple", "banana", "cherry"]
print("\nOriginal List:", fruits_list)

fruits_list[1] = "orange"   # Changing the second element
print("Modified List:", fruits_list)

# Explanation:
# Lists are mutable, so we can update, add, or remove elements.


# 3. Dictionary Example (Mutable)
student_info = {"name": "Ali", "roll_no": 12}
print("\nOriginal Dictionary:", student_info)

student_info["roll_no"] = 15   # Updating a value
print("Updated Dictionary:", student_info)

# Explanation:
# Dictionaries are mutable, which means we can change their values 
# by accessing them through keys.


# 4. Tuple Containing Lists (Nested Example)
mixed_tuple = ([1, 2, 3], ["x", "y", "z"])
print("\nOriginal Nested Tuple:", mixed_tuple)

mixed_tuple[1][2] = "changed"   # Modifying inside the list
print("Modified Nested Tuple:", mixed_tuple)

# Explanation:
# Tuples are immutable, so we cannot replace the lists themselves.
# However, since the tuple contains lists (which are mutable),
# we can still change the contents of those lists.

# Question 3 – User Information Dictionary (Validation + Logic)

def get_valid_name():
    name = input("Enter your name: ").strip()
    while not name:   # name should not be empty
        print("Name cannot be empty. Please try again.")
        name = input("Enter your name: ").strip()
    return name


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 100:   # valid range
                return age
            else:
                print("Age must be between 1 and 99.")
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")


def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if ("@" in email and "." in email 
            and not email.startswith((".", "@")) 
            and not email.endswith((".", "@"))):
            return email
        else:
            print("Invalid email format. Please try again.")


def get_valid_number():
    while True:
        try:
            fav_num = int(input("Enter your favorite number (1-100): "))
            if 1 <= fav_num <= 100:
                return fav_num
            else:
                print("Favorite number must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")


# Collecting User Information
user_data = {
    "name": get_valid_name(),
    "age": get_valid_age(),
    "email": get_valid_email(),
    "favorite_number": get_valid_number()
}

# Displaying Welcome Message
print(f"\nWelcome {user_data['name']}! "
      f"Your account has been registered with email {user_data['email']}.")


# Question 4 – Cinema Ticketing System

def calculate_ticket_price(age, is_student, is_weekend):
    # Validate age
    if age < 0 or age > 120:
        raise ValueError("Invalid age entered.")

    # Base pricing
    if age < 12:
        price = 5
    elif 13 <= age <= 17:
        price = 8
    elif 18 <= age <= 59:
        price = 12
    else:  # 60+
        price = 6

    # Student discount (20%) for age > 12
    if is_student and age > 12:
        price *= 0.8

    # Weekend surcharge (+$2)
    if is_weekend:
        price += 2

    return round(price, 2)


# --- Main Program ---
customers = []
total_revenue = 0

num_customers = int(input("Enter number of customers: "))

for i in range(num_customers):
    print(f"\n--- Customer {i+1} ---")
    
    # Age input
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 120:
                break
            else:
                print("Age must be between 0 and 120.")
        except ValueError:
            print("Please enter a valid number for age.")
    
    # Student input
    student_input = input("Is the customer a student? (yes/no): ").lower()
    is_student = (student_input == "yes")
    
    # Weekend input
    weekend_input = input("Is it a weekend show? (yes/no): ").lower()
    is_weekend = (weekend_input == "yes")
    
    # Calculate price
    ticket_price = calculate_ticket_price(age, is_student, is_weekend)
    total_revenue += ticket_price
    
    # Store customer details
    customers.append({
        "customer_id": i+1,
        "age": age,
        "student": is_student,
        "weekend": is_weekend,
        "ticket_price": ticket_price
    })


# Apply group discount if 4 or more customers
if num_customers >= 4:
    discount = total_revenue * 0.10
    total_revenue -= discount
    print(f"\nGroup discount applied: -${round(discount, 2)}")


# --- Display Results ---
print("\n--- Ticket Details ---")
for c in customers:
    print(f"Customer {c['customer_id']}: Age={c['age']}, "
          f"Student={c['student']}, Weekend={c['weekend']}, "
          f"Ticket Price=${c['ticket_price']}")

# Show total revenue
print(f"\nTotal Revenue: ${round(total_revenue, 2)}")

# Identify highest and lowest paying customers
highest = max(customers, key=lambda x: x['ticket_price'])
lowest = min(customers, key=lambda x: x['ticket_price'])

print(f"\nHighest Paying Customer: Customer {highest['customer_id']} "
      f"with ${highest['ticket_price']}")
print(f"Lowest Paying Customer: Customer {lowest['customer_id']} "
      f"with ${lowest['ticket_price']}")

# Question 5 – Weather Alert System

def weather_alert(temp_celsius, condition):
    # Bonus: convert Celsius to Fahrenheit and Kelvin
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    temp_kelvin = temp_celsius + 273.15

    # Weather alerts
    if temp_celsius < 0 and condition.lower() == "snowy":
        alert = "Heavy snow alert! Stay indoors."
    elif temp_celsius > 35 and condition.lower() == "sunny":
        alert = "Heatwave warning! Stay hydrated."
    elif condition.lower() == "rainy" and temp_celsius < 15:
        alert = "Cold rain alert! Wear warm clothes."
    else:
        alert = "Normal weather conditions."

    # Return message with conversions
    return (f"{alert}\n"
            f"Temperature: {temp_celsius}°C | "
            f"{round(temp_fahrenheit, 2)}°F | "
            f"{round(temp_kelvin, 2)}K")


# --- Example Runs ---
print(weather_alert(-5, "snowy"))
print(weather_alert(38, "sunny"))
print(weather_alert(10, "rainy"))
print(weather_alert(22, "cloudy"))


# Question 6 – Sales Analytics (Max, Min & Median)
import statistics

def analyze_sales(sales_list):
    highest = max(sales_list)
    lowest = min(sales_list)
    median_val = statistics.median(sales_list)
    return highest, lowest, median_val


# --- Main Program ---
sales = []

# Ask user for sales values (at least 5 required)
while True:
    try:
        num_days = int(input("Enter number of days of sales data: "))
        if num_days < 5:
            print("You must enter at least 5 sales values.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Collect sales data
for i in range(num_days):
    while True:
        try:
            sale = float(input(f"Enter sales for day {i+1}: "))
            sales.append(sale)
            break
        except ValueError:
            print("Please enter a valid sales amount.")

# Analyze sales
highest, lowest, median_val = analyze_sales(sales)

# Display summary
print("\n--- Sales Summary ---")
print(f"Highest sales day: {highest}")
print(f"Lowest sales day: {lowest}")
print(f"Median sales: {median_val}")


# Question 7 – E-commerce Inventory Management

def update_inventory(inventory_dict, item, quantity):
    if item not in inventory_dict:
        print(f"{item} not found in inventory.")
        return inventory_dict
    
    # Check if removing more than available
    if quantity < 0 and abs(quantity) > inventory_dict[item]:
        print(f"Not enough stock for {item}.")
    else:
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    
    return inventory_dict


# --- Initialize Inventory ---
inventory = {
    "laptop": 10,
    "phone": 20,
    "headphones": 15,
    "keyboard": 12,
    "mouse": 18
}

print("Initial Inventory:", inventory)

# --- Simulate Shopping Cart (3 purchases) ---
for i in range(3):
    item = input(f"\nEnter item {i+1} to buy: ").lower()
    try:
        qty = int(input(f"Enter quantity of {item}: "))
    except ValueError:
        print("Invalid quantity. Skipping item.")
        continue
    
    # Deduct quantity (negative for removal)
    inventory = update_inventory(inventory, item, -qty)

# --- After Checkout ---
print("\n--- Updated Inventory ---")
for product, stock in inventory.items():
    print(f"{product}: {stock}")

# Find most and least stocked products
most_stocked = max(inventory, key=inventory.get)
least_stocked = min(inventory, key=inventory.get)

print(f"\nMost stocked product: {most_stocked} ({inventory[most_stocked]} units)")
print(f"Least stocked product: {least_stocked} ({inventory[least_stocked]} units)")

users = {"admin": "admin123", "user": "1234"}

def login_user(username, password):
    if username in users:
        if users[username] == password:
            return username
    return None

def create_order(user, amount):
    if user == None:
        print("Invalid user")

    if amount > 10000:
        print("High value order")
    if amount > 10000:
        print("High value order")  # duplication

    discount = calculate_discount(amount)
    print("Final:", amount - discount)

def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.2
    return amount * 0.2

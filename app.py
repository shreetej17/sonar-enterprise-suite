from services import login_user, create_order
from database import connect_db

print("Enterprise system starting")

db = connect_db("admin", "admin123")   # hardcoded secret
user = login_user("admin", "admin123")

if user:
    create_order(user, 20000)

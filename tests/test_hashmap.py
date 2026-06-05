from src.models.product import Product
from src.models.user import User

from src.dsa.hashmap_store import (
    HashMapStore
)

store = HashMapStore()

# Product

product1 = Product(
    1001,
    "Gaming Mouse",
    "Gaming",
    1499,
    4.8
)

product2 = Product(
    1002,
    "Gaming Keyboard",
    "Gaming",
    2999,
    4.9
)

# User

user1 = User(
    1,
    "User_1"
)

# Store

store.add_product(product1)
store.add_product(product2)

store.add_user(user1)

# Retrieve

print(
    store.get_product(1001)
)

print(
    store.get_user(1)
)

print(
    "Total Products:",
    store.total_products()
)

print(
    "Total Users:",
    store.total_users()
)
from src.models.product import Product
from src.models.user import User

product = Product(
    1001,
    "Gaming Mouse",
    "Gaming",
    1499,
    4.8
)

user = User(
    1,
    "User_1"
)

user.add_purchase(1001)
user.add_search("gaming mouse")
user.add_cart_item(1001)

print(product)
print(user)

print(product.to_dict())
print(user.to_dict())
import pandas as pd
import random

# -------------------------
# PRODUCTS
# -------------------------

categories = {
    "Gaming": [
        "Gaming Mouse",
        "Gaming Keyboard",
        "Gaming Headset",
        "Gaming Chair",
        "RGB Mouse Pad",
        "Gaming Monitor"
    ],

    "Electronics": [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Smart Watch",
        "Bluetooth Speaker",
        "Webcam"
    ],

    "Fashion": [
        "T-Shirt",
        "Jeans",
        "Jacket",
        "Sneakers",
        "Hoodie",
        "Cap"
    ],

    "Books": [
        "Python Programming",
        "DSA Handbook",
        "Machine Learning",
        "Data Science",
        "Web Development",
        "AI Fundamentals"
    ],

    "Sports": [
        "Football",
        "Cricket Bat",
        "Tennis Racket",
        "Basketball",
        "Yoga Mat",
        "Gym Gloves"
    ]
}

products = []

product_id = 1001

for category, items in categories.items():

    for _ in range(20):

        name = random.choice(items)

        products.append({
            "product_id": product_id,
            "name": f"{name} {product_id}",
            "category": category,
            "price": random.randint(500, 15000),
            "rating": round(random.uniform(3.5, 5.0), 1)
        })

        product_id += 1

products_df = pd.DataFrame(products)

# -------------------------
# USERS
# -------------------------

users = []

for user_id in range(1, 51):

    users.append({
        "user_id": user_id,
        "name": f"User_{user_id}"
    })

users_df = pd.DataFrame(users)

# -------------------------
# PURCHASES
# -------------------------

purchases = []

for _ in range(500):

    purchases.append({
        "user_id": random.randint(1, 50),
        "product_id": random.choice(
            products_df["product_id"].tolist()
        )
    })

purchases_df = pd.DataFrame(purchases)

# -------------------------
# SEARCHES
# -------------------------

search_terms = [
    "gaming",
    "laptop",
    "smartphone",
    "python",
    "sports",
    "fashion",
    "headset",
    "keyboard",
    "machine learning",
    "data science"
]

searches = []

for _ in range(1000):

    searches.append({
        "user_id": random.randint(1, 50),
        "search_query": random.choice(search_terms)
    })

searches_df = pd.DataFrame(searches)

# -------------------------
# CARTS
# -------------------------

carts = []

for _ in range(200):

    carts.append({
        "user_id": random.randint(1, 50),
        "product_id": random.choice(
            products_df["product_id"].tolist()
        )
    })

carts_df = pd.DataFrame(carts)

# -------------------------
# SAVE FILES
# -------------------------

products_df.to_csv(
    "data/products.csv",
    index=False
)

users_df.to_csv(
    "data/users.csv",
    index=False
)

purchases_df.to_csv(
    "data/purchases.csv",
    index=False
)

searches_df.to_csv(
    "data/searches.csv",
    index=False
)

carts_df.to_csv(
    "data/carts.csv",
    index=False
)

print("Datasets generated successfully!")
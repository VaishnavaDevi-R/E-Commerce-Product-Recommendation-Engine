from src.utils.data_loader import (
    DataLoader
)

from src.engine.collaborative_filter import (
    CollaborativeFilter
)

loader = DataLoader()

data = loader.load_all()

cf = CollaborativeFilter(
    data["purchases"]
)

user_id = 1

recommendations = (
    cf.recommend_products(
        user_id,
        top_n=5
    )
)

print(
    f"\nRecommendations for User {user_id}\n"
)

for product_id, score in recommendations:

    print(
        f"Product ID: {product_id}"
        f" | Score: {round(score,3)}"
    )
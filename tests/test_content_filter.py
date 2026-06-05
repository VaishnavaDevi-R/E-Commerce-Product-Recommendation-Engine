from src.utils.data_loader import (
    DataLoader
)

from src.engine.content_filter import (
    ContentFilter
)

loader = DataLoader()

data = loader.load_all()

content_filter = ContentFilter(
    data["store"]
)

# Choose any existing product ID
product_id = 1001

recommendations = (
    content_filter.get_similar_products(
        product_id,
        top_n=5
    )
)

print(
    f"\nProducts similar to {product_id}\n"
)

for product in recommendations:

    print(
        product["name"],
        "| Score:",
        product["score"]
    )
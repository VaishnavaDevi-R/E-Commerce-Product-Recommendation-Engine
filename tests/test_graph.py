import pandas as pd

from src.dsa.graph_recommender import (
    GraphRecommender
)

# Sample Purchase Data

data = {

    "user_id": [
        1,
        1,
        1,
        2,
        2
    ],

    "product_id": [
        1001,
        1002,
        1003,
        1001,
        1004
    ]
}

purchases = pd.DataFrame(data)

graph = GraphRecommender()

graph.build_graph(
    purchases
)

related = graph.get_related_products(
    1001
)

print(
    "Products related to 1001:"
)

print(
    related
)
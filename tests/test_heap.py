from src.dsa.heap_ranker import (
    HeapRanker
)

recommendations = [

    {
        "product_id": 1001,
        "name": "Gaming Mouse",
        "score": 85
    },

    {
        "product_id": 1002,
        "name": "Gaming Keyboard",
        "score": 95
    },

    {
        "product_id": 1003,
        "name": "Gaming Chair",
        "score": 75
    },

    {
        "product_id": 1004,
        "name": "Gaming Headset",
        "score": 90
    },

    {
        "product_id": 1005,
        "name": "Webcam",
        "score": 70
    }
]

top_products = HeapRanker.get_top_products(
    recommendations,
    top_n=3
)

for product in top_products:

    print(
        product["name"],
        product["score"]
    )
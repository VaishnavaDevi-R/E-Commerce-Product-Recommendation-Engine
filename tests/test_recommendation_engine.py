from src.utils.data_loader import (
    DataLoader
)

from src.engine.recommendation_engine import (
    RecommendationEngine
)

loader = DataLoader()

data = loader.load_all()

engine = RecommendationEngine(

    store=data["store"],
    graph=data["graph"],
    purchases_df=data["purchases"]

)

recommendations = engine.recommend(

    user_id=1,
    top_n=10

)

print("\nTOP RECOMMENDATIONS\n")

for index, item in enumerate(

    recommendations,
    start=1

):

    print(

        f"{index}. "
        f"{item['name']} "
        f"| Score: {item['score']}"

    )
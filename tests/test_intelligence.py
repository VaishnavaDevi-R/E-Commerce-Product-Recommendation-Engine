from src.utils.data_loader import (
    DataLoader
)

from src.engine.intelligence_layer import (
    IntelligenceLayer
)

loader = DataLoader()

data = loader.load_all()

intel = IntelligenceLayer(

    purchases_df=data["purchases"],
    graph=data["graph"],
    store=data["store"]

)

print("\nTRENDING PRODUCTS\n")

for item in intel.get_trending_products(5):

    print(item)

print("\nFREQUENTLY BOUGHT TOGETHER\n")

sample_id = (
    data["products"]
    .iloc[0]["product_id"]
)

print(

    intel.frequently_bought_together(
        sample_id
    )

)
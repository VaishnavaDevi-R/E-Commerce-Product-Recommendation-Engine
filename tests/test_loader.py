from src.utils.data_loader import (
    DataLoader
)

loader = DataLoader()

data = loader.load_all()

print(
    "Products:",
    data["store"].total_products()
)

print(
    "Users:",
    data["store"].total_users()
)

print(
    "Graph Nodes:",
    data["graph"].total_products()
)

results = data["trie"].autocomplete(
    "gam"
)

print(
    "\nSearch Suggestions:"
)

print(results[:5])
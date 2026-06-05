from src.dsa.trie_search import (
    TrieSearch
)

trie = TrieSearch()

products = [

    "Gaming Mouse",
    "Gaming Keyboard",
    "Gaming Chair",
    "Gaming Headset",
    "Laptop",
    "Smartphone"
]

for product in products:

    trie.insert(product)

results = trie.autocomplete(
    "gam"
)

print(results)
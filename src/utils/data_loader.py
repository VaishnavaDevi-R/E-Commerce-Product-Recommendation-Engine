import pandas as pd

from src.models.product import Product
from src.models.user import User

from src.dsa.hashmap_store import HashMapStore
from src.dsa.graph_recommender import GraphRecommender
from src.dsa.trie_search import TrieSearch


class DataLoader:

    def __init__(self):

        self.store = HashMapStore()

        self.graph = GraphRecommender()

        self.trie = TrieSearch()

    # -------------------------
    # Load Products
    # -------------------------

    def load_products(
        self,
        file_path="data/products.csv"
    ):

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            product = Product(
                product_id=row["product_id"],
                name=row["name"],
                category=row["category"],
                price=row["price"],
                rating=row["rating"]
            )

            self.store.add_product(product)

            self.trie.insert(
                product.name
            )

        return df

    # -------------------------
    # Load Users
    # -------------------------

    def load_users(
        self,
        file_path="data/users.csv"
    ):

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            user = User(
                user_id=row["user_id"],
                name=row["name"]
            )

            self.store.add_user(user)

        return df

    # -------------------------
    # Load Purchases
    # -------------------------

    def load_purchases(
        self,
        file_path="data/purchases.csv"
    ):

        return pd.read_csv(file_path)

    # -------------------------
    # Load Searches
    # -------------------------

    def load_searches(
        self,
        file_path="data/searches.csv"
    ):

        return pd.read_csv(file_path)

    # -------------------------
    # Load Carts
    # -------------------------

    def load_carts(
        self,
        file_path="data/carts.csv"
    ):

        return pd.read_csv(file_path)

    # -------------------------
    # Build Graph
    # -------------------------

    def build_graph(
        self,
        purchases_df
    ):

        self.graph.build_graph(
            purchases_df
        )

    # -------------------------
    # Load Everything
    # -------------------------

    def load_all(self):

        products_df = self.load_products()

        users_df = self.load_users()

        purchases_df = self.load_purchases()

        searches_df = self.load_searches()

        carts_df = self.load_carts()

        self.build_graph(
            purchases_df
        )

        return {

            "products": products_df,
            "users": users_df,
            "purchases": purchases_df,
            "searches": searches_df,
            "carts": carts_df,

            "store": self.store,
            "graph": self.graph,
            "trie": self.trie
        }
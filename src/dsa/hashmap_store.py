from src.models.product import Product
from src.models.user import User


class HashMapStore:

    def __init__(self):

        # HashMaps

        self.products = {}
        self.users = {}

    # -------------------------
    # PRODUCT OPERATIONS
    # -------------------------

    def add_product(self, product):

        self.products[
            product.product_id
        ] = product

    def get_product(
        self,
        product_id
    ):

        return self.products.get(
            product_id
        )

    def get_all_products(self):

        return list(
            self.products.values()
        )

    # -------------------------
    # USER OPERATIONS
    # -------------------------

    def add_user(self, user):

        self.users[
            user.user_id
        ] = user

    def get_user(
        self,
        user_id
    ):

        return self.users.get(
            user_id
        )

    def get_all_users(self):

        return list(
            self.users.values()
        )

    # -------------------------
    # COUNTS
    # -------------------------

    def total_products(self):

        return len(
            self.products
        )

    def total_users(self):

        return len(
            self.users
        )
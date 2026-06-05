class User:

    def __init__(
        self,
        user_id,
        name
    ):

        self.user_id = user_id
        self.name = name

        self.purchase_history = []
        self.search_history = []
        self.cart_items = []

    def add_purchase(
        self,
        product_id
    ):

        self.purchase_history.append(
            product_id
        )

    def add_search(
        self,
        search_query
    ):

        self.search_history.append(
            search_query
        )

    def add_cart_item(
        self,
        product_id
    ):

        self.cart_items.append(
            product_id
        )

    def to_dict(self):

        return {
            "user_id": self.user_id,
            "name": self.name,
            "purchases": self.purchase_history,
            "searches": self.search_history,
            "cart_items": self.cart_items
        }

    def __str__(self):

        return (
            f"User ID: {self.user_id} | "
            f"Name: {self.name}"
        )
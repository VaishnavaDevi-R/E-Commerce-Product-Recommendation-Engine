class Product:

    def __init__(
        self,
        product_id,
        name,
        category,
        price,
        rating
    ):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating

    def to_dict(self):

        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "rating": self.rating
        }

    def __str__(self):

        return (
            f"{self.name} | "
            f"{self.category} | "
            f"₹{self.price} | "
            f"⭐ {self.rating}"
        )
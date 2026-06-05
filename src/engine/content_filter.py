class ContentFilter:

    def __init__(self, store):

        self.store = store

    # -------------------------
    # Similarity Score
    # -------------------------

    def calculate_similarity(
        self,
        product_a,
        product_b
    ):

        score = 0

        # Same Category
        if (
            product_a.category ==
            product_b.category
        ):
            score += 50

        # Similar Rating
        rating_gap = abs(
            product_a.rating -
            product_b.rating
        )

        score += max(
            0,
            20 - (rating_gap * 10)
        )

        # Similar Price
        price_gap = abs(
            product_a.price -
            product_b.price
        )

        if price_gap <= 1000:
            score += 30

        elif price_gap <= 3000:
            score += 15

        return round(score, 2)

    # -------------------------
    # Similar Products
    # -------------------------

    def get_similar_products(
        self,
        product_id,
        top_n=5
    ):

        target_product = (
            self.store.get_product(
                product_id
            )
        )

        if not target_product:
            return []

        recommendations = []

        for product in (
            self.store.get_all_products()
        ):

            if (
                product.product_id ==
                product_id
            ):
                continue

            similarity = (
                self.calculate_similarity(
                    target_product,
                    product
                )
            )

            recommendations.append({

                "product_id":
                product.product_id,

                "name":
                product.name,

                "category":
                product.category,

                "score":
                similarity
            })

        recommendations.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return recommendations[:top_n]
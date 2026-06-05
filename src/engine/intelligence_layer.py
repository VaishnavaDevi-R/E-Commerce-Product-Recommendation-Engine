from collections import Counter


class IntelligenceLayer:

    def __init__(

        self,
        purchases_df,
        graph,
        store

    ):

        self.purchases_df = purchases_df
        self.graph = graph
        self.store = store

    # -------------------------
    # Trending Products
    # -------------------------

    def get_trending_products(
        self,
        top_n=10
    ):

        counts = Counter(

            self.purchases_df[
                "product_id"
            ]

        )

        trending = []

        for product_id, count in (

            counts.most_common(top_n)

        ):

            product = (
                self.store
                .get_product(
                    product_id
                )
            )

            if product:

                trending.append({

                    "product_id":
                    product.product_id,

                    "name":
                    product.name,

                    "category":
                    product.category,

                    "purchases":
                    count

                })

        return trending

    # -------------------------
    # Frequently Bought Together
    # -------------------------

    def frequently_bought_together(
        self,
        product_id,
        top_n=5
    ):

        related = (

            self.graph
            .get_related_products(
                product_id
            )

        )

        result = []

        for item in related[:top_n]:

            product = (
                self.store
                .get_product(item)
            )

            if product:

                result.append({

                    "product_id":
                    product.product_id,

                    "name":
                    product.name

                })

        return result

    # -------------------------
    # Recommendation Reason
    # -------------------------

    def generate_reason(
        self,
        product
    ):

        reasons = []

        if product["rating"] >= 4.5:

            reasons.append(
                "Highly Rated"
            )

        if product["score"] > 150:

            reasons.append(
                "Popular Among Similar Users"
            )

        if product["score"] > 100:

            reasons.append(
                "Matches Your Interests"
            )

        reasons.append(
            "Recommended By Hybrid Engine"
        )

        return reasons
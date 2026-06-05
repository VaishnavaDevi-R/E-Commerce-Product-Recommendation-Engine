class CollaborativeFilter:

    def __init__(
        self,
        purchases_df
    ):

        self.purchases_df = purchases_df

    # -------------------------
    # User Purchases
    # -------------------------

    def get_user_products(
        self,
        user_id
    ):

        return set(

            self.purchases_df[
                self.purchases_df["user_id"]
                == user_id
            ]["product_id"]

        )

    # -------------------------
    # User Similarity
    # -------------------------

    def calculate_similarity(
        self,
        user_a,
        user_b
    ):

        products_a = (
            self.get_user_products(
                user_a
            )
        )

        products_b = (
            self.get_user_products(
                user_b
            )
        )

        if (
            len(products_a) == 0
            and
            len(products_b) == 0
        ):
            return 0

        intersection = (
            products_a.intersection(
                products_b
            )
        )

        union = (
            products_a.union(
                products_b
            )
        )

        return (
            len(intersection)
            /
            len(union)
        )

    # -------------------------
    # Similar Users
    # -------------------------

    def get_similar_users(
        self,
        user_id,
        top_n=5
    ):

        similarities = []

        all_users = (
            self.purchases_df[
                "user_id"
            ].unique()
        )

        for other_user in all_users:

            if other_user == user_id:
                continue

            score = (
                self.calculate_similarity(
                    user_id,
                    other_user
                )
            )

            similarities.append({

                "user_id":
                other_user,

                "score":
                score
            })

        similarities.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return similarities[:top_n]

    # -------------------------
    # Recommendations
    # -------------------------

    def recommend_products(
        self,
        user_id,
        top_n=10
    ):

        user_products = (
            self.get_user_products(
                user_id
            )
        )

        similar_users = (
            self.get_similar_users(
                user_id
            )
        )

        recommendation_scores = {}

        for user in similar_users:

            other_user = (
                user["user_id"]
            )

            similarity = (
                user["score"]
            )

            other_products = (
                self.get_user_products(
                    other_user
                )
            )

            for product in other_products:

                if product in user_products:
                    continue

                recommendation_scores[
                    product
                ] = (

                    recommendation_scores.get(
                        product,
                        0
                    )

                    + similarity

                )

        ranked = sorted(

            recommendation_scores.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return ranked[:top_n]
from collections import Counter


class FrequentlyBoughtTogether:

    def __init__(
        self,
        purchases_df
    ):

        self.purchases_df = purchases_df

    def get_recommendations(
        self,
        product_id,
        top_n=5
    ):

        users = self.purchases_df[
            self.purchases_df[
                "product_id"
            ] == product_id
        ]["user_id"]

        related = self.purchases_df[
            self.purchases_df[
                "user_id"
            ].isin(users)
        ]

        counter = Counter(
            related["product_id"]
        )

        if product_id in counter:
            del counter[product_id]

        return counter.most_common(
            top_n
        )
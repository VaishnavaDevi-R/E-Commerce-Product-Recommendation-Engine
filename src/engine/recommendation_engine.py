from collections import defaultdict

from src.engine.content_filter import ContentFilter
from src.engine.collaborative_filter import CollaborativeFilter
from src.dsa.heap_ranker import HeapRanker


class RecommendationEngine:

    def __init__(
        self,
        store,
        graph,
        purchases_df
    ):
        self.store = store
        self.graph = graph
        self.purchases_df = purchases_df

        self.content_filter = ContentFilter(
            store
        )

        self.collaborative_filter = CollaborativeFilter(
            purchases_df
        )

    # ----------------------------------
    # Product Popularity
    # ----------------------------------

    def get_popularity_scores(self):

        popularity = defaultdict(int)

        for _, row in self.purchases_df.iterrows():

            popularity[
                row["product_id"]
            ] += 1

        return popularity

    # ----------------------------------
    # Hybrid Recommendation Engine
    # ----------------------------------

    def recommend(
        self,
        user_id,
        top_n=10
    ):

        final_scores = defaultdict(float)

        user_products = set(

            self.purchases_df[
                self.purchases_df["user_id"]
                == user_id
            ]["product_id"]

        )

        popularity = self.get_popularity_scores()

        # ----------------------------------
        # Cold Start User
        # ----------------------------------

        if len(user_products) == 0:

            trending = []

            for product_id, score in popularity.items():

                product = self.store.get_product(
                    product_id
                )

                if not product:
                    continue

                trending.append({

                    "product_id":
                    product.product_id,

                    "name":
                    product.name,

                    "category":
                    product.category,

                    "price":
                    product.price,

                    "rating":
                    product.rating,

                    "score":
                    score

                })

            return HeapRanker.get_top_products(
                trending,
                top_n
            )

        # ----------------------------------
        # Content Based
        # ----------------------------------

        for product_id in user_products:

            similar_products = (

                self.content_filter
                .get_similar_products(
                    product_id,
                    top_n=5
                )

            )

            for item in similar_products:

                final_scores[
                    item["product_id"]
                ] += (

                    item["score"]
                    * 0.40

                )

        # ----------------------------------
        # Collaborative Filtering
        # ----------------------------------

        collaborative_products = (

            self.collaborative_filter
            .recommend_products(
                user_id,
                top_n=20
            )

        )

        for product_id, score in collaborative_products:

            final_scores[
                product_id
            ] += score * 30

        # ----------------------------------
        # Graph Recommendations
        # ----------------------------------

        for product_id in user_products:

            related_products = (

                self.graph
                .get_related_products(
                    product_id
                )

            )

            for related in related_products:

                final_scores[
                    related
                ] += 20

        # ----------------------------------
        # Popularity Bonus
        # ----------------------------------

        for product_id in list(
            final_scores.keys()
        ):

            final_scores[
                product_id
            ] += (

                popularity.get(
                    product_id,
                    0
                ) * 2

            )

        # ----------------------------------
        # Build Final Recommendation List
        # ----------------------------------

        recommendations = []

        for product_id, score in (

            final_scores.items()

        ):

            if product_id in user_products:
                continue

            product = self.store.get_product(
                product_id
            )

            if not product:
                continue

            recommendations.append({

                "product_id":
                product.product_id,

                "name":
                product.name,

                "category":
                product.category,

                "price":
                product.price,

                "rating":
                product.rating,

                "score":
                round(score, 2)

            })

        return HeapRanker.get_top_products(
            recommendations,
            top_n
        )
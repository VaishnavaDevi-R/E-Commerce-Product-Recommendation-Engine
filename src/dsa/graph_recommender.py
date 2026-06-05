from collections import defaultdict


class GraphRecommender:

    def __init__(self):

        self.graph = defaultdict(set)

    # -------------------------
    # Add Relationship
    # -------------------------

    def add_relationship(
        self,
        product_a,
        product_b
    ):

        self.graph[product_a].add(
            product_b
        )

        self.graph[product_b].add(
            product_a
        )

    # -------------------------
    # Build Graph
    # -------------------------

    def build_graph(
        self,
        purchases_df
    ):

        grouped_users = purchases_df.groupby(
            "user_id"
        )["product_id"].apply(list)

        for products in grouped_users:

            unique_products = list(
                set(products)
            )

            for i in range(
                len(unique_products)
            ):

                for j in range(
                    i + 1,
                    len(unique_products)
                ):

                    self.add_relationship(
                        unique_products[i],
                        unique_products[j]
                    )

    # -------------------------
    # Recommendations
    # -------------------------

    def get_related_products(
        self,
        product_id
    ):

        return list(
            self.graph.get(
                product_id,
                []
            )
        )

    # -------------------------
    # Total Nodes
    # -------------------------

    def total_products(self):

        return len(
            self.graph
        )
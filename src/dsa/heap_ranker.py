import heapq


class HeapRanker:

    @staticmethod
    def get_top_products(
        recommendations,
        top_n=5
    ):

        return heapq.nlargest(
            top_n,
            recommendations,
            key=lambda x: x["score"]
        )

    @staticmethod
    def get_bottom_products(
        recommendations,
        bottom_n=5
    ):

        return heapq.nsmallest(
            bottom_n,
            recommendations,
            key=lambda x: x["score"]
        )
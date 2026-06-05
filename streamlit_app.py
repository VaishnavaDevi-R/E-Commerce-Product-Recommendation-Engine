import streamlit as st
import pandas as pd
import plotly.express as px

from src.utils.data_loader import DataLoader
from src.utils.export_utils import export_excel
from src.utils.image_mapper import get_image

from src.engine.recommendation_engine import (
    RecommendationEngine
)

from src.engine.content_filter import (
    ContentFilter
)

from src.engine.intelligence_layer import (
    IntelligenceLayer
)

from src.engine.fbt_service import (
    FrequentlyBoughtTogether
)


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="DSA E-Commerce Recommendation Engine",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
<style>

.main-header{
    font-size:40px;
    font-weight:bold;
    color:#1E88E5;
}

.sub-header{
    font-size:18px;
    color:gray;
}

.product-card{
    padding:15px;
    border-radius:15px;
    border:1px solid #dddddd;
    margin-bottom:15px;
}

.metric-card{
    text-align:center;
}

</style>
""",
    unsafe_allow_html=True
)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_resource
def load_system():

    loader = DataLoader()

    data = loader.load_all()

    recommendation_engine = RecommendationEngine(
        store=data["store"],
        graph=data["graph"],
        purchases_df=data["purchases"]
    )

    content_filter = ContentFilter(
        data["store"]
    )

    intelligence = IntelligenceLayer(
        purchases_df=data["purchases"],
        graph=data["graph"],
        store=data["store"]
    )

    fbt_service = FrequentlyBoughtTogether(
        data["purchases"]
    )

    return (
        data,
        recommendation_engine,
        content_filter,
        intelligence,
        fbt_service
    )


(
    data,
    recommendation_engine,
    content_filter,
    intelligence,
    fbt_service
) = load_system()


# =====================================================
# DATA REFERENCES
# =====================================================

products_df = data["products"]

users_df = data["users"]

purchases_df = data["purchases"]

store = data["store"]

graph = data["graph"]

trie = data["trie"]


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title(
    "🛒 Navigation"
)

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Recommendations",
        "Search",
        "Products",
        "Trending",
        "Frequently Bought Together"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
DSA Components Used:

✅ HashMap

✅ Heap

✅ Graph

✅ Trie

✅ Content Filtering

✅ Collaborative Filtering

✅ Hybrid Recommendation Engine
"""
)


# =====================================================
# MAIN HEADER
# =====================================================

st.markdown(
    """
<div class='main-header'>
DSA-Powered E-Commerce Recommendation Engine
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class='sub-header'>
Hybrid Recommendation System using
HashMap, Heap, Graph, Trie,
Content-Based Filtering and
Collaborative Filtering
</div>
""",
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# DASHBOARD PAGE
# =====================================================

if page == "Dashboard":

    st.header("📊 Dashboard")

    # ---------------------------------
    # KPI CARDS
    # ---------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Products",
            len(products_df)
        )

    with col2:

        st.metric(
            "Users",
            len(users_df)
        )

    with col3:

        st.metric(
            "Purchases",
            len(purchases_df)
        )

    with col4:

        st.metric(
            "Categories",
            products_df[
                "category"
            ].nunique()
        )

    st.markdown("---")

    # ---------------------------------
    # CATEGORY DISTRIBUTION
    # ---------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📦 Products by Category"
        )

        category_count = (

            products_df[
                "category"
            ]
            .value_counts()
            .reset_index()

        )

        category_count.columns = [
            "Category",
            "Count"
        ]

        fig = px.bar(
            category_count,
            x="Category",
            y="Count",
            title="Products by Category"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------------------------
    # CATEGORY PIE CHART
    # ---------------------------------

    with col2:

        st.subheader(
            "🥧 Category Distribution"
        )

        pie_fig = px.pie(
            category_count,
            names="Category",
            values="Count",
            title="Category Share"
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )

    st.markdown("---")

    # ---------------------------------
    # TOP PURCHASED PRODUCTS
    # ---------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🔥 Most Purchased Products"
        )

        top_products = (

            purchases_df[
                "product_id"
            ]
            .value_counts()
            .head(10)
            .reset_index()

        )

        top_products.columns = [
            "Product ID",
            "Purchases"
        ]

        fig2 = px.bar(
            top_products,
            x="Product ID",
            y="Purchases",
            title="Top Purchased Products"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ---------------------------------
    # MOST ACTIVE USERS
    # ---------------------------------

    with col2:

        st.subheader(
            "👥 Most Active Users"
        )

        active_users = (

            purchases_df[
                "user_id"
            ]
            .value_counts()
            .head(10)
            .reset_index()

        )

        active_users.columns = [
            "User ID",
            "Purchases"
        ]

        fig3 = px.bar(
            active_users,
            x="User ID",
            y="Purchases",
            title="Top Active Users"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    st.markdown("---")

    # ---------------------------------
    # TOP RATED PRODUCTS
    # ---------------------------------

    st.subheader(
        "⭐ Top Rated Products"
    )

    top_rated = (

        products_df
        .sort_values(
            by="rating",
            ascending=False
        )
        .head(10)

    )

    st.dataframe(
        top_rated,
        use_container_width=True
    )

    # =====================================================
# RECOMMENDATIONS PAGE
# =====================================================

elif page == "Recommendations":

    st.header(
        "🎯 Personalized Recommendations"
    )

    user_id = st.selectbox(
        "Select User",
        sorted(
            users_df[
                "user_id"
            ].unique()
        )
    )

    top_n = st.slider(
        "Number of Recommendations",
        min_value=5,
        max_value=20,
        value=10
    )

    if st.button(
        "Generate Recommendations",
        use_container_width=True
    ):

        recommendations = (

            recommendation_engine
            .recommend(
                user_id=user_id,
                top_n=top_n
            )

        )

        if len(recommendations) == 0:

            st.warning(
                "No recommendations found."
            )

        else:

            st.success(
                f"Generated {len(recommendations)} recommendations"
            )

            recommendation_df = pd.DataFrame(
                recommendations
            )

            # ---------------------------------
            # DOWNLOADS
            # ---------------------------------

            col1, col2 = st.columns(2)

            with col1:

                csv_data = (
                    recommendation_df
                    .to_csv(
                        index=False
                    )
                )

                st.download_button(
                    label="⬇ Download CSV",
                    data=csv_data,
                    file_name="recommendations.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            with col2:

                excel_data = export_excel(
                    recommendation_df
                )

                st.download_button(
                    label="⬇ Download Excel",
                    data=excel_data,
                    file_name="recommendations.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

            st.markdown("---")

            # ---------------------------------
            # RECOMMENDATION CARDS
            # ---------------------------------

            for item in recommendations:

                image_path = get_image(
                    item["name"]
                )

                col1, col2 = st.columns(
                    [1, 3]
                )

                # -------------------------
                # IMAGE
                # -------------------------

                with col1:

                    if image_path:

                        try:

                            st.image(
                                image_path,
                                width=180
                            )

                        except:

                            st.image(
                                "https://via.placeholder.com/180"
                            )

                # -------------------------
                # PRODUCT DETAILS
                # -------------------------

                with col2:

                    st.markdown(
                        f"""
### {item['name']}

**Category:** {item['category']}

**Price:** ₹{item['price']}

**Rating:** ⭐ {item['rating']}

**Recommendation Score:** {item['score']}
"""
                    )

                    reasons = (

                        intelligence
                        .generate_reason(
                            item
                        )

                    )

                    st.info(
                        "Why Recommended?  \n"
                        +
                        " • ".join(
                            reasons
                        )
                    )

                st.divider()

            # ---------------------------------
            # TABLE VIEW
            # ---------------------------------

            st.subheader(
                "📋 Recommendation Table"
            )

            st.dataframe(
                recommendation_df,
                use_container_width=True
            )

            # ---------------------------------
            # SCORE CHART
            # ---------------------------------

            st.subheader(
                "📈 Recommendation Scores"
            )

            chart = px.bar(
                recommendation_df,
                x="name",
                y="score",
                color="category",
                title="Recommendation Ranking"
            )

            st.plotly_chart(
                chart,
                use_container_width=True
            )

            # =====================================================
# SEARCH PAGE
# =====================================================

elif page == "Search":

    st.header(
        "🔍 Product Search"
    )

    query = st.text_input(
        "Search Products"
    )

    if query:

        suggestions = (
            trie.autocomplete(
                query
            )
        )

        if suggestions:

            st.success(
                f"{len(suggestions)} suggestions found"
            )

            for item in suggestions:

                image_path = get_image(
                    item
                )

                col1, col2 = st.columns(
                    [1, 4]
                )

                with col1:

                    if image_path:

                        try:

                            st.image(
                                image_path,
                                width=120
                            )

                        except:
                            pass

                with col2:

                    st.markdown(
                        f"### {item}"
                    )

                st.divider()

        else:

            st.warning(
                "No products found."
            )


# =====================================================
# PRODUCTS PAGE
# =====================================================

elif page == "Products":

    st.header(
        "📦 Product Catalog"
    )

    category = st.selectbox(
        "Select Category",
        ["All"] +
        sorted(
            products_df[
                "category"
            ].unique()
        )
    )

    filtered_df = products_df.copy()

    if category != "All":

        filtered_df = filtered_df[
            filtered_df[
                "category"
            ] == category
        ]

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Find Similar Products"
    )

    product_id = st.number_input(
        "Product ID",
        min_value=int(
            products_df[
                "product_id"
            ].min()
        ),
        max_value=int(
            products_df[
                "product_id"
            ].max()
        ),
        step=1
    )

    if st.button(
        "Find Similar Products"
    ):

        similar_products = (

            content_filter
            .get_similar_products(
                product_id,
                top_n=5
            )

        )

        if similar_products:

            for item in similar_products:

                image_path = get_image(
                    item["name"]
                )

                col1, col2 = st.columns(
                    [1, 3]
                )

                with col1:

                    if image_path:

                        try:

                            st.image(
                                image_path,
                                width=150
                            )

                        except:
                            pass

                with col2:

                    st.markdown(
                        f"""
### {item['name']}

**Category:** {item['category']}

**Similarity Score:** {item['score']}
"""
                    )

                st.divider()

        else:

            st.warning(
                "No similar products found."
            )


# =====================================================
# TRENDING PAGE
# =====================================================

elif page == "Trending":

    st.header(
        "🔥 Trending Products"
    )

    trending_products = (

        intelligence
        .get_trending_products(
            top_n=10
        )

    )

    trending_df = pd.DataFrame(
        trending_products
    )

    st.dataframe(
        trending_df,
        use_container_width=True
    )

    if not trending_df.empty:

        chart = px.bar(
            trending_df,
            x="name",
            y="purchases",
            color="category",
            title="Trending Products"
        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )

        st.markdown("---")

        for item in trending_products:

            image_path = get_image(
                item["name"]
            )

            col1, col2 = st.columns(
                [1, 3]
            )

            with col1:

                if image_path:

                    try:

                        st.image(
                            image_path,
                            width=150
                        )

                    except:
                        pass

            with col2:

                st.markdown(
                    f"""
### {item['name']}

**Category:** {item['category']}

**Purchases:** {item['purchases']}
"""
                )

            st.divider()


# =====================================================
# FREQUENTLY BOUGHT TOGETHER
# =====================================================

elif page == "Frequently Bought Together":

    st.header(
        "🛒 Frequently Bought Together"
    )

    selected_product = st.number_input(
        "Enter Product ID",
        min_value=int(
            products_df[
                "product_id"
            ].min()
        ),
        max_value=int(
            products_df[
                "product_id"
            ].max()
        ),
        step=1
    )

    if st.button(
        "Find Related Products",
        use_container_width=True
    ):

        related_products = (

            fbt_service
            .get_recommendations(
                selected_product,
                top_n=5
            )

        )

        if related_products:

            st.success(
                f"Found {len(related_products)} related products"
            )

            related_df = pd.DataFrame(
                related_products,
                columns=[
                    "Product ID",
                    "Frequency"
                ]
            )

            st.dataframe(
                related_df,
                use_container_width=True
            )

            chart = px.bar(
                related_df,
                x="Product ID",
                y="Frequency",
                title="Frequently Bought Together"
            )

            st.plotly_chart(
                chart,
                use_container_width=True
            )

        else:

            st.warning(
                "No related products found."
            )

            
import streamlit as st


def set_page_config():
    """Configure page settings and styling"""
    st.set_page_config(
        page_title="Gramedians",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
        .book-card {
            border: 1px solid #2e2e2e;
            border-radius: 12px;
            padding: 20px;
            width: 100%;
            height: 100%;
            text-align: center;
            background-color: #1e1e1e;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 20px;
        }
        .book-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        }
        .book-card img {
            border-radius: 8px;
            max-height: 250px;
            object-fit: cover;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .book-title {
            font-size: 16px;
            font-weight: bold;
            margin: 12px 0;
            color: #ffffff;
            line-height: 1.4;
        }
        .book-desc {
            font-size: 14px;
            color: #b0b0b0;
            margin: 10px 0;
            line-height: 1.6;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        .book-price {
            font-size: 18px;
            font-weight: bold;
            color: #00ff88;
            margin: 15px 0;
        }
        .buy-button {
            background-color: #00ff88;
            color: #1e1e1e;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
            transition: background-color 0.2s;
        }
        .buy-button:hover {
            background-color: #00cc6a;
        }
        .detail-container {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 15px;
            margin-top: 20px;
        }
        .section-title {
            color: #00ff88;
            font-size: 24px;
            margin-bottom: 20px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

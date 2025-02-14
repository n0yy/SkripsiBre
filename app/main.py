import streamlit as st
import numpy as np
from utils.loader import books
from utils.recommender import BookRecomendation

st.set_page_config(page_title="Dosan Book Store", layout="wide")

if "selected_book" not in st.session_state:
    st.title("📚 Dosan Book Recommendation System")
    st.write("Temukan buku terbaik untuk Anda!")

st.markdown(
    """
    <style>
    .book-card {
        border: 1px solid #e1e4e8;
        border-radius: 10px;
        padding: 15px;
        width: 100%;
        height: auto;
        text-align: center;
        background-color: #000;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 1em;
    }
    .book-card img {
        border-radius: 10px;
        max-height: 200px;
        object-fit: cover;
    }
    .book-title {
        font-size: 12px;
        font-weight: bold;
        margin-top: 10px;
        color: #f0f0f0;
    }
    .book-desc {
        font-size: 14px;
        color: #666;
        height: 60px;
        overflow: hidden;
    }
    .book-price {
        font-size: 16px;
        font-weight: bold;
        color: #fff;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'selected_book' in st.session_state:
    model = BookRecomendation()
    book = st.session_state['selected_book']
    cols = st.columns(2)
    with cols[0]:
        st.title(book['title'])
        st.image(book['ImageURL'], width=300)
        st.write(book['description'])
        st.write(f"💰 Harga: {book['price']}")
        st.markdown(f"[Beli Sekarang]({book['bookURL']})", unsafe_allow_html=True)
        if st.button("Kembali ke Home"):
            del st.session_state['selected_book']
            st.rerun()

        book_similarity = model.recommend(books[book["bookURL"] == books["bookURL"]].index[0])
        cols = st.columns(4)
        for i, idx in enumerate(book_similarity.index):
            recommend = book_similarity.loc[idx]
            with cols[i % 4]:
                st.markdown(
                f"""
                <div class="book-card">
                    <img src="{recommend['ImageURL']}" width="100%">
                    <div class="book-title">{recommend['title']}</div>
                    <p class="book-desc">{recommend['description'][:100]}...</p>
                    <div class="book-price">💰 Harga: {recommend['price']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    random_idx = np.random.randint(low=0, high=len(books), size=8)
    cols = st.columns(4) 

    for i, idx in enumerate(random_idx):
        book = books.loc[idx]
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="book-card">
                    <img src="{book['ImageURL']}" width="100%">
                    <div class="book-title">{book['title']}</div>
                    <p class="book-desc">{book['description'][:100]}...</p>
                    <div class="book-price">💰 Harga: {book['price']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"➡ Lihat Detail {i}"):
                st.session_state['selected_book'] = book
                st.rerun()

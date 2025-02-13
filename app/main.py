import streamlit as st
import numpy as np
from utils.loader import books, embedding

st.set_page_config(page_title="Dosan Book Store", layout="wide")

st.title("📚 Dosan Book Recommendation System")
st.write("Temukan buku terbaik untuk Anda!")

# Generate random in
random_idx = np.random.randint(low=0, high=len(books), size=10)

cols = st.columns(2)

for i, idx in enumerate(random_idx):
    book = books.loc[idx]
    with cols[i % 2]:
        with st.container():
            st.image(book["ImageURL"], width=150)
            st.subheader(book["title"])
            st.write(book["description"][:200] + "...")
            st.write(f"💰 Harga: {book['price']}")
            st.markdown(f"[🛒 Beli Sekarang]({book['bookURL']})", unsafe_allow_html=True)
            st.markdown("---")

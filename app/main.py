import streamlit as st
from utils.loader import books
from utils.ui import render_book_card, render_book_detail, render_recommendations
from utils.config import set_page_config


def init_session_state():
    """Initialize session state variables"""
    if "selected_book" not in st.session_state:
        st.session_state.selected_book = None
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""


def search_books(query):
    """Search books by title or description"""
    if not query:
        return None
    query = query.lower()
    return books[books["title"].str.lower().str.contains(query)]


def main():
    init_session_state()
    set_page_config()

    if st.session_state.selected_book is None:
        st.title("📚 Gramedians Book Store")
        st.write("Temukan buku terbaik untuk Anda!")

        # Search bar
        st.session_state.search_query = st.text_input(
            "🔍 Cari buku...", value=st.session_state.get("search_query", "")
        )

        filtered_books = search_books(st.session_state.search_query)

        if filtered_books is None:
            st.info("Masukkan kata kunci pencarian untuk menemukan buku.")
        elif len(filtered_books) == 0:
            st.warning("Tidak ada buku yang ditemukan.")
        else:
            cols = st.columns(4)
            for i, (_, book) in enumerate(filtered_books.iterrows()):
                with cols[i % 4]:
                    render_book_card(book, i)
    else:
        if st.button("← Kembali ke Home"):
            st.session_state.selected_book = None
            st.rerun()

        render_book_detail(st.session_state.selected_book)
        render_recommendations(st.session_state.selected_book)


if __name__ == "__main__":
    main()

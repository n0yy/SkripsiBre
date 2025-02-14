import streamlit as st
import numpy as np
from utils.loader import books
from utils.recommender import BookRecomendation

def init_session_state():
    """Initialize session state variables"""
    if "selected_book" not in st.session_state:
        st.session_state.selected_book = None
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""

def set_page_config():
    """Configure page settings and styling"""
    st.set_page_config(
        page_title="Dosan Book Store",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.markdown("""
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
    """, unsafe_allow_html=True)

def render_book_card(book, index=None, show_button=True):
    """Render a single book card"""
    # Convert Series to dict if necessary
    book_data = book.to_dict() if hasattr(book, 'to_dict') else book
    
    card_html = f"""
        <div class="book-card">
            <img src="{book_data['ImageURL']}" width="100%">
            <div class="book-title">{book_data['title']}</div>
            <p class="book-desc">{book_data['description'][:150]}...</p>
            <div class="book-price">💰 Rp {book_data['price']:,.2f}</div>
        </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    if show_button:
        if st.button(f"Lihat Detail", key=f"detail_{index}" if index is not None else "detail_single"):
            st.session_state.selected_book = book_data
            st.rerun()

def render_book_detail(book):
    """Render the detailed view of a book"""
    # Convert Series to dict if necessary
    book_data = book.to_dict() if hasattr(book, 'to_dict') else book
    
    st.markdown(f"<h1 style='color: #00ff88;'>{book_data['title']}</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(book_data['ImageURL'], use_container_width =True)
    
    with col2:
        st.markdown("<div class='detail-container'>", unsafe_allow_html=True)
        st.markdown(f"<h3>Deskripsi</h3>", unsafe_allow_html=True)
        st.write(book_data['description'])
        st.markdown(f"<div class='book-price'>💰 Rp {book_data['price']:,.2f}</div>", unsafe_allow_html=True)
        st.markdown(f"<a href='{book_data['bookURL']}' class='buy-button' target='_blank'>Beli Sekarang</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def render_recommendations(book):
    """Render book recommendations"""
    # Convert Series to dict if necessary
    book_data = book.to_dict() if hasattr(book, 'to_dict') else book
    
    st.markdown("<h2 class='section-title'>Rekomendasi Buku Serupa</h2>", unsafe_allow_html=True)
    model = BookRecomendation()
    book_idx = books[books["bookURL"] == book_data["bookURL"]].index[0]
    book_similarity = model.recommend(book_idx)
    
    cols = st.columns(4)
    for i, idx in enumerate(book_similarity.index[:4]):  # Limit to 4 recommendations
        recommend = book_similarity.loc[idx]
        with cols[i]:
            render_book_card(recommend, i, show_button=True)

def search_books(query):
    """Search books by title or description"""
    if not query:
        return books.sample(8)
    query = query.lower()
    return books[
        books['title'].str.lower().str.contains(query)
    ]

def main():
    init_session_state()
    set_page_config()
    
    # Check if selected_book exists in session state and is not None
    if st.session_state.selected_book is None:
        st.title("📚 Dosan Book Store")
        st.write("Temukan buku terbaik untuk Anda!")
        
        # Search bar
        st.session_state.search_query = st.text_input(
            "🔍 Cari buku...",
            value=st.session_state.get("search_query", "")
        )
        
        filtered_books = search_books(st.session_state.search_query)
        
        if len(filtered_books) == 0:
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
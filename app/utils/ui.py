import streamlit as st
import pandas as pd

def render_book_card(book, index=None, show_button=True):
    """Render a single book card"""
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
    book_data = book.to_dict() if hasattr(book, 'to_dict') else book
    
    st.markdown(f"<h1 style='color: #00ff88;'>{book_data['title']}</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(book_data['ImageURL'], use_container_width=True)
    
    with col2:
        st.markdown("<div class='detail-container'>", unsafe_allow_html=True)
        st.markdown(f"<h3>Deskripsi</h3>", unsafe_allow_html=True)
        st.write(book_data['description'])
        st.markdown(f"<div class='book-price'>💰 Rp {book_data['price']:,.2f}</div>", unsafe_allow_html=True)
        st.markdown(f"<a href='{book_data['bookURL']}' class='buy-button' target='_blank'>Beli Sekarang</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

def render_recommendations(book):
    """Render book recommendations"""
    from utils.recommender import BookRecomendation
    from utils.loader import books
    
    book_data = book.to_dict() if hasattr(book, 'to_dict') else book
    
    st.markdown("<h2 class='section-title'>Rekomendasi Buku Serupa</h2>", unsafe_allow_html=True)
    model = BookRecomendation()
    book_idx = books[books["bookURL"] == book_data["bookURL"]].index[0]
    book_similarity = model.recommend(book_idx)
    
    cols = st.columns(4)
    for i, idx in enumerate(book_similarity.index[:4]):
        recommend = book_similarity.loc[idx]
        with cols[i]:
            render_book_card(recommend, i, show_button=True)
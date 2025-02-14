import numpy as np
import pandas as pd

from utils import loader
from sklearn.metrics.pairwise import cosine_similarity

class BookRecomendation:
    def __init__(self):
        self.embedding = loader.embedding
        self.books = loader.books
    def calc_similar(self, idx: int, top_n: int = 10):
        similarity_scores = cosine_similarity(self.embedding[idx].reshape(1, -1), self.embedding)[0]
        top_indices = np.argpartition(-similarity_scores, top_n + 1)[:top_n + 1]  # Ambil top (top_n + 1)
        top_indices = top_indices[top_indices != idx]  # Hapus indeks yang sama dengan idx
        return top_indices[:top_n] 

    
    def recommend(self, idx: int, top_n: int = 10) -> pd.DataFrame:
        top_indices = self.calc_similar(idx, top_n)
        return self.books.loc[top_indices, ["title", "description", "price", "ImageURL", "bookURL"]]

import pandas as pd
import numpy as np

books = pd.read_csv("./data/cleaned/books.csv")
embedding = np.load("./models/embedding.npz")["embedding"]
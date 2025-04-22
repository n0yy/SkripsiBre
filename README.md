# Gramedians Book Store - Sistem Rekomendasi Buku

## Deskripsi Proyek

Gramedians Book Store adalah aplikasi berbasis web yang menyediakan sistem pencarian dan rekomendasi buku. Aplikasi ini dikembangkan menggunakan Streamlit dan mengimplementasikan sistem rekomendasi berbasis konten (content-based filtering) dengan menggunakan teknik embedding dan perhitungan similaritas antar buku.

## Fitur Utama

- Pencarian buku berdasarkan judul atau deskripsi
- Detail informasi buku (judul, harga, deskripsi, dll)
- Sistem rekomendasi buku berdasarkan similaritas konten

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama
- **Streamlit**: Framework untuk pengembangan antarmuka web
- **Pandas**: Manipulasi dan analisis data
- **NumPy**: Komputasi numerik
- **Google GenAI**: Pembuatan embedding teks
- **Scikit-learn**: Perhitungan cosine similarity

## Struktur Proyek

```
gramedians-book-store/
├── app/
│   ├── main.py                 # Aplikasi Streamlit utama
│   └── utils/
│       ├── loader.py           # Modul untuk memuat data buku
│       ├── ui.py               # Komponen UI
│       └── config.py           # Konfigurasi aplikasi
├── data/
│   ├── books-v2.csv            # Dataset mentah buku
│   ├── cleaned/
│   │   └── books.csv           # Dataset buku setelah preprocessing
│   ├── books_with_embedding.csv # Dataset dengan embedding
│   └── processed/
│       └── books.parquet       # Dataset final (format parquet)
├── models/
│   └── embeddings.npz          # Model embedding tersimpan
├── notebooks/
│   ├── 1. Preprocessing.ipynb  # Notebook preprocessing data
│   ├── 2. Similarity.ipynb     # Notebook perhitungan similaritas
│   └── 3. Calculation of Similarity.ipynb # Notebook analisis similaritas
└── README.md                   # Dokumentasi proyek
```

## Workflow Pengembangan

### 1. Preprocessing Data

Data buku dari Gramedia diproses melalui tahapan berikut:

- Membaca data CSV mentah
- Menghapus kolom yang tidak diperlukan (metadata)
- Memeriksa dan menangani nilai null
- Menyaring buku dengan deskripsi yang terlalu pendek
- Menggabungkan title dan description untuk membuat kolom "text"
- Menyimpan hasil preprocessing ke file CSV

### 2. Pembuatan Embedding

- Menggunakan Google GenAI API (model text-embedding-004)
- Mengubah teks (judul + deskripsi) menjadi vektor embedding
- Menyimpan embedding dalam format numpy array

### 3. Perhitungan Similaritas

- Menghitung cosine similarity antara embedding buku
- Implementasi perhitungan similaritas menggunakan scikit-learn
- Alternatif implementasi dari scratch menggunakan numpy
- Membuat fungsi untuk mendapatkan top-N rekomendasi berdasarkan similaritas

### 4. Pengembangan Aplikasi

- Membangun interface aplikasi menggunakan Streamlit
- Implementasi fitur pencarian buku
- Menampilkan detail buku yang dipilih
- Menampilkan rekomendasi buku berdasarkan similaritas konten

## Cara Menjalankan Aplikasi

### Prasyarat

- Python 3.11+
- Library yang tercantum dalam requirements.txt

### Langkah-langkah Instalasi

1. Clone repositori ini

   ```bash
   git clone https://github.com/username/gramedians-book-store.git
   cd gramedians-book-store
   ```

2. Buat virtual environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Untuk Linux/Mac
   # atau
   .venv\Scripts\activate  # Untuk Windows
   ```

3. Install dependensi

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi

   ```bash
   streamlit run app/main.py
   ```

5. Buka browser dan akses `http://localhost:8501`

## Alur Kerja Sistem Rekomendasi

1. **Input Pencarian**

   - Pengguna memasukkan kata kunci pencarian
   - Sistem memfilter buku berdasarkan kata kunci

2. **Pemilihan Buku**

   - Pengguna memilih buku dari hasil pencarian
   - Sistem menampilkan detail buku

3. **Generate Recomendation**
   - Sistem mengambil embedding buku yang dipilih
   - Menghitung cosine similarity dengan semua buku lain
   - Mengurutkan buku berdasarkan skor similaritas
   - Menampilkan top-N buku yang paling mirip

## Penjelasan Metode Cosine Similarity

Cosine similarity antara dua vektor A dan B didefinisikan sebagai:

$\text{cosine\_similarity}(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \cdot \|\mathbf{B}\|}$

Untuk kasus membandingkan satu vektor A dengan seluruh matriks embedding M:

$\text{cos\_sim} = \frac{\mathbf{A} \cdot \mathbf{M}^T}{\|\mathbf{A}\| \cdot \|\mathbf{M}\|_{\text{row-wise}}}$

Dimana:

- $\mathbf{A} \cdot \mathbf{M}^T$: Dot product antara vektor $\mathbf{A}$ dan setiap baris dari matriks $\mathbf{M}$
- $\|\mathbf{A}\|$: Norma (panjang) dari vektor $\mathbf{A}$
- $\|\mathbf{M}\|_{\text{row-wise}}$: Norma masing-masing baris (vektor) dalam matriks $\mathbf{M}$

## Future Improvements

- Implementasi sistem rekomendasi kolaboratif
- Optimasi performa pada dataset yang lebih besar
- Penambahan fitur kategori dan filter
- Implementasi feedback pengguna untuk meningkatkan rekomendasi
- Integrasi dengan API pembelian buku

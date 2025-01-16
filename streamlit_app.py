import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = 'all_data.csv'

@st.cache_data
def load_data(file_path):
    """Memuat data dari file csv."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"File {file_path} tidak ditemukan. Pastikan file berada di direktori yang benar.")
        return None

data = load_data(FILE_PATH)

if data is not None:
    
    st.markdown("<h1 style='text-align: center; color: blue;'>DATA ANALISIS DENGAN PYTHON</h1>", unsafe_allow_html=True)
    st.image("eCommerce.png", caption="Analisis Data E-Commerce", use_container_width=True)

    # Filter interaktif untuk review score
    st.sidebar.header ("Cek Jumlah Pesanan Berdasarkan Review Score")
    review_score_options = sorted(data['review_score'].dropna().unique())
    selected_score = st.sidebar.selectbox("Pilih Review Score untuk Ditampilkan:",
        options=review_score_options
    )

    # Filter data berdasarkan pilihan pengguna
    filtered_data = data[data['review_score'] == selected_score]
    review_counts = filtered_data['review_score'].value_counts().sort_index()
    customer_count = len(filtered_data)
    
    st.sidebar.write(f"### Jumlah Yang Mendapatkan Review Score **{selected_score}** adalah: **{customer_count}** Pesanan")
    st.write(f"## Grafik Jumlah Pesanan Yang Mendapatkan Review Score **{selected_score}**")

    # Data untuk visualisasi
    review_counts = filtered_data['review_score'].value_counts().sort_index() 

    scores = review_counts.index.tolist()
    counts = review_counts.values
    colors = ['gray'][:len(scores)]

    fig, ax = plt.subplots()
    ax.bar(scores, counts, color=colors)
    ax.set_title(None)
    ax.set_xlabel(f"Terdapat {customer_count} Pelanggan")
    ax.set_ylabel("Jumlah Pesanan")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)
   
    st.write("# Gambaran Secara Umum")    
    st.write(
        """
        ## Tingkat Kepuasan Pelanggan
        Berikut Merupakan Grafik Tingkat Kepuasan Pelanggan Berdasarkan Review Score.
        """
    )

    review_counts = data['review_score'].value_counts().sort_index()

    scores = review_counts.index.tolist()
    counts = review_counts.values
    colors = ['lime', 'blue', 'red', 'magenta', 'gold'][:len(scores)]

    fig, ax = plt.subplots()
    ax.bar(scores, counts, color=colors)
    ax.set_title("Tingkat Kepuasan Pelanggan")
    ax.set_xlabel("Review Score")
    ax.set_ylabel("Jumlah")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

    st.write(
        """
        ## Produk Yang Banyak Dibeli Pelanggan
        Berikut Merupakan Grafik Produk Yang Paling Banyak Dibeli Pelanggan.
        """
    )

    product_counts = data['product_category_name_english'].value_counts()

    products = product_counts.index.tolist()
    counts = product_counts.values
    colors = ['blue', 'cyan', 'magenta', 'gold', 'lime', 'gray'][:len(products)]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(products, counts, color=colors)
    ax.set_title("Produk Paling Banyak Dibeli")
    ax.set_xlabel("Nama Produk")
    ax.set_ylabel("Jumlah")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

else:
    st.warning("Tidak ada data yang bisa ditampilkan, periksa file csv")

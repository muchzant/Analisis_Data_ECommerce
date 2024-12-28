# Visualisasi Data Pelanggan

Streamlit memvisualisasikan kepuasan pelanggan, termasuk produk yang paling sering dibeli berdasarkan dataset yang disediakan.

## Fitur
- **Visualisasi Grafik Batang**: Menampilkan tingakt kepuasan dan jumlah produk yang dibeli oleh pelanggan, dikelompokkan berdasarkan jenis produk.
- **Antarmuka Interaktif**: Aplikasi web Streamlit yang mudah digunakan untuk eksplorasi data.

## Requirements
Untuk menjalankan ini, diperlukan:

- Python 3.13.1 atau versi lebih baru
- Library yang dibutuhkan:
  - `babel==2.16.0`
  - `matplotlib==3.10.0`
  - `numpy==2.2.1`
  - `pandas==2.2.3`
  - `seaborn==0.13.2`
  - `streamlit==1.41.1`
  
## Instalasi
1. Clone repositori ini atau unduh dataset `all_data.csv` dan script Python-nya.

2. Instal library Python yang dibutuhkan:

3. Pastikan file `all_data.csv` berada di direktori yang sama dengan script Python.

## Cara Menjalankan
1. Jalankan aplikasi Streamlit dengan perintah berikut di terminal:

  - streamlit run `bar.py`

2. Aplikasi akan terbuka di browser default Anda. Jika tidak, salin URL dari terminal dan tempelkan ke browser Anda.

## Output

- Menampilkan grafik batang yang memvisualisasikan kepuasan pelanggan dan produk yang paling sering dibeli berdasarkan data di `all_data.csv`.

## Informasi Dataset
- **File**: `all_data.csv`
- **Deskripsi**: Berisi data pelanggan, termasuk nama kategori produk dan jumlah pembelian.

## Kustomisasi
Anda dapat mengkustomisasi visualisasi dengan:
- Memperbarui variabel `file_path` untuk memuat dataset yang berbeda.
- Memodifikasi judul grafik, label, atau warna dalam kode.

## Pemecahan Masalah
- Pastikan file `all_data.csv` ada dan diformat dengan benar.
- Pastikan semua library yang dibutuhkan telah diinstal.

## Lisensi
Proyek ini bersifat open-source.



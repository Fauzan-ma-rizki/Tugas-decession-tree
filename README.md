📂 Struktur File
Pastikan file dataset berada di dalam satu folder yang sama dengan script Python yang akan dijalankan:

student_lifestyle_dataset.xlsx : File dataset utama yang berisi data gaya hidup mahasiswa.

data latih 10.py : Script untuk Skenario 1 (Menggunakan 11 data awal).

semua data.py : Script untuk Skenario 2 (Menggunakan seluruh data).

🚀 Skenario Pengujian
Skenario 1: Pengujian Data Terbatas (Poin 1 & 2 Tugas)
Dataset: Menggunakan 10 baris pertama sebagai data latih (Train) dan baris ke-11 sebagai data uji (Test).

Parameter Model: 5 Pohon Keputusan (n_estimators=5), maksimal 1 fitur (max_features=1), kedalaman maksimal 1 (max_depth=1).

Visualisasi: Menampilkan plot tepat 5 pohon sederhana.

Tujuan: Memahami cara kerja dasar Random Forest secara manual/terbatas. Model pada tahap ini sengaja dibuat lemah (underfitting), sehingga wajar jika prediksinya mungkin meleset.

Skenario 2: Pengujian Seluruh Data (Poin 4 Tugas)
Dataset: Menggunakan seluruh baris data dengan pembagian 80% untuk data latih dan 20% untuk data uji.

Parameter Model: 100 Pohon Keputusan (n_estimators=100) dengan parameter standar, sehingga model bekerja dengan kapasitas maksimal.

Visualisasi: Hanya menampilkan plot 10 pohon pertama untuk kebutuhan presentasi (agar jendela popup rapi, tidak berat, dan teks terbaca jelas).

Tujuan: Melihat performa asli model. Dengan data yang lengkap dan 100 pohon pendukung, model mampu mencapai akurasi sangat tinggi.

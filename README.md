# PERTEMUAN 11 - DICTIONARY/MAP

## Identitas Mahasiswa

* **Nama:** Reva Liyanasari
* **NIM:** 2225250101
* **Kelas:** 3A
* **Mata Kuliah:** Algoritma dan Pemrograman
* **Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.

## Tujuan Repositori

Repositori ini dibuat untuk memenuhi kegiatan praktik mata kuliah Algoritma dan Pemrograman pada Pertemuan 11 dengan materi dictionary/map dan pasangan key-value dalam Python.

Melalui praktik ini, mahasiswa diharapkan mampu:
- Membuat dictionary menggunakan pasangan key-value.
- Mengakses data menggunakan key.
- Menggunakan `get()` untuk menangani key yang tidak tersedia.
- Menambah dan memperbarui data dalam dictionary.
- Menelusuri data menggunakan `items()`.
- Menggunakan fungsi untuk melakukan pencarian dan perhitungan rata-rata nilai.
- Memodelkan data pendidikan menggunakan dictionary bersarang.
- Melakukan pengujian program berdasarkan test case yang ditentukan.

## Daftar Berkas

### Praktik 2 - Sistem Data Mahasiswa

**`praktik/data_mahasiswa.py`**

Program sistem data mahasiswa menggunakan dictionary dengan NIM sebagai key utama. Setiap value berupa dictionary yang menyimpan nama, kelas, dan nilai mahasiswa.

Program menyediakan operasi pencarian mahasiswa berdasarkan NIM, penambahan mahasiswa baru, pembaruan nilai, penampilan seluruh data mahasiswa, serta perhitungan rata-rata nilai.

Program menggunakan fungsi `cari_mahasiswa()` untuk mencari data mahasiswa dan fungsi `rata_rata_nilai()` untuk menghitung rata-rata nilai seluruh mahasiswa. Method `get()` digunakan untuk menangani pencarian NIM yang tidak tersedia, sedangkan `items()` digunakan untuk menelusuri NIM beserta data setiap mahasiswa.

## Cara Menjalankan

1. Buka folder repositori melalui Visual Studio Code.
2. Buka terminal pada direktori utama repositori.
3. Jalankan perintah berikut:

   ```bash
   python3 praktik/data_mahasiswa.py
   ```

4. Periksa hasil pencarian mahasiswa berdasarkan NIM.
5. Periksa hasil penambahan dan pembaruan data mahasiswa.
6. Periksa rekap seluruh data dan hasil perhitungan rata-rata nilai.

Jika perintah `python3` tidak dikenali pada Windows, gunakan:

   ```bash
   python praktik/data_mahasiswa.py
   ```

## Struktur Data dan Fungsi

### 1. Dictionary `data_mahasiswa`

Dictionary `data_mahasiswa` digunakan untuk menyimpan data mahasiswa dengan NIM sebagai key utama. Setiap value berisi dictionary yang memiliki tiga atribut, yaitu nama, kelas, dan nilai.

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78}
}
```

### 2. Fungsi `cari_mahasiswa(data, nim)`

Digunakan untuk mencari data mahasiswa berdasarkan NIM. Fungsi ini menggunakan method `get()` agar program dapat menampilkan pesan `"Data tidak ditemukan"` apabila NIM tidak tersedia.

### 3. Fungsi `rata_rata_nilai(data)`

Digunakan untuk menghitung rata-rata nilai seluruh mahasiswa. Fungsi memeriksa apakah dictionary kosong, menjumlahkan nilai mahasiswa menggunakan `sum()`, kemudian membaginya dengan jumlah mahasiswa menggunakan `len()`.

### 4. Penambahan Data Mahasiswa

Data mahasiswa baru ditambahkan menggunakan key `"A006"` dengan nama Fajar, kelas C, dan nilai 80.

### 5. Pembaruan Nilai Mahasiswa

Nilai mahasiswa dengan NIM `"A002"` diperbarui dari 78 menjadi 82 melalui akses dictionary bersarang.

### 6. Rekap Data Mahasiswa

Method `items()` digunakan untuk mengambil pasangan key dan value sehingga seluruh NIM, nama, kelas, dan nilai mahasiswa dapat ditampilkan menggunakan perulangan.

## Hasil Pengujian

| No. | Pengujian | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Pencarian mahasiswa tersedia | NIM: `A003` | Data Citra, kelas B, nilai 92 ditampilkan | Data Citra, kelas B, nilai 92 ditampilkan | Berhasil |
| 2 | Pencarian mahasiswa tidak tersedia | NIM: `A006` sebelum penambahan | Pesan `Data tidak ditemukan` ditampilkan | Pesan `Data tidak ditemukan` ditampilkan | Berhasil |
| 3 | Penambahan mahasiswa | NIM: `A006` | Data Fajar berhasil ditambahkan | Data Fajar, kelas C, nilai 80 ditambahkan | Berhasil |
| 4 | Pembaruan nilai mahasiswa | NIM: `A002`, nilai baru: `82` | Nilai Budi berubah dari 78 menjadi 82 | Nilai Budi berubah menjadi 82 | Berhasil |
| 5 | Rekap data mahasiswa | Menggunakan `items()` | Seluruh data mahasiswa ditampilkan | Seluruh data mahasiswa ditampilkan | Berhasil |
| 6 | Perhitungan rata-rata nilai | Seluruh 6 mahasiswa setelah pembaruan | Rata-rata nilai sebesar 83,50 | Rata-rata nilai sebesar 83,50 | Berhasil |

## Refleksi

Melalui praktik ini, saya mempelajari bahwa dictionary dapat digunakan untuk menyimpan data secara terstruktur menggunakan pasangan key-value. Penggunaan NIM sebagai key memudahkan pencarian data mahasiswa tanpa harus mencari berdasarkan posisi indeks seperti pada list.

Saya juga mempelajari penggunaan `get()` untuk menangani key yang tidak tersedia, penambahan dan pembaruan data menggunakan assignment, serta penggunaan `items()` untuk menelusuri seluruh pasangan key-value.

Salah satu kesalahan yang dapat terjadi adalah mengakses key yang belum tersedia menggunakan tanda kurung siku, misalnya `data["A006"]`. Jika key tersebut belum ada, Python dapat menghasilkan `KeyError`. Kesalahan ini dapat diatasi dengan menggunakan `get()`, seperti `data.get(nim, "Data tidak ditemukan")`, sehingga program dapat memberikan pesan yang sesuai tanpa mengalami `KeyError`.

Praktik ini membantu saya memahami penerapan dictionary bersarang dan fungsi dalam mengelola data pendidikan menggunakan Python.

## Sumber

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 11, Dictionary/Map dan Pasangan Key-Value dalam Python.
- Python Software Foundation, dokumentasi Python 3 mengenai dictionary dan struktur data.
# Pertemuan 09 - List dan Pengolahan Data Numerik

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Fikri Yustiawan |
| **NIM** | 2225250075 |
| **Kelas** | 3E |
| **Jurusan** | Pendidikan Matematika |

## Tujuan
Mengolah kumpulan data numerik dengan list Python: akses indeks, slicing, manipulasi elemen, perulangan, agregasi, dan fungsi yang menerima list.

## Struktur Program
```
pertemuan-09-list-2225250075/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_buat_list.py          # membuat list, len()
|   |-- 02_indeks_slicing.py     # indeks positif/negatif, slicing
|   |-- 03_manipulasi_list.py    # ubah, append, insert, remove
|   |-- 04_agregasi_nilai.py     # sum, len, min, max, rata-rata
|   |-- 05_filter_kelulusan.py   # for + if, list lulus baru
|   `-- 06_fungsi_statistik.py   # fungsi rata_rata (aman list kosong)
`-- praktik/
    |-- analisis_nilai_mahasiswa.py  # program utama (10 nilai, batas 60)
    `-- uji_test_case.py             # pengujian test case wajib
```

## Cara Menjalankan
```
python3 praktik/analisis_nilai_mahasiswa.py
python3 praktik/uji_test_case.py
```
(Di Windows gunakan `python`.)

## Hasil Praktik (data: [78, 55, 90, 67, 60, 82, 45, 71, 88, 59])
| Keluaran | Nilai |
|---|---|
| Banyak data | 10 |
| Total | 695 |
| Rata-rata | 69.50 |
| Minimum / Maksimum | 45 / 90 |
| Nilai lulus | [78, 90, 67, 60, 82, 71, 88] |
| Jumlah lulus / belum lulus | 7 / 3 |

## Test Case
| Data | Yang diperiksa | Harapan | Aktual | Status |
|---|---|---|---|---|
| [60, 70, 80] | Rata-rata | 70.00 | 70.00 | Lulus |
| [60, 70, 80] | Minimum | 60 | 60 | Lulus |
| [60, 70, 80] | Maksimum | 80 | 80 | Lulus |
| [60, 70, 80] | Jumlah lulus | 3 | 3 | Lulus |
| [59, 60, 61] | Jumlah lulus (batas 60) | 2 | 2 | Lulus |
| [] | rata_rata tidak error | 0 | 0 | Lulus |

## Refleksi
- Yang saya pahami: indeks list dimulai dari 0, bukan 1, dan pada slicing `nilai[1:4]` batas akhir (indeks 4) tidak ikut diambil, jadi hasilnya hanya indeks 1, 2, dan 3. Indeks negatif seperti `nilai[-1]` berguna untuk mengambil elemen terakhir tanpa perlu menghitung panjang list.
- Kesalahan yang berhasil diperbaiki: saat menguji fungsi `rata_rata` dengan list kosong `[]`, program error `ZeroDivisionError` karena `sum(data) / len(data)` membagi dengan 0. Saya memperbaikinya dengan menambahkan pemeriksaan `if len(data) == 0: return 0` sebelum pembagian, lalu mengujinya lagi sampai tidak error.

## Exit Ticket
- Satu keuntungan list dibanding banyak variabel adalah semua nilai tersimpan dalam satu variabel, sehingga bisa dihitung dengan `len`, `sum`, `min`, dan `max` serta ditelusuri dengan satu perulangan `for`, tanpa menulis n1, n2, n3, dan seterusnya.
- Kesalahan indeks yang paling mungkin saya lakukan adalah mengira indeks pertama adalah 1, sehingga mengakses `nilai[len(nilai)]` dan mendapat `IndexError`. Indeks terakhir yang valid adalah `len(nilai) - 1`, atau cukup `nilai[-1]`.
- Konsep Pertemuan 7 yang paling membantu pada Pertemuan 9 adalah fungsi, karena proses seperti `rata_rata(data)` dan `nilai_lulus(data)` cukup ditulis sekali lalu dipakai untuk list apa pun.
- Hal yang perlu saya siapkan untuk materi string pada Pertemuan 10 adalah memantapkan indeks, slicing, dan iterasi, karena string juga urutan karakter yang diakses dengan cara yang sama seperti list.

## Sumber dan Bantuan
- Bahan ajar Pertemuan 09, Algoritma dan Pemrograman (Dr. Aan Hendrayana, S.Si., M.Pd.).
- Dokumentasi Python 3: Data Structures.
- Bantuan AI (Claude) digunakan untuk menyusun draf kode, README, dan pengujian; saya telah membaca dan menjalankan seluruh kode tersebut.

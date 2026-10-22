# Pengujian test case wajib (jalankan: python3 praktik/uji_test_case.py)
from analisis_nilai_mahasiswa import rata_rata, nilai_lulus

kasus = [
    ("[60,70,80] rata-rata 70.00", f"{rata_rata([60, 70, 80]):.2f}", "70.00"),
    ("[60,70,80] minimum", str(min([60, 70, 80])), "60"),
    ("[60,70,80] maksimum", str(max([60, 70, 80])), "80"),
    ("[60,70,80] jumlah lulus", str(len(nilai_lulus([60, 70, 80]))), "3"),
    ("[59,60,61] jumlah lulus", str(len(nilai_lulus([59, 60, 61]))), "2"),
    ("[] rata_rata tidak error", str(rata_rata([])), "0"),
]

semua_ok = True
for nama, aktual, harapan in kasus:
    status = "LULUS" if aktual == harapan else "GAGAL"
    if status == "GAGAL":
        semua_ok = False
    print(f"{status:6} | {nama:28} | harapan={harapan:6} aktual={aktual}")

print("\nSemua test case lulus." if semua_ok else "\nAda test case gagal.")

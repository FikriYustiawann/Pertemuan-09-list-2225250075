# Latihan 6 - Fungsi statistik
# Input  : list nilai
# Proses : fungsi rata_rata yang aman untuk list kosong
# Output : rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata = {rata_rata(nilai):.2f}")
print(f"Rata-rata list kosong = {rata_rata([]):.2f}")

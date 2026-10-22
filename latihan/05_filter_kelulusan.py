# Latihan 5 - Filter kelulusan
# Input  : list nilai, batas lulus 60
# Proses : telusuri tiap nilai, simpan yang >= 60
# Output : list nilai lulus dan jumlahnya
nilai = [75, 55, 80, 60, 45, 90]
lulus = []
for x in nilai:
    if x >= 60:
        lulus.append(x)
print(f"Nilai lulus  = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")

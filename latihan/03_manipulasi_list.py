# Latihan 3 - Manipulasi list
# Input  : list [75, 80, 65]
# Proses : ubah, tambah, sisip, hapus
# Output : list akhir
nilai = [75, 80, 65]
nilai[1] = 82        # [75, 82, 65]
nilai.append(90)     # [75, 82, 65, 90]
nilai.insert(1, 70)  # [75, 70, 82, 65, 90]
nilai.remove(65)     # [75, 70, 82, 90]
print(nilai)

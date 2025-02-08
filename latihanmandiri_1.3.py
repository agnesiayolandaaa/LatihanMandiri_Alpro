modalAwal = 200000000
bunga_pertahun = 0.10
tahun = 0
target = 400000000

while modalAwal < target : 
    modalAwal += modalAwal * bunga_pertahun
    tahun += 1

print(f'Waktu yang dibutuhkan untuk mencapai target adalah {tahun}tahun')
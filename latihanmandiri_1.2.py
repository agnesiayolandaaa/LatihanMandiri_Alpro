beliemas_awal = 650000
beratemas_awal= 25

#harga emas setelah naik
harga_emasAwalNaik = 685000

modal_awal = beliemas_awal*beratemas_awal

#total emas setelah harga emas naik
total_emasawal = harga_emasAwalNaik * beratemas_awal
keuntungan_rupiah = total_emasawal - modal_awal
keuntungan_persen = (keuntungan_rupiah / modal_awal) * 100

print(f"Keuntungan dalam rupiah: {keuntungan_rupiah}, rupiah")
print(f"Keuntungan dalam persen: {keuntungan_persen:.2f}%")

#Gerard beli emas kedua 15 gram
beliemas_kedua = 685000
beratemas_kedua= 15
harga_emasKeduaNaik = 715000
modal_kedua = beliemas_kedua * beratemas_kedua

total_beratemas = beratemas_awal + beratemas_kedua
total_emaskedua = total_beratemas * harga_emasKeduaNaik
modalSemua= modal_awal + modal_kedua

keuntungan_rupiah = total_emaskedua - modalSemua
keuntungan_persen = (keuntungan_rupiah / modalSemua) * 100

print(f"Keuntungan dalam rupiah: {keuntungan_rupiah}, rupiah")
print(f"Keuntungan dalam persen: {keuntungan_persen:.2f}%")
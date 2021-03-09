#Ini variabel
nama = "Muhammad Hafiz Aditya"
nim = "I0320064"
tempat_lahir = "Magelang"
hobi = "membaca buku dan fotografi"
alasan_1 = "karena membaca buku dapat meningkatkan wawasan dan kemampuan saya dalam berpikir."
alasan_2 = "kegiatan memotret dapat membuat saya merasa ter-refresh, karena hidup itu butuh keseimbangan"
tanggal_lahir = 17
bulan_lahir = 7
tahun_lahir = 2002

#Ini rumus menghitung umur
import datetime
waktu = datetime.datetime.now()

umur_bulan = (waktu.year - tahun_lahir) * 12 + (waktu.month - bulan_lahir) + (waktu.day - tanggal_lahir)/30
umur_tahun = umur_bulan / 12
umur_hari = umur_bulan * 30

#Ini tempat perintah print
print("\n====================\n   Identitas Diri\n====================")
print("\nHai, perkenalkan nama saya",nama,". Saya lahir di", tempat_lahir,"Pada",tanggal_lahir,"-",bulan_lahir,"-",tahun_lahir)
print("\nTepat hari ini saya berumur", round(umur_tahun, 2),"tahun, atau", round(umur_bulan, 2),"dalam bulan, atau",round(umur_hari, 2),"dalam hari")
print("\nSaya memiliki 2 hobi, yakni", hobi, "Saya sangat suka membaca buku", alasan_1,"Sedangkan alasan saya menyukai fotografi ialah", alasan_2)


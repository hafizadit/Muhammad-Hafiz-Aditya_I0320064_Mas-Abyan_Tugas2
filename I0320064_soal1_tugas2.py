
# Program Menghitung Luas Persegi Panjang
print("\n")
print("="*32,"\nProgram Menghitung Luas Persegi Panjang\n================================")

p = float(input("Masukkan nilai panjang :"))
l = float(input("Masukkan nilai lebar :"))

Lpp = p * l

print("\nPersegi panjang anda memiliki panjang =", p, "dan memiliki lebar =",l,"\nSehingga luas persegi panjang anda =", Lpp,"\n")


# Program menghitung luas lingkaran
print("="*32,"\nProgram Menghitung Luas Lingkaran\n================================")

r = float(input("Masukkan nilai jari-jari :"))

Ll = (3.14) * r ** 2

print("\nLingkaran anda memiliki jari-jari =", r, "\nSehingga luas lingkaran anda =", Ll,"\n")


# Program Luas Kubus
print("="*32,"\nProgram Menghitung Luas Kubus\n================================")

s = float(input("Masukkan nilai rusuk kubus :"))

Lk = 6 * s ** 2

print("\nKubus anda memiliki rusuk =", s, "\nSehingga luas kubus anda =", Lk,"\n")


# Program Konversi suhu celcius ke farenheit
print("="*32,"\nProgram Konversi Suhu Celcius ke Farenheit\n================================")

c = float(input("Masukkan suhu dalam Celcius :"))

f = (9/5 * c) + 32

print("\nSuhu dalam celcius =", c, "derajat celcius\nSehingga suhu dalam farenheit =", f,"derajat farenheit\n")

# Program Konversi suhu Reamur ke Kelvin
print("="*32,"\nProgram Konversi Suhu Reamur ke Kelvin\n================================")

reamur = float(input("Masukkan suhu dalam Reamur :"))

kelvin = (5/4 * reamur) + 273

print("\nSuhu dalam reamur =", reamur, "derajat reamur\nSehingga suhu dalam Kelvin =", kelvin,"derajat kelvin")

print("")
print("="*50)
judul = "Program Selesai"
center = judul.center(50)
print(center)
print("="*50)
print("")
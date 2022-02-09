import math 
print("Menghitung Luas Cat Logo Pak Chanek") # Judul
print() # nambah space biar rapi
# Meminta user memasukan data
radius = float(input("Masukan radius lingkaran: ")) # membuat syarat input menjadi tipe float
# syarat agar input yang dimasukan harus => 0
if radius < 0: # berguna untuk menghindari hasil yang negatif jika membuat suatu perhitungan besaran skalar
     print ("Mohon maaf radius yang anda masukan salah")
     print("Masukan bilangan yang => 0")
       

else:
    # Luas segitiga adalah 1/2 * alas * tinggi, alas = 2 * radius, tinggi = radius
    LuasSegitiga = 1/2 * 2 * radius * radius  # Menghitung Luas segitiga        
    Luas_Cat_Segitiga = LuasSegitiga # Menghitung luas cat di dalam segitiga

    LuasLingkaran = math.pi * (radius**2) # Menghitung Luas Lingkaran
    Luas_Cat_Lingkaran = LuasLingkaran - LuasSegitiga # Menghitung luas cat di dalam lingkaran

    #  Luas persegi adalah sisi * sisi, sisi = 2 * radius

    LuasPersegi = (2*radius) ** 2 # Menghitung Luas persegi
    Luas_Cat_Persegi = LuasPersegi - LuasLingkaran # Menghitung luas cat di dalam persegi


    # print output dengan type float yang berpresisi .2f atau mengatur 2 digit di belakqng (.)
    print("Luas daerah cat merah:", "{:.2f}".format(Luas_Cat_Persegi)) 
    print("Luas daerah cat kuning:", "{:.2f}".format(Luas_Cat_Lingkaran))
    print("Luas daerah cat ungu:", "{:.2f}".format(Luas_Cat_Segitiga))
















print("Selamat datang di kalkulator IPK!") # judul
jumlah_matkul = int(input("Masukan jumlah mata kuliah: ")) # meminta user menginput nilai int()
while jumlah_matkul < 0: # mengulang jika masukan < 0
    jumlah_matkul = int(input("Masukan jumlah mata kuliah: "))

# menginisialiasi variabel untuk menyimpan jumlah data
total_mutu = 0 # bobot * total_sks_lulus = menyimpan jumlah bobot per 1 sks untuk matkul yang lulus
total_sks_lulus = 0 # jumlah total sks yang lulus
total_sks = 0 # jumlah total sks
total_nilai = 0 # bobot * total_sks = menyimpan jumlah bobot per 1 sks untuk semua matkul

# membuat sistem pengulangan dengan for loop
for i in range(1,jumlah_matkul+1):
    print() # nambah space
    # meminta user memasukan nilai dengan format yang sudah ditentukan
    mata_kuliah = str(input("Masukan nama mata kuliah ke-" + str(i) + ": "))
    jumlah_sks = int(input("Masukan jumlah SKS" + " " + mata_kuliah + ": "))
    nilai = float(input("Masukan nilai yang kamu dapatkan: "))

    while nilai < 0: # melakukan pengulangan pertanyaan untuk meninta user memasukan nilai, jika nilai < 0
        print("Nilai yang kamu masukan tidak valid")
        nilai = float(input("Masukan nilai yang kamu dapatkan: "))

# membuat beberapa kondisi untuk setiap nilai yang di input
# LULUS
    if (nilai >= 85):
        total_mutu += (4.0*jumlah_sks) # merubah atau menambahkan jumlah untuk total_mutu
        total_nilai += (4.0*jumlah_sks) # merubah atau menambahkan jumlah untuk total_nilai
        total_sks_lulus += jumlah_sks # menambahakan jumlah sks yang lulus
        total_sks += jumlah_sks  # menambahkan jumlah dari semua sks ada
# untuk setiap kondisi (if) dibawah memiliki konsep yang sama seperti (if) di atas
    elif (80 <= nilai < 85):
        total_mutu += (3.7*jumlah_sks)
        total_nilai += (3.7*jumlah_sks)
        total_sks_lulus += jumlah_sks
        total_sks += jumlah_sks  
            
    elif (75 <= nilai < 80):
        total_mutu += (3.3*jumlah_sks)
        total_nilai += (3.3*jumlah_sks)
        total_sks_lulus += jumlah_sks
        total_sks += jumlah_sks  
        
    elif (70 <= nilai < 75):
        total_mutu += (3.0*jumlah_sks)
        total_nilai += (3.0*jumlah_sks)
        total_sks_lulus += jumlah_sks
        total_sks += jumlah_sks  
            
    elif (65 <= nilai < 70):
        total_mutu += (2.7*jumlah_sks)
        total_nilai += (2.7*jumlah_sks)
        total_sks_lulus += jumlah_sks
        total_sks += jumlah_sks  
        
    elif (60 <= nilai < 65):
        total_mutu += (2.3*jumlah_sks)
        total_nilai += (2.3*jumlah_sks)
        total_sks_lulus += jumlah_sks
        total_sks += jumlah_sks  

    elif (55 <= nilai < 60): 
        total_mutu += (2.0*jumlah_sks)
        total_nilai += (2.0*jumlah_sks)
        total_sks_lulus += jumlah_sks
        total_sks += jumlah_sks
# TIDAK LULUS
    elif (40 <= nilai < 55): 
        total_nilai += (1.0*jumlah_sks)
        total_sks += jumlah_sks  

    elif (0 <= nilai < 40): 
        total_nilai += (0.0*jumlah_sks)
        total_sks += jumlah_sks

# Merumuskan nilai IPK dan IPT
ipk = total_mutu / total_sks_lulus
ipt = total_nilai / total_sks

# menyalin data dan melakukan format string untuk mengatur banyak digit di belakang (.2f) atau dengan presisi 2 digit dibelakang (.)
Total_mutu = f"{total_mutu:.2f}"
Total_nilai = f"{total_nilai:.2f}"
Ipk = f"{ipk:.2f}"
Ipt = f"{ipt:.2f}"




print() # nambah space
# mengeluarkan output yang dibutuhkan
print("Jumlah SKS yang lulus  :", total_sks_lulus, "/" , total_sks)
print("Jumlah mutu yang lulus :",Total_mutu, "/", Total_nilai)
print("Total IPK kamu adalah", Ipk)
print("Total IPT kamu adalah", Ipt)
  


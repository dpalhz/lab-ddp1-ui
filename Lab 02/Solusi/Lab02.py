print("Selamat datang di Kalkulator IPK!")

jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
while (jumlah_matkul < 0):
    print("Nilai yang kamu masukkan tidak valid")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

jumlah_sks_lulus = 0
jumlah_sks_total = 0
jumlah_mutu_lulus = 0
jumlah_mutu_total = 0

for matkul_ke in range(jumlah_matkul):
    nama_matkul = input(f"Masukkan nama mata kuliah ke-{matkul_ke + 1}: ")
    sks_matkul = int(input(f"Masukkan jumlah SKS {nama_matkul}: "))
    
    while True:
        nilai_matkul = float(input("Masukkan nilai yang kamu dapatkan: "))

        if (nilai_matkul >= 0): break
        
        print("Nilai yang kamu masukkan tidak valid")

    print()

    is_lulus = True
    if nilai_matkul >= 85:
        bobot = 4.0
    elif 80 <= nilai_matkul < 85:
        bobot = 3.7
    elif 75 <= nilai_matkul < 80:
        bobot = 3.3
    elif 70 <= nilai_matkul < 75:
        bobot = 3.0
    elif 65 <= nilai_matkul < 70:
        bobot = 2.7
    elif 60 <= nilai_matkul < 65:
        bobot = 2.3
    elif 55 <= nilai_matkul < 60:
        bobot = 2.0
    elif 40 <= nilai_matkul < 55:
        bobot = 1.0
        is_lulus = False
    else:
        bobot = 0.0
        is_lulus = False

    if (is_lulus):
        jumlah_sks_lulus += sks_matkul
        jumlah_mutu_lulus += sks_matkul * bobot

    jumlah_sks_total += sks_matkul
    jumlah_mutu_total += sks_matkul * bobot
    
if (jumlah_matkul == 0):
    print("Tidak ada mata kuliah yang diambil.")
else:
    IPK = 0
    if (jumlah_sks_lulus != 0):
        IPK = jumlah_mutu_lulus / jumlah_sks_lulus
        
    IPT = jumlah_mutu_total / jumlah_sks_total

    print(f"Jumlah SKS lulus: {jumlah_sks_lulus} / {jumlah_sks_total}")
    print(f"Jumlah mutu lulus: {jumlah_mutu_lulus:.2f} / {jumlah_mutu_total:.2f}")
    print(f"Total IPK kamu adalah {IPK:.2f}")
    print(f"Total IPT Kamu adalah {IPT:.2f}")

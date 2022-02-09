MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

# TESTING
MATKUL_TERSEDIA = [
    ["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
    ["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
    ["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
    ["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
    ["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
    ["matdis 1 b",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40]
]
# MATKUL_TERSEDIA = [
# ["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
# ["ddp 1 c", HARI[2] + JAM[8] + 0, HARI[2] +  JAM[9] + 40],
# ["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[1] +  JAM[9] + 40],
# ["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
# ["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
# ["matdis 1 b", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
# ["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
# ]

"""
Merepresentasikan jadwal “ddp 1 a” hari senin 08.00 sampai 09.40, serta hari rabu jam 08.00 sampai 09.40

Jadwal “ddp 1 b” hari selasa jam 08.00 sampai 09.40
Jadwal “manbis” hari senin jam 09.00 sampai 10.40
Jadwal “matdis 1 a” hari rabu jam 09.00 sampai 10.40
Jadwal “matdis 1 b” hari rabu jam 09.00 sampai 10.40
"""

# kode Anda selanjutnya
def mode():
    print('''=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
    ''')
lst1 = [] # penyimpanan data matkul yang dipilih.(LIST UTAMA)

while True:
    mode()
    perintah = input("Masukan pilihan: ") 
# pilih 1    
    if perintah == "1":
        namaMatkul = input('Masukan nama matkul: ')
        data = [] # untuk membantu pemeriksaan list agar (LIST UTAMA) tidak ke reset
        for i in MATKUL_TERSEDIA:   # memeriksa kesesuaian input terhadap element didalam element list(MATKUL_TERSEDIA)
            if namaMatkul in list(i):    
                data.append(list(i))
                lst1.append(list(i))           
        if len(data) == 0: # menghendle jika nama matkul tidak tersedia di list(MATKUL_TERSEDIA) 
            print("Matkul tidak ditemukan")
        print()
# pilih 2
    elif perintah == "2": # tricky remove list
        lst2 = lst1[::] # mengambil element list utama 
        a = len(lst2)
        namaMatkul = input('Masukan nama matkul: ')
        for i in lst1:
            if namaMatkul in list(i):
                lst2.remove(list(i)) # menghapus element
        if len(lst2) == a: # jika tidak ada yang dihapus
            print("Matkul tidak ditemukan")
        lst1.clear() # menghapus seluruh data list utama
        lst1.extend(lst2) # mengisi data list utama baru setelah proses remove element
        print()

# pilih 3
    elif perintah == "3":        
        banyakTabrakan = 0  
        m1 = [] # list untuk menyimpan nama matkul yang bentrok
        m2 = []
        for i in range(len(lst1)-1): # konsep kombinasi dalam mengecek tabrakan waktu Matkul
            lst2 = lst1[i::] # mengambil element pada list Utama
            lst3 = lst1[i+1::] # mengambil elemen+1 pada list utama
            for j in lst2:
                for k in lst3:
                    a,b = j[1], j[2] # mengambil starttime dan endtime
                    c,d = k[1], k[2]
                    if a<=c<=b or a<=d<=b: # kondisi jika terjadi bentrok waktu
                        banyakTabrakan += 1 
                        namaMatkul1 = j[0] # memesihkan nama matkul yang bentrok
                        namaMatkul2 = k[0]
                        m1.append(namaMatkul1) # memasukan nama matkul yang bentrok ke dalam list baru
                        m2.append(namaMatkul2)
                    # print("Check1",a,b)
                    # print("pada check2",c,d)
                break
        if banyakTabrakan == 0:
            print("Tidak ada mata kuliah yang bermasalah")
        elif banyakTabrakan > 0: # jika terjadi bentrok
            for i in range(len(m1)): 
                print("\t",m1[i], "bentrok dengan",m2[i])
        print()
# pilih 4
    elif perintah == "4":
        lst1 = sorted(lst1, key= lambda x:(x[1])) # sorted list dengan lambda , berdasarkan start_time
        print("daftar matkul: ")
        for i in lst1:
            nama = i[0] # mengambil nama matkul
            hari1 = ""
            hari2 = ""
            start = ""
            end = ""
            if i[1] < HARI[1]: # kondisi start_time
                hari1 += "Senin,"
                start += (str(int(i[1]/60)).zfill(2)+"."+ str(int(i[1]%60)).zfill(2)) #.zfill = leading zero(2 angka)
            elif i[1] < HARI[2]:
                hari1 += "Selasa,"
                a = i[1] - HARI[1]
                start += str(int(a/60)).zfill(2)+"." + str(int(i[1]%60)).zfill(2)
            elif i[1] < HARI[3]:
                hari1 += "Rabu,"
                a = i[1] - HARI[2]
                start += str(int(a/60)).zfill(2)+"." + str(int(i[1]%60)).zfill(2)               
            elif i[1] < HARI[4]:
                a = i[1] - HARI[3]
                start += str(int(a/60)).zfill(2)+"." + str(int(i[1]%60)).zfill(2)
            elif i[1] < HARI[5]:
                hari1 += "Jumat,"  
                a = i[1] - HARI[4]
                start += str(int(a/60)).zfill(2)+"." + str(int(i[1]%60)).zfill(2)
            elif i[1] < HARI[6]:
                hari1 += "Sabtu,"
                a = i[1] - HARI[5]
                start += str(int(a/60)).zfill(2)+"." + str(int(i[1]%60)).zfill(2)
            elif i[1] < (HARI[6]+HARI[1]):
                hari1 += "Minggu,"
                a = i[1] - HARI[6]
                start += str(int(a/60)).zfill(2)+"." + str(int(i[1]%60)).zfill(2)

            if i[2] < HARI[1]: # kondisi end_time
                hari2 += "Senin,"
                end += (str(int(i[2]/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2))#.zfill = leading zero(2 angka)
            elif i[2] < HARI[2]:
                hari2 += "Selasa,"
                b = i[2] - HARI[1]
                end += str(int(b/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2)
            elif i[2] < HARI[3]:
                hari2 += "Rabu,"
                b = i[2] - HARI[2]
                end += str(int(b/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2)               
            elif i[2] < HARI[4]:
                b = i[2] - HARI[3]
                end += str(int(b/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2)
            elif i[2] < HARI[5]:
                hari2 += "Jumat,"  
                b = i[2] - HARI[4]
                end += str(int(b/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2)
            elif i[2] < HARI[6]:
                hari2 += "Sabtu,"
                b = i[2] - HARI[5]
                end += str(int(b/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2)
            elif i[2] < (HARI[6]+HARI[1]):
                hari2 += "Minggu,"
                b = i[2] - HARI[6]
                end += str(int(b/60)).zfill(2)+"." + str(int(i[2]%60)).zfill(2)
                              
            matkul = "{:<14}{:<8}{:^6} s/d {:<8}{:^6}".format(nama.upper(),hari1,start,hari2,end) # formatting jadwal yang dipilih
            print("\t",matkul)
        print()
# pilih 5
    elif perintah == "5": # KELUAR PROGRAM
        print("Terima kasih!")
        exit()
    else: # handle salah input
        print("Maaf, pilihan tidak tersedia")
        print()
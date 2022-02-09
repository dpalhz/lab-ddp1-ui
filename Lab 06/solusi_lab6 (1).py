MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] + JAM[9] + 40],
["ddp 1 a", HARI[2] + JAM[8] + 0, HARI[2] + JAM[9] + 40],
["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[1] + JAM[9] + 40],
["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["matdis 1 b", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40]
]

DAFTAR_HARI = [
    'Senin',
    'Selasa',
    'Rabu',
    'Kamis',
    'Jumat',
    'Sabtu',
    'Minggu'
]

daftar_perintah = '''
=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
'''

jadwalku = []

def add_matkul(matkul):
    jadwal_matkul_diambil = [detail_matkul for detail_matkul in MATKUL_TERSEDIA if detail_matkul[0].lower() == matkul.lower()]

    if (len(jadwal_matkul_diambil) > 0):
        jadwalku.extend(jadwal_matkul_diambil)
        return
    
    print("Matkul tidak ditemukan")

def drop_matkul(matkul):
    jadwal_matkul_dibuang = [detail_matkul for detail_matkul in jadwalku if detail_matkul[0].lower() == matkul.lower()]
    jumlah_matkul_dibuang = len(jadwal_matkul_dibuang)

    if (jumlah_matkul_dibuang > 0):
        for idx in range(jumlah_matkul_dibuang):
            jadwalku.remove(jadwal_matkul_dibuang[idx])
        return
    
    print("Matkul tidak ditemukan")

def cek_ringkasan():
    bentrok = False
    for i in range(len(jadwalku)):
        for j in range(i+1, len(jadwalku)):
            kriteria_1_bentrok = jadwalku[i][1] <= jadwalku[j][1] < jadwalku[i][2]
            kriteria_2_bentrok = jadwalku[i][1] < jadwalku[j][2] <= jadwalku[i][2]
            kriteria_3_bentrok = jadwalku [j][1] < jadwalku[i][1] < jadwalku[i][2] < jadwalku[j][2]

            if (kriteria_1_bentrok or kriteria_2_bentrok or kriteria_3_bentrok):
                print(f"{jadwalku[i][0]} bentrok dengan {jadwalku[j][0]}")
                bentrok = True

    if (not bentrok):
        print("Tidak ada masalah")
    

def lihat_daftar_matkul():
    if (len(jadwalku) == 0):
        print("Tidak ada matkul yang diambil")
    else:
        jadwalku.sort(key=lambda jadwal: jadwal[1])

        for jadwal in jadwalku:
            matkul = jadwal[0]
            waktu_mulai = jadwal[1]
            waktu_selesai = jadwal[2]

            hari_mulai = DAFTAR_HARI[waktu_mulai // MENIT_DALAM_HARI]
            jam_mulai = (waktu_mulai % MENIT_DALAM_HARI) // MENIT_DALAM_JAM
            menit_mulai = (waktu_mulai % MENIT_DALAM_HARI) % MENIT_DALAM_JAM

            hari_selesai = DAFTAR_HARI[waktu_selesai // MENIT_DALAM_HARI]
            jam_selesai = (waktu_selesai % MENIT_DALAM_HARI) // MENIT_DALAM_JAM
            menit_selesai = (waktu_selesai % MENIT_DALAM_HARI) % MENIT_DALAM_JAM

            print(f"{matkul:20s}{hari_mulai:10s}{jam_mulai:02d}:{menit_mulai:02d} s/d {hari_selesai:10s}{jam_selesai:02d}:{menit_selesai:02d}")


def main():
    while (True):
        print(daftar_perintah)

        try:
            pilihan = int(input("Masukkan pilihan (dalam angka): ").strip())
            if (pilihan == 1):
                matkul = input("Masukkan nama matkul: ").strip()
                add_matkul(matkul)
            elif (pilihan == 2):
                matkul = input("Masukkan nama matkul: ").strip()
                drop_matkul(matkul)
            elif (pilihan == 3):
                cek_ringkasan()
            elif (pilihan == 4):
                lihat_daftar_matkul()
            elif (pilihan == 5):
                print("Terima kasih!")
                break
            else:
                print("Nomor perintah tidak tersedia")

        except ValueError:
            print("input tidak valid")

if __name__ == "__main__":
    main()
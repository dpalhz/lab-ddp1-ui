PROMPT = "Selamat datang! Silahkan masukkan jadwal KA:"

CMD_PROMPT = """Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT"""

def get_jadwal():
    jadwal = list()
    while True:
        str_input = input()
        if str_input.lower() == "selesai":
            break
        else:
            jadwal.append(dict(zip(["nomor_ka", "tujuan_akhir",
                                    "jam_keberangkatan", "harga_tiket"],
                                   str_input.split())))
    return jadwal

def info_tujuan(jadwal):
    result = set(row["tujuan_akhir"] for row in jadwal)

    if len(result) == 0:
        return "Tidak ada jadwal KA yang sesuai"
    else:
        return "\n".join(["KA di stasiun ini memiliki tujuan akhir:"]
                         + list(result))

def do_tujuan_kelas(tujuan_akhir, kelas_kereta, jadwal):
    kelas_map = {'1': 'Eksekutif', '2':'Bisnis', '3':'Ekonomi'}
    return [row for row in jadwal if row['tujuan_akhir'] == tujuan_akhir and
            kelas_map[row['nomor_ka'][0]] == kelas_kereta]

def tujuan_kelas(tujuan_akhir, kelas_kereta, jadwal):
    result = do_tujuan_kelas(tujuan_akhir, kelas_kereta, jadwal)
    if len(result) == 0:
        return "Tidak ada jadwal KA yang sesuai"
    else:
        return "\n".join([f"KA {row['nomor_ka']} berangkat pukul {row['jam_keberangkatan']} dengan harga tiket {row['harga_tiket']}" for row in result])

def tujuan_kelas_termurah(tujuan_akhir, kelas_kereta, jadwal):
    result = do_tujuan_kelas(tujuan_akhir, kelas_kereta, jadwal)
    if len(result) == 0:
        return "Tidak ada jadwal KA yang sesuai"
    else:
        result = min(result, key=lambda row:row["harga_tiket"])
        return f"KA {result['nomor_ka']} berangkat pukul {result['jam_keberangkatan']} dengan harga tiket {result['harga_tiket']}"

def do_tujuan_jam(tujuan_akhir, jam_keberangkatan, jadwal):
    return [row for row in jadwal
            if int(row['jam_keberangkatan']) <= int(jam_keberangkatan)
            and row['tujuan_akhir'] == tujuan_akhir]

def tujuan_jam(tujuan_akhir, jam_keberangkatan, jadwal):
    result = do_tujuan_jam(tujuan_akhir, jam_keberangkatan, jadwal)
    if len(result) == 0:
        return "Tidak ada jadwal KA yang sesuai"
    else:
        return "\n".join([f"KA {row['nomor_ka']} berangkat pukul {row['jam_keberangkatan']} dengan harga tiket {row['harga_tiket']}" for row in result])

def tujuan_jam_termurah(tujuan_akhir, jam_keberangkatan, jadwal):
    result = do_tujuan_jam(tujuan_akhir, jam_keberangkatan, jadwal)
    if len(result) == 0:
        return "Tidak ada jadwal KA yang sesuai"
    else:
        result = min(result, key=lambda row:row["harga_tiket"])
        return f"KA {result['nomor_ka']} berangkat pukul {result['jam_keberangkatan']} dengan harga tiket {result['harga_tiket']}"

def exec_query(raw_str, jadwal):
    is_done = False
    message = ""
    
    command = raw_str.split()
    if command[0] == "EXIT":
        is_done = True
        message = "Terima kasih sudah menggunakan program ini!"
    elif command[0] == "INFO_TUJUAN":
        message = info_tujuan(jadwal)
    elif command[0] == "TUJUAN_KELAS":
        message = tujuan_kelas(command[1], command[2], jadwal)
    elif command[0] == "TUJUAN_KELAS_TERMURAH":
        message = tujuan_kelas_termurah(command[1], command[2], jadwal)
    elif command[0] == "TUJUAN_JAM":
        message = tujuan_jam(command[1], command[2], jadwal)
    elif command[0] == "TUJUAN_JAM_TERMURAH":
        message = tujuan_jam_termurah(command[1], command[2], jadwal)
    else:
        message = "Perintah yang dimasukkan tidak valid"
    return is_done, message

def main():
    print(PROMPT)
    jadwal = get_jadwal()
    print(CMD_PROMPT)
    while True:
        is_done, message = exec_query(input("Masukkan perintah: "), jadwal)
        print(message)
        if is_done:
            break

if __name__ == "__main__":
    main()

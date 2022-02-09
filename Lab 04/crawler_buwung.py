# Meminta user meninput sesuatu
file_input = input("Masukan nama file input : ")
file_output = input("Masukan nama file output : ")


try: # try dan except di gunakan untuk menghandle Error , untuk khasus ini untuk text yang tidak ada ataupun Error lainnya
    myFile = open(file_input, "r") # Membuka file dan membaca
    
        
    if myFile.read() == "": # kondisi jika read pada text kosong
        print("File input ada, tetapi kosong")
        myFile.close()
        
           
    else :
        myFile = open(file_input, "r") # Konsepnya sama seperti sebelumnya
        output = open(file_output, "w") # membuka atau membuat (write) text dalam file (Memperbarui isi setiap di isi)
        # inisialisasi variabel untuk menyimpan nilai
        Hesteg = 0
        Mention = 0
        Url = 0
        
        for line in myFile:
            new_line = ''
            line = line.split() # merubah setiap line menjadi list

    
            for x in list(line): # Mengecek isi list setiap line 
        
                if "@" in x: # kondisi jika ada "@", dan mengganti nilai tersebut
                    Mention += 1
                    x = "[M]"
                    new_line += (x + ' ') 
            
            
                elif "#" in x: # kondisi jika ada "#", dan mengganti nilai tersebut
                    Hesteg += 1
                    x = "[H]"
                    new_line += (x + ' ') 

            
                elif "www." in x: # kondisi jika ada "www." , dan mengganti nilai tersebut
                    Url += 1
                    x = "[U]"  
                    new_line += (x + ' ')          
                else:
                    new_line += (x + ' ')

        
            print(new_line, file = output) # Memasukan perubahan text ke file baru setiap linenya
                                    
        
        # Menggunakan aturan formatting untuk merapikan tampilan
        a = "{:<8}:{!s:>5}".format("Mention",Mention) # rata kiri & rata kanan
        b = "{:<8}:{!s:>5}".format("Hesteg",Hesteg)
        c = "{:<8}:{!s:>5}".format("Url",Url)
        d = "#" * len(a)
        # memasukan data ke dalam file baru (data output ke sebuah .txt)
        print(" ", file = output)
        print(d, file = output)
        print(a, file = output)
        print(b, file = output)
        print(c, file = output)

        print("Output berhasil ditulis pada", file_output)
        # memnutup text file
        myFile.close()
        output.close()
except:
    print("File tidak dapat ditemukan")        


finally: # selalu muncul setiap program dijalankan
    input("Program selesai. Tekan enter untuk keluar..." )# usur akan keluar program setelah menekan enter
    exit()

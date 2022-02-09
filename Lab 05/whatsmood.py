file_in = input("Masukan nama file input: ")
# file_in = "Percakapan1.txt"
# menginisialisasi variabel
poinSmile = 50
poinSad = 50
poinAngry = 50
def koreksi():  # fungsi untuk koreksi minimal daa maksimal poin
    global poinSmile, poinSad, poinAngry # global = keyword untuk dapat me-modify variabel diluar 
    if poinSmile > 100:
        poinSmile = 100
    elif poinSmile < 0:
        poinSmile = 0
    if poinAngry > 100:
        poinAngry = 100
    elif poinAngry < 0:
        poinAngry = 0
    if poinSad > 100:
        poinSad = 100
    elif poinSad < 0:
        poinSad = 0
    
# fungsi untuk merubah poin smile, sad, dan angry
def smile():
    global poinSmile, poinSad, poinAngry
    poinSmile += 9
    poinSad -= 6         
def sad():
    global poinSmile, poinSad, poinAngry 
    poinSad += 10
    poinAngry -= 8   
def angry():
    global poinSmile, poinSad, poinAngry
    poinAngry += 13
    poinSmile -= 5

    

try: # try dan except di gunakan untuk menghandle Error , untuk khasus ini untuk text yang tidak ada ataupun Error lainnya
    fileInput = open(file_in, "r") # Membuka file dan membaca
    
        
    if fileInput.read() == "": # kondisi jika read pada text kosong
        print("File input ada, tetapi kosong")
        fileInput.close()
        exit() # program keluar (berhenti)
    else:
        fileInput = open(file_in, "r")
        
        for line in fileInput:
            new_line = ''
            line = line.split() # merubah setiap line menjadi list
            if "Chanek:" in line: # kondisi jika pak chenek mengirim pesan
                for x in list(line): # Mengecek isi list setiap line                                                 
                    if "(smile)" in x: # kondisi jika ada "(smile)"", dan mengganti nilai tersebut
                        x = "\U0001f603"
                        new_line += (x + ' ') 
                        smile()           
                    elif "(sad)" in x: # kondisi jika ada "(sad)", dan mengganti nilai tersebut
                        x = "\U0001f622"
                        new_line += (x + ' ') 
                        sad()            
                    elif "(angry)" in x: # kondisi jika ada "(angry)" , dan mengganti nilai tersebut
                        x = "\U0001f621"
                        new_line += (x + ' ')
                        angry()          
                    else:
                        new_line += (x + ' ')
            else:
                for x in list(line):
                    if "(smile)" in x: # kondisi jika ada "(smile)"", dan mengganti nilai tersebut
                        x = "\U0001f603"
                        new_line += (x + ' ')             
                    elif "(sad)" in x: # kondisi jika ada "(sad)", dan mengganti nilai tersebut
                        x = "\U0001f622"
                        new_line += (x + ' ')             
                    elif "(angry)" in x: # kondisi jika ada "(angry)" , dan mengganti nilai tersebut
                        x = "\U0001f621"
                        new_line += (x + ' ')                                  
                    else:
                        new_line += (x + ' ') # memasukan data x ke new_line

        
            print(new_line)
        fileInput.close() # menutup file
except FileNotFoundError: # kondisi file tidak ada
    print("File input tidak ada")
    exit() # keluar program


print()
print("Mengukur suasana hati....")
print()
print("#"*5,"Hasil Pengukuran","#"*5)
koreksi() # koreksi nilai minimal dan maksimal
hasil = "Happiness = {} | Sadness = {} | Anger = {}".format(poinSmile,poinSad,poinAngry) 
print(hasil)
print("#"*5,"Kesimpulan","#"*5)
# kondisi perasaan pak Chanek
if poinSmile > poinAngry and poinSmile > poinSad:
    print("Pak Chanek sedang bahagia")
elif poinSad > poinSmile and poinSad > poinAngry:
    print("Pak chanek sedang sedih")
elif poinAngry > poinSmile and poinAngry > poinSad:
    print("Pak Chanek sedang marah")
elif poinSmile == poinAngry == poinSad:
    print("Kesimpulan tidak ditemukan")
elif poinSmile == poinAngry and poinSmile > poinSad:
    print("Pak Chanek sedang bahagia atau marah")
elif poinSmile == poinSad and poinSmile > poinAngry:
    print("Pak Chanek sedang bahagia atau sedih")
elif poinSad == poinAngry and poinSad > poinSmile:
    print("Pak Chanet sedang sedih atau marah")
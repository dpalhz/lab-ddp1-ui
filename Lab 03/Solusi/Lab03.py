import string # membuka module string in python
# Meminta user memasukan input
a = input("Masukan input Himpunan A: ")
b = input("Masukan input Himpinan B: ")
# a = 'a,2,3'
# b = 'c,e,3'
print("A x B =")
start_a = 0
end_a = a.find(',',0) # mengoreksi  ada ","

# count(","+1) untuk menghitung jumlah elemen setiap himpunan
for i in range(a.count(",")+1): # for loop untuk memisahkan huruf pada himpunan a
    if end_a == -1: # untuk kondisi himpunan a akhir tidak ada ","
        c = (a[start_a:])
            
    else:
        mulai = 0
        akhir = b.find(',', 0)
        for j in range (b.count(",")+1):

            if akhir == -1:
                break
                
            else:
                print("(" +a[start_a:end_a]+","+b[mulai:akhir]+")", end= ",") # membuat himpunan a mengambil setiap himpunan b
                
            mulai = akhir + 1 # mengoreksi huruf selanjutnya
            akhir = b.find(',', mulai)
            continue
        
        elemen_a = a [start_a:end_a]

    start_a = end_a +1 #    Melanjutkan koreksi di angka selanjutnya
    end_a = a.find(',', start_a) # melihat apakah ada ","


   
          
                 
            
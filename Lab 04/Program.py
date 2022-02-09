lst = [[],[]]
for i in range(0, len(lst), 4):
    soal = "{:<10} {:<10} {:<10} {:<10}".format(lst[i], lst[i+1],lst[i+2],lst[i+3])
    print(soal)


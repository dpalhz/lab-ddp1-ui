

Hesteg = 0
Mention = 0
Url = 0
file = input(" :")

# with open(file) as myInput:
#     my_file = myInput.readlines()
my_file = open(file, "r")

# x = my_file.readline().split()

for line in my_file:
    new_line = ''
    line = line.split()
    
    for x in list(line):
        
        if "@" in x:
            Mention += 1
            x = "[M]"
            new_line += (x + ' ') 
            
            
        elif "#" in x:
            Hesteg += 1
            x = "[R]"
            new_line += (x + ' ') 

            
        elif "www." in x:
            Url += 1
            x = "[J]"  
            new_line += (x + ' ')          
        else:
            new_line += (x + ' ')
    print(new_line)   
        

print(Hesteg)
print(Mention)  
print(Url)     
 
#         
# print(x)

# for i in list(x):
#     if "@" == i:
#         i = i.replace("[M]")
    

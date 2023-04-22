handle = open('file1.txt','r')
handle1 = open('file2.txt','r')

baris = handle.readline()
baris2 = handle1.readline()
# Cara 1 
while baris != '' and baris2 !='':
    if baris == baris2:
        print(f'{baris.strip()} sama dengan {baris2.strip()}')
    else:
        print(f'{baris.strip()} beda dengan {baris2.strip()} ')
    baris = handle.readline()
    baris2 = handle1.readline()    
# Cara 2
for baris in handle:
    baris2 = handle1.readline()
    if baris.strip() == baris2.strip():
        print(f'{baris.strip()} sama dengan {baris2.strip()}')    
    else:
        print(F'{baris.strip()} beda dengan {baris2.strip()}')

#Cara 3
baris1 = handle.readlines()
baris2 = handle1.readlines()
c=0
for a in baris1:
    b=baris2[c]
    if a==b:
        print('sama')
    else:
        print('beda')
    c=c+1


handle.close()
handle1.close()

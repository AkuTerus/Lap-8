handle = open('soal.txt','r')
for line in handle:
    line = line.lower()
    line = line.split('||')
    line1 = line[0].strip()
    line2 = line[1].strip()
    jawaban = input('Jawaban : ').lower()
    if jawaban == line2:
        print('Benar')
    else:
        print('Salah')

handle.close()






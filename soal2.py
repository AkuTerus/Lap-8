handle = open('soal.txt','r')   
for i in handle:
    i = i.lower()
    i = i.split('||')
    line1 = i[0].strip()
    line2 = i[1].strip()
    soal = str(line1)
    print(soal)
    jawaban = input('Jawaban : ').lower()
    if jawaban == line2:
        print('Jawaban Benar !')
    else:
        print('Jawaban Salah !')
handle.close()

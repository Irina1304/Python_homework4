#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
#содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

ffile1 = open('file5.1.txt', 'r')
ffile2 = open('file5.2.txt', 'r')
ffile3 = open('file5.3.txt', 'w')
file1 = ffile1.readline()
file2 = ffile2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            ffile3.write(str(int(file1[i])+int(file2[i])))
        else:
            ffile3.write(str(file1[i]))
    else:
        ffile3.write(str(file1[i]))
ffile1.close
ffile2.close
ffile3.close
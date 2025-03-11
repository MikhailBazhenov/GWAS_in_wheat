# This program converts diploid hmp file with SNP data from TASSEL in a format suitable for STRUCTURE

filename = 'Genotypes_for_structure.hmp.txt'

f1 = open(filename, 'r')  # открываем файл
f2 = open(filename.split('.')[0] + '.str.txt', 'w')  # создаем файл для вывода данных

rows = []  # это массив строк исходной таблицы
for line in f1:
    rows.append(line.strip())  # добавляем строки из исходного файла

cells = rows[0].split('\t')  # разбиваем первую строку из файла по знакам табуляции на ячейки
L = len(cells)  # длина строки данных (число столбцов в исходной таблице)
cells_new = []  # создаем пустой массив строк новой перевернутой таблицы

for i in range(L):
    cells_new.append('')  # создаем пустые строки новой таблицы по числу столбцов в исходной

for i in range(len(rows)):  # проходимся по строкам исходной таблицы
    cells = rows[i].split('\t')  # разбваем строки исходной таблицы на ячейки
    for j in range(L):
        cells_new[j] = cells_new[j] + '\t' + cells[j]  # добавляем ячейки в столбцы новой таблицы

#for i in range(12):
#    print(cells_new[i])

#exit(0)
for i in range(L):
    if i == 2:
        ref = cells_new[i].split('\t')
    if i == 3:
        pos = cells_new[i].split('\t')
        for j in range(len(pos)):
            if j == 0:
                continue
            if j == 1:
                pos[j] = 'Distance'
                continue
            if j == 2:
                prev = int(pos[j].replace(' ',''))
                pos[j] = '-9'
                continue
            if j > 2:
                pos_ws = pos[j].replace(' ','')
                posi = int(pos_ws)
                pos[j] = str(posi - prev)
                prev = posi
                if ref[j] != ref[j-1]:
                    pos[j] = '-9'
        for j in range(len(pos)):
            if j == 2:
                out = pos[j]
            if j > 2:
                out = out + '\t'+ pos[j]
        Distance = out
        continue
    if i == 0:
        Ids = ''
        Idsi = cells_new[i].split('\t')
        for j in range(len(Idsi)):
            if j == 0:
                continue
            if j == 1:
                continue
            if j == 2:
                Ids = Idsi[j]
            if j > 2:
                Ids = Ids + '\t' + Idsi[j]
        continue
    if i == 3:
        continue
    if i == 10:
        print(Ids)
        print(Distance)
        f2.write(Ids + '\n')
        f2.write(Distance + '\n')
        continue
    if i > 10:
        sample = cells_new[i].split('\t')
        for j in range(len(sample)):
            if j == 0:
                continue
            if j == 1:
                out1 = sample[j]
                out2 = sample[j]
                continue
            if j > 1:
                dot = sample[j]
                if dot[0] == 'A':
                    out1 = out1 + '\t' + '1'
                if dot[0] == 'T':
                    out1 = out1 + '\t' + '2'
                if dot[0] == 'G':
                    out1 = out1 + '\t' + '3'
                if dot[0] == 'C':
                    out1 = out1 + '\t' + '4'
                if dot[0] == 'N':
                    out1 = out1 + '\t' + '-9'
                if dot[1] == 'A':
                    out2 = out2 + '\t' + '1'
                if dot[1] == 'T':
                    out2 = out2 + '\t' + '2'
                if dot[1] == 'G':
                    out2 = out2 + '\t' + '3'
                if dot[1] == 'C':
                    out2 = out2 + '\t' + '4'
                if dot[1] == 'N':
                    out2 = out2 + '\t' + '-9'
        print(out1)
        print(out2)
        f2.write(out1 + '\n')
        f2.write(out2 + '\n')
print('No of samples = ' + str(L-11))
print('No of markers = ' + str(len(Idsi)-2))

f1.close()
f2.close()

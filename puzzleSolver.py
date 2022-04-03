from copy import deepcopy


def printPuzzle(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == 16):
                print("   -", end=" ")
            else:
                print('{:4}'.format(matrix[i][j]), end=" ")
        print()


def posisiKurang(matrix, bilPertama, bilKedua):
    barisBilPertama, kolomBilPertama = posisi(matrix, bilPertama)
    barisBilKedua, kolomBilKedua = posisi(matrix, bilKedua)
    return barisBilPertama*4+kolomBilPertama < barisBilKedua*4+kolomBilKedua


def posisi(matrix, x):
    i = 0
    while(i < 4):
        j = 0
        while(j < 4):
            if(matrix[i][j] == x):
                return i, j
            j += 1
        i += 1


def posisiSelKosong(matrix):
    i, j = posisi(matrix, 16)
    if((i+j) % 2 == 0):
        return 0
    else:
        return 1


def Kurang(matrix, x):
    count = 0
    for i in range(4):
        for j in range(4):
            if((matrix[i][j] < x) and posisiKurang(matrix, x, matrix[i][j])):
                count += 1
    return count


def sigmaKurang(matrix):
    count = 0
    for i in range(4):
        for j in range(4):
            count += Kurang(matrix, matrix[i][j])
    return count


def puzzleCanBeSolve(matrix, total):
    return total % 2 == 0


def ubinSalahPosisi(matrix):
    count = 0
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != i*4+j+1 and matrix[i][j] != 16):
                count += 1
    return count


def pindahUbin(matrix, posisiBaris, posisiKolom, arahVertikal, arahHorizontal):
    temp = matrix[posisiBaris][posisiKolom]
    matrix[posisiBaris][posisiKolom] = matrix[posisiBaris +
                                              arahVertikal][posisiKolom + arahHorizontal]
    matrix[posisiBaris + arahVertikal][posisiKolom + arahHorizontal] = temp


def pindahkanSlotKosong(matriks, arah):
    matrix = deepcopy(matriks)
    barisSelKosong, kolomSelKosong = posisi(matrix, 16)
    if(arah == 0):  # Up
        if(barisSelKosong != 0):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, -1, 0)
    elif(arah == 1):  # Right
        if(kolomSelKosong != 3):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, 0, 1)
    elif(arah == 2):  # Down
        if(barisSelKosong != 3):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, 1, 0)
    elif(arah == 3):  # Left
        if(kolomSelKosong != 0):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, 0, -1)
    return matrix


def insert(list, listSimpul, prio, arah, kedalaman, matrix, id, idparent):
    list.append((prio, arah, kedalaman, matrix, id, idparent))
    listSimpul.append((id, idparent, matrix))
    list.sort(key=lambda i: i[0])


def delete(list):
    return list.pop(0)


def isGoal(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != i*4+j+1):
                return False
    return True


def deleteLowerPrio(list, prio):
    for i in list:
        if (i[0] < prio):
            list.remove(i)


def findId(listSimpul, id):
    for i in range(len(listSimpul)):
        if (listSimpul[i][0] == id):
            return listSimpul[i]


def findLangkah(listSimpul, id):
    listLangkah = []
    while(id != 1):
        temp = findId(listSimpul, id)
        listLangkah.insert(0, temp[2])
        id = temp[1]
    return listLangkah

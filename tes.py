from audioop import reverse
from queue import PriorityQueue

from numpy import matrix


def printPuzzle(matrix):
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=" ")
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


def puzzleCanBeSolve(matrix):
    return (posisiSelKosong(matrix) + sigmaKurang(matrix)) % 2 == 0


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


def pindahkanSlotKosong(matrix, arah):
    barisSelKosong, kolomSelKosong = posisi(matrix, 16)
    if(arah == 1):  # Up
        if(barisSelKosong != 0):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, 1, 0)
    elif(arah == 2):  # Right
        if(kolomSelKosong != 3):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, 0, 1)
    elif(arah == 3):  # Down
        if(barisSelKosong != 3):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, -1, 0)
    elif(arah == 4):  # Left
        if(kolomSelKosong != 0):
            pindahUbin(matrix, barisSelKosong, kolomSelKosong, 0, -1)


def insert(list, prio, matrix):
    list.append((prio, matrix))
    list.sort(reverse=True)


    #######################
    #     MAIN            #
    #######################
puzzle = [[0 for j in range(4)] for i in range(4)]
print("Masukkan elemen puzzle: ")
for i in range(4):
    for j in range(4):
        puzzle[i][j] = int(input("Masukkan elemen ke-" + str(i*4+j) + ": "))

print()
print("Puzzle: ")
for i in range(4):
    for j in range(4):
        print(puzzle[i][j], end=" ")
    print()
print()

print(sigmaKurang(puzzle))

if(puzzleCanBeSolve(puzzle)):
    print("Puzzle bisa diselesaikan")
else:
    print("Puzzle tidak bisa diselesaikan")

pindahkanSlotKosong(puzzle, 2)
printPuzzle(puzzle)

list = []
insert(list, 4, "ASU")
insert(list, 5, "KAMBINg")
insert(list, 1, "ANJING")

print(list[0][1])

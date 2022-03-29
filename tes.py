from queue import PriorityQueue

from numpy import matrix


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


def pindahkanSlotKosong(matrix, arah):

    if(arah == 1):  # Up
        print()


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

prioQueue = PriorityQueue()

import time
from puzzleSolver import *

# Proses inisiasi puzzle
puzzle = [[0 for j in range(4)] for i in range(4)]
fileName = input("\nMasukkan nama file: ")
file = open(fileName, "r")

for i in range(4):
    f = file.readline().split()
    for j in range(4):
        puzzle[i][j] = int(f[j])
print("Puzzle: ")
printPuzzle(puzzle)
print()

start = time.time()
# Penghitungan dan Pencetakan nilai Kurang(i)
for i in range(1, 17):
    print("Kurang(" + str(i) + ") = " + str(Kurang(puzzle, i)))

totalValue = sigmaKurang(puzzle) + posisiSelKosong(puzzle)
print("\nSigmaKurang + X = " + str(totalValue))

if(puzzleCanBeSolve(puzzle, totalValue)):
    print("Puzzle bisa diselesaikan")

    prioQueue = []
    listSimpul = []
    simpulChecked = 1
    found = False
    insert(prioQueue, listSimpul, 0, 0, 0, puzzle, 1, 0)
    while(len(prioQueue) != 0 and not found):
        simpul = delete(prioQueue)
        # simpul struct:
        # 1. prio
        # 2. arah
        # 3. depth
        # 4. matrix
        # 5. id
        # 6. parentid
        for i in range(4):
            if((i+2) % 4 == simpul[1] and simpul[2] != 0):
                continue
            puzzleMove = pindahkanSlotKosong(simpul[3], i)
            if(puzzleMove == simpul[3]):
                continue
            print(simpulChecked)
            simpulChecked += 1
            if(isGoal(puzzleMove)):
                listSimpul.append((simpulChecked, simpul[4], puzzleMove))
                prio = simpul[2]+1 + ubinSalahPosisi(puzzleMove)
                deleteLowerPrio(prioQueue, prio)
                found = True
                break
            else:
                insert(prioQueue, listSimpul, simpul[2]+1+ubinSalahPosisi(
                    puzzleMove), i, simpul[2]+1, puzzleMove, simpulChecked, simpul[4])
    end = time.time()
    idGoal = simpulChecked
    iter = 1
    listLangkah = findLangkah(listSimpul, idGoal)
    for i in listLangkah:
        print("Langkah ke-" + str(iter))
        printPuzzle(i)
        print()
        iter += 1

    print("Jumlah simpul yang dibangkitkan: " +
          str(simpulChecked))
    print(f"Runtime of the program is {end - start}")
else:
    print("Puzzle tidak bisa diselesaikan")
print()

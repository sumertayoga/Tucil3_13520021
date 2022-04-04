import heapq
import time
from puzzleSolver import *
import random

masukanTidakSesuai = True
while(masukanTidakSesuai):
    print("Pilih cara membentuk puzzle")
    print("1. Random")
    print("2. Baca File")
    pilihan = int(input("Ketik pilihan (1/2): "))
    puzzle = [[0 for j in range(4)] for i in range(4)]
    if(pilihan == 1):
        randomList = random.sample(range(1, 17), 16)
        fillPuzzleFromList(puzzle, randomList)
        outputFile = open("output.txt", "w")
        masukanTidakSesuai = False
    elif(pilihan == 2):
        fileName = input("\nMasukkan nama file: ")
        file = open("./test/" + fileName, "r")
        outputFile = open("./test/output.txt", "w")
        for i in range(4):
            f = file.readline().split()
            for j in range(4):
                puzzle[i][j] = int(f[j])
        file.close()
        masukanTidakSesuai = False
    else:
        print("Masukan tidak sesuai. Ulangi!")

print("Puzzle: ")
outputFile.write("Puzzle: \n")
printPuzzle(puzzle, outputFile)
print()
outputFile.write("\n")

start = time.time()
# Penghitungan dan Pencetakan nilai Kurang(i)
for i in range(1, 17):
    print("Kurang(" + str(i) + ") = " + str(Kurang(puzzle, i)))
    outputFile.write("Kurang(" + str(i) + ") = " + str(Kurang(puzzle, i)))
    outputFile.write("\n")

totalValue = sigmaKurang(puzzle) + posisiSelKosong(puzzle)
print("\nSigmaKurang + X = " + str(totalValue))
outputFile.write("\nSigmaKurang + X = " + str(totalValue) + "\n")

if(puzzleCanBeSolve(puzzle, totalValue)):
    print("Puzzle bisa diselesaikan")
    outputFile.write("Puzzle bisa diselesaikan\n")

    prioQueue = []
    listSimpul = []
    simpulChecked = 1
    found = False
    heapq.heappush(prioQueue, (0, 0, 0, puzzle, 1, 0))
    while(len(prioQueue) != 0 and not found):
        simpul = heapq.heappop(prioQueue)
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
            # print(simpulChecked)
            simpulChecked += 1
            if(isGoal(puzzleMove)):
                listSimpul.append((simpulChecked, simpul[4], puzzleMove))
                prio = simpul[2]+1 + ubinSalahPosisi(puzzleMove)
                found = True
                break
            else:
                heapq.heappush(prioQueue, (simpul[2]+1+ubinSalahPosisi(
                    puzzleMove), i, simpul[2]+1, puzzleMove, simpulChecked, simpul[4]))
                listSimpul.append((simpulChecked, simpul[4], puzzleMove))
    end = time.time()
    idGoal = simpulChecked
    iter = 1
    listLangkah = findLangkah(listSimpul, idGoal)
    for i in listLangkah:
        print("Langkah ke-" + str(iter))
        outputFile.write("Langkah ke-" + str(iter) + "\n")
        printPuzzle(i, outputFile)
        print()
        outputFile.write("\n")
        iter += 1

    print("Jumlah simpul yang dibangkitkan: " +
          str(simpulChecked))
    print(f"Runtime of the program is {end - start}")
    outputFile.write("Jumlah simpul yang dibangkitkan: " +
                     str(simpulChecked) + "\n")
    outputFile.write(f"Runtime of the program is {end - start}")
else:
    print("Puzzle tidak bisa diselesaikan")
    outputFile.write("Puzzle tidak bisa diselesaikan ")
outputFile.close()

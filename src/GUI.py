import heapq
import tkinter
import time
import random
from turtle import width
from puzzleSolver import *


def startSolver():
    outputFile = open("../test/output.txt", "w")
    outputFile.write("Puzzle: \n")
    printPuzzle(puzzle, outputFile)

    start = time.time()
    listKurangLabel = []
    for i in range(0, 8):
        listKurangLabel.append(tkinter.Label(
            root, text="Kurang(" + str(i*2+1) + ") = " + str(Kurang(puzzle, i*2+1))))
        listKurangLabel[i*2].place(x=300, y=24+(i)*20)
        listKurangLabel.append(tkinter.Label(
            root, text="Kurang(" + str(i*2+2) + ") = " + str(Kurang(puzzle, i*2+2))))
        listKurangLabel[i*2+1].place(x=400, y=24+(i)*20)
        outputFile.write("Kurang(" + str(i*2+1) + ") = " +
                         str(Kurang(puzzle, i*2+1)) + "\n")
        outputFile.write("Kurang(" + str(i*2+2) + ") = " +
                         str(Kurang(puzzle, i*2+2)) + "\n")

    totalValue = sigmaKurang(puzzle) + posisiSelKosong(puzzle)
    sigmaKurangLabel = tkinter.Label(
        root, text="SigmaKurang + X = " + str(totalValue))
    sigmaKurangLabel.place(x=300, y=190)
    outputFile.write("SigmaKurang + X = " + str(totalValue) + "\n")

    if(puzzleCanBeSolve(puzzle, totalValue)):
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
        finishFrame = tkinter.Frame(master=root, width=275,
                                    height=100, background="green").place(x=300, y=280)
        finishLabel = tkinter.Label(
            finishFrame, text="Puzzle Has Been Solved !!", width=33, background="green", foreground="white")
        finishLabel.place(x=320, y=297)
        timeExecLabel = tkinter.Label(
            finishFrame, text=f"Time Execution: {end-start}", width=33, background="green", foreground="white")
        timeExecLabel.place(x=320, y=317)
        nodeRaisedLabel = tkinter.Label(
            finishFrame, text=f"Nodes Raised: {simpulChecked}", width=33, background="green", foreground="white")
        nodeRaisedLabel.place(x=320, y=337)
        outputFile.write("Puzzle Has Been Solved !!\n")
        outputFile.write(f"Time Execution: {end-start} \n")
        outputFile.write(f"Nodes Raised: {simpulChecked} \n")

        idGoal = simpulChecked
        iter = 1
        listLangkah = findLangkah(listSimpul, idGoal)
        for pzl in listLangkah:
            outputFile.write(
                "Langkah ke-" + str(iter) + "\n")
            iter += 1
            printPuzzle(pzl, outputFile)
            root.update()
            time.sleep(1)
            for i in range(4):
                for j in range(4):
                    if(pzl[i][j] != 16):
                        listPuzzleLabel[i*4+j].config(text=str(pzl[i][j]))
                    else:
                        listPuzzleLabel[i*4+j].config(text="")
    else:
        finishFrame = tkinter.Frame(master=root, width=275,
                                    height=100, background="red").place(x=300, y=280)
        finishLabel = tkinter.Label(
            finishFrame, text="Puzzle Can't Be Solved :(", font="Arial, 12", width=28, background="red", foreground="white")
        finishLabel.place(x=313, y=314)
        outputFile.write("Puzzle Can't Be Solved :(")


def randomClicked():
    randomList = random.sample(range(1, 17), 16)
    fillPuzzleFromList(puzzle, randomList)
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] != 16):
                listPuzzleLabel[i*4+j].config(text=str(puzzle[i][j]))
            else:
                listPuzzleLabel[i*4+j].config(text="")
    root.update()


def importClicked():
    file = open("../test/" + importFileEntry.get(), "r")
    for i in range(4):
        f = file.readline().split()
        for j in range(4):
            puzzle[i][j] = int(f[j])
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] != 16):
                listPuzzleLabel[i*4+j].config(text=str(puzzle[i][j]))
            else:
                listPuzzleLabel[i*4+j].config(text="")
    file.close()
    root.update()


root = tkinter.Tk()
root.geometry('600x400')

listPuzzleLabel = []
puzzleFrame = tkinter.Frame(master=root, width=250,
                            height=250, background="grey").place(x=25, y=25)

puzzle = [[i*4+j+1 for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        frame = tkinter.Frame(
            root, relief=tkinter.RAISED, borderwidth=2)
        a = (50+50*j)
        b = (50+50*i)
        frame.place(x=a, y=b)
        if(puzzle[i][j] != 16):
            label = tkinter.Label(master=frame, width=6,
                                  height=3, text=str(puzzle[i][j]))
        else:
            label = tkinter.Label(master=frame, width=6,
                                  height=3, text="")
        listPuzzleLabel.append(label)
        label.pack()
root.update()

randomButton = tkinter.Button(
    root, text="Randomize", width=10, command=randomClicked)
randomButton.place(x=25, y=280)

lbl = tkinter.Label(root, text="or")
lbl.place(x=125, y=280)

importFileEntry = tkinter.Entry(root, width=18)
importFileEntry.place(x=163, y=280)

importButton = tkinter.Button(
    root, text="IMPORT", width=10, command=importClicked)
importButton.place(x=125, y=320)

startButton = tkinter.Button(
    root, text="START", width=10, command=startSolver)
startButton.place(x=25, y=320)

root.mainloop()

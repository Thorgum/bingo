import random

grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

flags = [0] * 75

def generate_num():
    global exit
    exit = 0
    while exit != 1:
        num = random.randint(0, 74)
        if flags[num] != 1:  # Fixed indexing
            flags[num] = 1
            exit = 1
            return num  # Removed + 1

def grid_maker():
    global row, col,flags, grid
    row = 0
    col = 0
    while row != 5:  # Fixed row count
        col = 0
        while col != 5:
            num = generate_num()
            grid[row][col] = str(num + 1) # Adjusted indexing
            col += 1
        row += 1
    flags = [0] * 75
def checkbingo():
    global i
    global grid
    i = 0
    global bingo
    bingo = 0
    while bingo != 1:
        R = str(grid[i][0])+str(grid[i][1])+str(grid[i][2])+str(grid[i][3])+str(grid[i][4])
        C = str(grid[0][i]) + str(grid[1][i]) + str(grid[2][i]) + str(grid[3][i]) + str(grid[4][i])
        D = str(grid[0][0]) + str(grid[1][1]) + str(grid[2][2]) + str(grid[3][3]) + str(grid[4][4])
        OD = str(grid[0][4]) + str(grid[1][3]) + str(grid[2][2]) + str(grid[3][1]) + str(grid[4][0])
        if R == "00000" or C == "00000" or D == "00000" or OD == "00000":
            bingo = 1
            return 1
        elif i == 4:
            return 0
        else:
            i = i + 1
    if bingo == 0:
        return 0
def pgrid():
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[0][0]}   |  {grid[0][1]}   |  {grid[0][2]}   |  {grid[0][3]}   |  {grid[0][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[1][0]}   |  {grid[1][1]}   |  {grid[1][2]}   |  {grid[1][3]}   |  {grid[1][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[2][0]}   |  {grid[2][1]}   |  {grid[2][2]}   |  {grid[2][3]}   |  {grid[2][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[3][0]}   |  {grid[3][1]}   |  {grid[3][2]}   |  {grid[3][3]}   |  {grid[3][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[4][0]}   |  {grid[4][1]}   |  {grid[4][2]}   |  {grid[4][3]}   |  {grid[4][4]}   |")
    print("|                                       |")
    print("_________________________________________")

def pngrid(grid):
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[0][0]}   |  {grid[0][1]}   |  {grid[0][2]}   |  {grid[0][3]}   |  {grid[0][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[1][0]}   |  {grid[1][1]}   |  {grid[1][2]}   |  {grid[1][3]}   |  {grid[1][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[2][0]}   |  {grid[2][1]}   |  {grid[2][2]}   |  {grid[2][3]}   |  {grid[2][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[3][0]}   |  {grid[3][1]}   |  {grid[3][2]}   |  {grid[3][3]}   |  {grid[3][4]}   |")
    print("|                                       |")
    print("_________________________________________")
    print("|                                       |")
    print(f"|  {grid[4][0]}   |  {grid[4][1]}   |  {grid[4][2]}   |  {grid[4][3]}   |  {grid[4][4]}   |")
    print("|                                       |")
    print("_________________________________________")


grid_maker()
print("Welcome to Noah's Bingo.")
print("Your Bingo grid is shown below.")
pgrid()

A = input("Ready to begin? Yes/No ")
if A.lower() == "yes":
    global bingo
    bingo = 0
    global rolls
    rolls = 0
    while bingo != 1:
        global num
        num = generate_num()
        print("")
        print("")
        print("")
        print(f"The number is: {num}")
        row = 0
        col = 0
        while row < 5:  # Fixed row count
            col = 0
            while col < 5:
                if int(grid[row][col]) == num:
                    grid[row][col] = 0
                col += 1
            row += 1
        bingo = checkbingo()
        rolls = rolls + 1
        print("")
        print("")
        print("")
        pngrid(grid)
        ready = input("ready for next number? Y/N ")
        while ready.lower() != "y":
            ready = input("ready for next number? Y/N ")
    print("BINGO!!!!")
    print(f"It took you {rolls} spins.")

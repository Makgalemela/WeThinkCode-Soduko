# You may create additional functions here:
import ast


# The function read and manipulate data to a desirable format
def readFile():
    puzzleData = []
    # read - r
    # write - w

    with open("sample.txt", "r") as lines:
        lineData = []
        for line in lines:
            line = line.strip().replace('  ',', ').replace(' ','')
            if line[-1] == ',':
                line= line[:-1]
            puzzleData.append( ast.literal_eval(line))
    return puzzleData





# Function to print the 
def printPuzzle(puzzle):
    for line in puzzle:
        print(line,'\n')


def puzzleComplete(puzzle):

    for i in range(0,10):
        for j in range(0,10):
            if puzzle[i][j] == 0:
                return False
    
    return True

def computerRanges(quadrands):
    quadrandsConstrains = []
    quadrandsConstrains.append([1,[0,3],[0,3]])
    quadrandsConstrains.append([2,[3,6],[0,3]])
    quadrandsConstrains.append([3,[6,9],[0,3]])
    quadrandsConstrains.append([4,[0,3],[3,6]])
    quadrandsConstrains.append([5,[3,6],[3,6]])
    quadrandsConstrains.append([6,[6,9],[3,6]])
    quadrandsConstrains.append([7,[0,3],[6,9]])
    quadrandsConstrains.append([8,[3,6],[6,9]])
    quadrandsConstrains.append([9,[6,9],[6,9]])

    for line in quadrandsConstrains:
        if line[0] == quadrands:
            return line



def puzzleSolved(puzzle):
    total = 45
    for i in range(0,9):
        rowSum = 0
        columnSum =0
        for j in range(0,9):
            rowSum +=puzzle[i][j]
            columnSum +=puzzle[j][i]
        if rowSum != total or columnSum != total:
            return False
    return True


# We have 9 quadrand
def autoSolveAlgorithm(puzzleCopy , quadrand):
    quadrandData = []
    total = 45
    ranges = computerRanges(quadrand)
    puzzle = puzzleCopy
    rangeRow = ranges[2]
    rangeCol = ranges[1]
    printPuzzle(puzzle)
    print('/n')

    for i in range(rangeRow[0], rangeRow[1]):
        for j in range(rangeCol[0],rangeCol[1]):
            if puzzle[i][j] != 0:
                total =0
                quadrandData.append(puzzle[i][j])
                quadrandData.sort()
    numberToEValuate = 10
    numberWhichDoNoTExistInAQuadrand = []

    # Find missing number ins a quadrand
    for i in range(1,10): 
        for item in quadrandData:
            if i == item:
                numberToEValuate = 0
        if numberToEValuate ==10 :
            numberWhichDoNoTExistInAQuadrand.append(i)
    
    # Fill quadrand with missing numbers
    for i in range(rangeRow[0], rangeRow[1]):
        for j in range(rangeCol[0],rangeCol[1]):
            if puzzle[i][j] == 0:
                for num in numberWhichDoNoTExistInAQuadrand:
                    if not numberExistInRowColum(puzzle, i, j, num):
                        puzzle[i][j] = num
    
    if total == 0:
        autoSolveAlgorithm(puzzle , quadrand)
    else :
        print("Solved")
        printPuzzle(puzzle)
        return



# Chech if the function exist in both row and column

def numberExistInRowColum(puzzle, row, col , searcParam) :
    foundInRow = False
    foundInColumn = False
    #check if it exist in a row
    for i in range(0,9):
        if puzzle[row][i] ==searcParam:
            foundInRow = True
            break

    #check if it exist in columns
    for i in range(0,9):
        if puzzle[i][col] == searcParam:
            foundInColumn = True
            break

    if foundInColumn or foundInRow:
        return True
    elif foundInColumn and foundInRow:
        return True
    else :
        return False
           
# Additional Functions above this comment
# Implement your Sudoku Solution Below:
def solve_sudoku(puzzle):
    #Edit the code Below Here
    print("When pronted to enter row or col, row 1 would be enter as 0, and col 1 as 0 , row 9 as 8 and so on..")
    puzzleCopy = puzzle
    while not puzzleSolved(puzzleCopy) :
        print("..................................................",'\n')

        print("PUZZLE IS NOT YET SOLVED , enter -1 to quit",'\n')

        print("..................................................",'\n')
        printPuzzle(puzzleCopy)
        print("..................................................",'\n')

        firstValue = int(input("Please Enter your row : "))
        secondValue = int(input("Please Enter your col : "))
        if firstValue == -1 or secondValue ==-1 :
            break

        while firstValue >8 or secondValue >8 :
            firstValue = int(input("Please Enter your row (0-8) : "))
            secondValue = int(input("Please Enter your col (0-8) : "))
        
        solutionNumber = int(input("Please Enter the number : " ))
        if solutionNumber == -1:
            break
    
        puzzle[firstValue][secondValue] = solutionNumber


        #
        if puzzleSolved(puzzleCopy):
            cont = int(input("inputer Enter 1 to play again or 0 to quit : "))
            if cont == 1:
                solve_sudoku(puzzle)
            else:
                return

        # for i in range(1,10):
        #     autoSolveAlgorithm(puzzleCopy, i)




solve_sudoku(readFile())



import time
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
count=0

# Function to check if it is safe to go to cell (x, y) from current cell.
# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed
def isSafe(x, y, processed):
    return (0 <= x < M) and (0 <= y < N) and not processed[x][y]


# A recursive function to generate all possible words in a boggle
def searchBoggle(board, words, processed, i, j, path=""):
    # mark current node as processed
    processed[i][j] = True
    global count
    count=count+1
    # update the path with the current character and insert it into the set
    path = path + board[i][j]
    #sprint(path)
    words.add(path)

    # check for all 8 possible movements from the current cell
    for k in range(8):
        # skip if cell is invalid or it is already processed

        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, processed, i + row[k], j + col[k], path)



    # mark current node as unprocessed
    processed[i][j] = False


# Function to search for given set of words in a boggle
def searchInBoggle(board, input):
    # construct a matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]

    # construct a set to store all possible words constructed from the matrix
    words = set()

    # generate all possible words in a boggle
    for i in range(M):
        for j in range(N):
            # consider each character as a starting point and run DFS
            searchBoggle(board, words, processed, i, j)

    # for each word in the input list, check whether it is present in the set
    k=[word.upper() for word in input if word in words]
    return k


def runBoard(file_name):

    start=time.time()
    myBoard = open(file_name, 'r')
    board = []
    global count
    count=0
    for line in myBoard:
        letters = line.strip()
        print(letters)
        letters=letters.lower().split()
        board.append(letters)


    myDict = open('myDict.txt', 'r')
    dictionary = []
    for words in myDict:
        dictionary.append(words.strip())

    global M
    global N
    (M, N) = (len(board), len(board[0]))

    final_list=searchInBoggle(board, dictionary)
    d=[]
    max_len=max([len(i) for i in final_list])
    for i in range(max_len-1):
        d.append([])

    for i in final_list:
        d[len(i)-2].append(i)

    print("And we're off!")

    print("All done")
    print()
    print('Searched total of {} moves in {} seconds'.format(count,time.time()-start))
    print()
    print('Words found')
    for key,values in enumerate(d):
        print('{} -letter words:'.format(key+2),end="  ")
        for i in values:
            print(i,end=" ")
        print()

    print()
    print('Found {} words in total:'.format(len(final_list)))
    print('Alpha-sorted list words:')
    print(final_list)
    print()

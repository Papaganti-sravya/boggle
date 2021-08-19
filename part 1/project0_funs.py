import sys
import random

def loadBoard(file_name):
    '''
    #random generator 
    alpha =list('abcdefghijklmnopqrstuvwxyz')   # The letters we need to pickup from 
    size = int(input("enter the size: "))   # we will input the size of the boggle 4*4 0r 10*10
    random.seed(0)
    s = random.choices(alpha, k=size*size,)     #create a board of random with given size 

    file_obj = open(file_name,"w")    # we will store the boggle in a file the file name is given in function calling 
    for i in range(0,size*size,size):               
        file_obj.write(' '.join(s[i:i+size])+"\n")   # used to arrange the elements as a matrix 
    '''
    obj=open(file_name,'r')   #used to write the matrix in the give file 
    
    return obj     #return the file object 
    
    '''     
     # an other way to print the elements in the matrix form  
    for i in range(0,size*size,size):    
        for j in range(i,i+size):       
            print(s[j],end=" ")
        print("\n")   
    ''' 

def printBoard(file):
    for line in file.readlines():   
        print(line.strip())         #print every line 
    
    


def possibleMoves(pos, file):

    x=pos[0]   # initialising the first axis in the given index(0,0) as x
    y=pos[1]   # initialising the second axis in the given index(0,0) as y
    a=[]
    file.seek(0)   #since we opened the file previous the cursor will be at the end, with this we will get the cursor to the beginning of the file 

    line=file.read().splitlines()  
    #print(line)
    '''
    for line in file.readlines():
        (line.strip())
        '''
    size=((len(line[0])+1))//2  #to get the size of one line (characters)
    #print(size)

    #logic to make sure that the point should not go out of the board 

    if x+1<size and y+1<size:
        a.append((x+1,y+1))  
    if x+1<size and y-1>=0:
        a.append((x+1,y-1)) 
    if x+1<size:
        a.append((x+1,y)) 
    if x-1>=0 and y+1<size:
        a.append((x-1,y+1))
    if x-1>=0 and y-1>=0:
        a.append((x-1,y-1))
    if x-1>=0:
        a.append((x-1,y))
    if y-1>=0:
        a.append((x,y-1))
    if y+1<size:
        a.append((x,y+1))
    return a


def legalMoves(moves , exsited_moves):
    #print(moves)
    #print("em",exsited_moves)
    #Logic to print the index which are not there in the existing moves 
    #basically to remove the common index points 
    print(set(moves)-set(exsited_moves))


def examineState(myBoard, pos, dic, myDict):
    myBoard.seek(0) 
    myDict.seek(0)
    flag = 0
    word = [] # an list to for a word in dic 
    
    for line in myBoard.readlines():
        word.append(line.strip().split())
    
    #logic to append the elements that are in dic
    Word_req = ''
    for i,j in dic:
        Word_req = Word_req + word[i][j]
    

    #A string to create a final word 
    #logic to append the final element of the word that comes from the pos index 
    xx= pos[0]
    yy= pos[1]
    Word_req = Word_req + word[xx][yy]

    #logic to check if the word is there in the dictonary or not  
    for line in myDict:
        #print(Word_req.lower())
        if (Word_req.lower()) == line.strip():
            print(Word_req, "Yes")
            #print(line)
            flag = 1
            break 
    if flag==0:
        print(Word_req , "No")
    
    #myBoard.close()
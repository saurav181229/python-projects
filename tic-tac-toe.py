#basic tic tac toe game
import random
import time
name='none'
global a
board = {'top-left':' ','top-middle':' ','top-right':' ',
          'center-left':' ','center-middle':' ','center-right':' ',
          'bottom-left':' ','bottom-middle':' ','bottom-right':' '
                           }

# to display the board
def boardDisplay():
    print(" board configuration is: ")
    print(f"{board['top-left']}|{board['top-middle']}|{board['top-right']}")
    print("------")
    print(f"{board['center-left']}|{board['center-middle']}|{board['center-right']}")
    print('------')
    print(f"{board['bottom-left']}|{board['bottom-middle']}|{board['bottom-right']}")





 #to select the block by the user
def userChoice():
    choice = input("enter the position(top-left,top-middle,top-right,center-left,center-middle,center-right,bottom-left ,bottom-middle, bottom-right):")
    board[choice] = 'X';


# random selection of a block by user
def compChoice():
    dic = dict()
    for (key,values) in board.items():
        if values == ' ':
            dic[key]=values
    compChoice = random.choice(list(dic.keys()))
    board[compChoice]='O'    

 #checks the board status on who is winning
def winStatus():
    global a    
    if(board['top-left']==board['top-right'] and board['top-right']==board['top-middle']):
        if(board['top-left']!=' '):
            a = board['top-left']
    elif (board['center-left']==board['center-right'] and board['center-right']==board['center-middle']):
        if board['center-left']!=' ':
            a = board['center-left']
    elif (board['bottom-left']==board['bottom-right'] and board['bottom-right']==board['bottom-middle']):
        if board['bottom-left']!=' ':
            a = board['bottom-left']
    elif (board['top-left']==board['bottom-left'] and board['top-left']==board['center-left']):
        if board['top-left']!=' ':
            a = board['top-left']
    elif (board['top-middle']==board['center-middle'] and board['center-middle']==board['bottom-middle']):
        if board['top-middle']!=' ':
            a = board['top-middle']
    elif (board['top-right']==board['center-right'] and board['center-right']==board['bottom-right']):
        if board['top-right']!=' ':
            a = board['top-right']
    elif (board['top-left']==board['center-middle'] and board['top-left']==board['bottom-right']):
        if board['top-left']!=' ':
            a = board['top-left']
    else: 
        if(board['top-right']==board['center-middle'] and board['center-middle']==board['bottom-left']):
            if board['bottom-left']!=' ':
                a = board['bottom-left']
    return a



#game start function
def start():
    global a
    a = ' '
    count = 0
    while a ==' ':
        count+=1
        boardDisplay()
        userChoice()
        boardDisplay()
        compChoice()
        boardDisplay()
        winStatus()
        if a!=' ':
            break
        if count>4:
            break

    if a =='X':
        print(f"{name} is victorious!! ")

    elif a =='O':
        print("computer is victorious!! better luck next time")
    else:
        print("its a tie")

#welcome screen
def welcome():
    global name
    name = input("enter your name :")
    time.sleep(3)
    print(f" welcome {name} to tic tac toe !!!")
    start()



welcome()
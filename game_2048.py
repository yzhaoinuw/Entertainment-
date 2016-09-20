#Author: Yue Zhao
#Lab 14: 2048

#This program runs the game of 2048, in which a player's goal is to make the number
#2048 in at least one tile out of the randomly given tile of 2 or 4 by add neighboring 
#tiles up. 

from random import randint #for randomly picking empty tiles and assigning 2 or 4
#starting with an empty 4 by 4 game board
gameboard = [['    ','    ','    ','    '],['    ','    ','    ','    '],['    ','    ','    ','    '],['    ','    ','    ','    ']]

def add_newtile():
    emptytiles = []  #this list collects all the empty tiles
    for i in range(4):
        for j in range(4):
            if gameboard[i][j] == '    ':  #this is how empty tile is defined
                emptytiles.append([i,j])
    if len(emptytiles) > 0:   #if there are empty tiles put a 2 or 4 in one of them            
        emptytile = emptytiles[randint(0,len(emptytiles)-1)]  #randomly pick one from the empty tiles
        gameboard[emptytile[0]][emptytile[1]] = [2,2,2,2,2,2,2,2,2,4][randint(0,9)] #giving a 10% chance of getting a 4 
 
def display():
    for k in range(4): #print one out of the 4 rows per iteration
        l1 = 4 - len(str(gameboard[k][0])) #2048 is four digit, so let max digit 
        l2 = 4 - len(str(gameboard[k][1])) #print space before numbers so that every
        l3 = 4 - len(str(gameboard[k][2])) #tile has the same length
        l4 = 4 - len(str(gameboard[k][3]))
        print '-' * 21 #print the roof or floor of the game board  
        print '|' +' '* l1 +str(gameboard[k][0])+ '|' +' '* l2 +str(gameboard[k][1])+ '|' +' '* l3 +str(gameboard[k][2])+ '|' +' '* l4 +str(gameboard[k][3])+'|'  
    print '-' * 21 #add a floor
    print #leave some space between each display

def win():
    for row in gameboard:
        for tile in row:
            if tile == 2048:   #if you want to cheat,change 2048 to, say, 8
                return True
            
def move_up():
    C0 = [gameboard[0][0],gameboard[1][0],gameboard[2][0],gameboard[3][0]] #extract and store the columns
    C1 = [gameboard[0][1],gameboard[1][1],gameboard[2][1],gameboard[3][1]]    
    C2 = [gameboard[0][2],gameboard[1][2],gameboard[2][2],gameboard[3][2]]
    C3 = [gameboard[0][3],gameboard[1][3],gameboard[2][3],gameboard[3][3]]
    C = [C0] + [C1] + [C2] + [C3] #making a giant list for iteration purpose
    n = 0
    for i in range(4):
        values = []  #this is a list to store the numbers in a column
        for tile in C[i]:
            if tile != '    ':
                values.append(tile)
        values = values + ['    '] * (4-len(values)) #ensure that this list has four elements
        if values != C[i]:
            n += 1
        for j in range(4):       
            gameboard[j][i] = values[j] #reassigning the values to gameboard thus accomplishing move-up
    if n > 0:
        return True #by returning True here, this function actually does two things at the same time
    else:
        return False
    
def up_addition():
    n = 0    
    if move_up() == True: #While it's checking for True, it actually also does move things up 
        n += 1            #we need to move tiles before doing addition
    for i in range(3): #since it's up addition, we look one row below down so omit the last row to avoid IdexError
        for j in range(4): 
            if gameboard[i][j] != '    ' and gameboard[i][j] == gameboard[i+1][j]: #check for addability
                gameboard[i][j] = gameboard[i][j] + gameboard[i+1][j] #replace the upper tile with the sum
                gameboard[i+1][j] = '    '  #replace the lower tile with empty tile
                n += 1
    if n > 0:  #if any changes were made, move again and add a new tile 
        move_up()
        add_newtile()         
        display()
    else:  #if there either move available or addition can be done in this direction 
        print 'there is no more addition in this direction'
    
def move_down(): #almost the same as move_up, just need to do it in opposite direction
    C0 = [gameboard[3][0],gameboard[2][0],gameboard[1][0],gameboard[0][0]] #the order of the columns is
    C1 = [gameboard[3][1],gameboard[2][1],gameboard[1][1],gameboard[0][1]] #flipped compare to move_up   
    C2 = [gameboard[3][2],gameboard[2][2],gameboard[1][2],gameboard[0][2]]
    C3 = [gameboard[3][3],gameboard[2][3],gameboard[1][3],gameboard[0][3]]
    C = [C0] + [C1] + [C2] + [C3] 
    n = 0
    for i in range(4):
        values = []  
        for tile in C[i]:
            if tile != '    ':
                values.append(tile)
        values = values + ['    '] * (4-len(values)) 
        if values != C[i]:
            n += 1
        for j in range(4):       
            gameboard[j][i] = values[3-j] 
    if n > 0:
        return True
    else:
        return False

def down_addition():
    n = 0
    if move_down() == True:
        n += 1 
    for i in range(3): 
        for j in range(4): 
            if gameboard[3-i][j] != '    ' and gameboard[3-i][j] == gameboard[2-i][j]: 
                gameboard[3-i][j] = gameboard[3-i][j] + gameboard[2-i][j] 
                gameboard[2-i][j] = '    '  #replace the upper tile with empty tile
                n += 1
    if n > 0:   
        move_down()
        add_newtile()         
        display()
    else:
        print 'there is no more addition in this direction' 

def move_left():  #move horizontally is a little different from moving vertically
    n = 0         #but the idea is the same 
    for i in range(4):
        values = []
        for j in range(4):
            if gameboard[i][j] != '    ':
                values.append(gameboard[i][j])
        values = values + ['    '] * (4-len(values))
        if values != gameboard[i]:
            n +=1
        for k in range(4):
            gameboard[i][k] = values[k]               
    if n > 0:
        return True
    else:
        return False    

def left_addtion(): #similar idea as adding vertically, need to watch out for
    n = 0           #out of index
    if move_left() == True:
        n += 1 
    for i in range(4):
        for j in range(3):
            if gameboard[i][j] != '    ' and gameboard[i][j] == gameboard[i][j+1]:
                gameboard[i][j] = gameboard[i][j] + gameboard[i][j+1]
                gameboard[i][j+1] = '    '
                n += 1
    if n > 0:
        move_left()
        add_newtile()
        display()
    else:
        print 'there is no more addition in this direction' 
    
def move_right():
    n = 0
    for i in range(4):
        values = []
        for j in range(4):
            if gameboard[i][3-j] != '    ':
                values.append(gameboard[i][3-j])
        values = values + ['    '] * (4-len(values))
        if values != gameboard[i][::-1]:
            n +=1
        for k in range(4):
            gameboard[i][3-k] = values[k]               
    if n > 0:
        return True
    else:
        return False  

def right_addition():
    n = 0
    if move_right() == True:
        n += 1 
    for i in range(4):
        for j in range(3):
            if gameboard[i][3-j] != '    ' and gameboard[i][3-j] == gameboard[i][2-j]:
                gameboard[i][3-j] = gameboard[i][3-j] + gameboard[i][2-j]
                gameboard[i][2-j] = '    '
                n += 1
    if n > 0:
        move_right()
        add_newtile()
        display()
    else:
        print 'there is no more addition in this direction' 
    
def playability(): # a function that checks for playability 
    n = 0
    for i in range(4):      #range of 4 are used for both i and j here, so I will try and except
        for j in range(4):  # IndexError. this way I check all the directions using one double loop 
            if gameboard[i][j] == '    ':
                n += 1 #if there is still empty spot, it's certainly still playable
            try: #if there is potential for addition in any direction, it's still playable
                if gameboard[i][j] != '    ' and gameboard[i][j] == gameboard[i+1][j]:
                    n += 1
            except IndexError:
                pass        
            try:    
                if gameboard[i][j] != '    ' and gameboard[i][j] == gameboard[i][j+1]:
                    n += 1
            except IndexError:
                pass          
    if n == 0:  #if no playable, return False, indicating that the game is not playable anymore
        return False
        
start = True  #two while loops, this one is for restarting a new game without running 
while start == True:    #the program again 
    gameboard = [['    ','    ','    ','    '],['    ','    ','    ','    '],['    ','    ','    ','    '],['    ','    ','    ','    ']]
    add_newtile() 
    add_newtile()
    display()
    playable = True
    while playable == True:   #this loop is for repeatedly making moves 
        move = raw_input('Direction: ') 
        if move == 'u':
            up_addition() 
        if move == 'd':
            down_addition() 
        if move == 'l':
            left_addtion() 
        if move == 'r':
            right_addition()   
        if win() == True:
            print "Congratulations! You have won the game!!! "
            onemore = raw_input('Would you like one more game? (y/n)') 
            if onemore == 'n':
                print "Thanks for playing!"
                playable = False
                start = False  #quit both loops
            else:
                playable = False #quit one loop, and start over the game
        if playability() == False: #check for playability. if no addition and
            print "Game over!"     #no move can be made, then the game is over
            onemore = raw_input('Would you like one more game? (y/n)')
            if onemore == 'n':
                print "Thanks for playing!"
                playable = False
                start = False  
            else:
                playable = False                        
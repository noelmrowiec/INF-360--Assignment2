# INF360 - Programming in Python
# Noel Mrowiec
# Assignment 2
# CHO-HAN Dice Game
# 29JAN2023

import random, sys
numOfRounds = 3

print('Welcome to the CHO-HAN Dice Game!')
print('The rules: ')
print('Goal of the game: Literally meaning "even-odd" in Japanese, this is another dice gambling game, played with only two dice and a considerable amount of theatrics. \
It\'s really pretty simple: the dice thrower makes a bet on the outcome of the roll and rolls their dice. If you guess correctly, you win bet based on the odds of your choice. \
If you guess incorrectly, you lose your bet. There are ' +str(numOfRounds)+ ' total rounds. Highest score wins!\n')


selection = ''


#Print inital screen
while True:
    selection  = input('Press "v" to view the odds of each bet type\n"q" to quit\nOr press enter to continue!')
    selection = selection.lower()       #parse input

    #Check input
    if selection == 'q':
        print('Now quitting, play again soon!')
        sys.exit(0)                               #exit 
    elif selection == 'v':
        print('Below are the odds:\nLuckey 8: Pays 6.84 for 1\nPair: Pays 5.7 for 1\nEven: Pays 1.9 for 1\nOdd: Pays 1.9 for 1\n')
        continue                            #go back to the start of while loop after printing
    else:
        break                               #move to the play screen
         
#play screen
numOfPlayers = 2
pl1Score = 0
pl2Score = 0
playerTurn = 1;                         #playerTurn = 1 is player 1's turn, and playerTurn = 2 is player 2's turn
currentRound = 1;

for i in range(numOfRounds * numOfPlayers):     #loop is for each player, so 2 players for 3 rounds requires 6 loops
    selection
    while True:
        selection  = input('\nPlayer ' +str(playerTurn) + ' enter your bet type: \n"o" for odd \n"e" for even \n"p"  for pairs (i.e. 2 and 2, 5 and 5) \n\
    "l" for lucky 8 (total equal 8) \n"v" to view the odds of each bet type\n"q" to quit\n')
        selection = selection.lower()           #parse input

        #Check input
        if selection == 'q':
            print('Now quitting, play again soon!')
            sys.exit(0)                                     #exit 
        elif selection == 'v':
            print('Below are the odds:\nLuckey 8: Pays 6.84 for 1\nPair: Pays 5.7 for 1\nEven: Pays 1.9 for 1\nOdd: Pays 1.9 for 1\n')
            #continue                                #go back to the start of while loop after printing
        elif selection != 'o'  and selection != 'e' and selection != 'p' and selection != 'l' and selection != 'v':
            print('Selection incorrrect\n')         #go back to the start of while loop after printing
            #continue
        else:
            print('Player ' + str(playerTurn) +': you selected ' + str(selection))
            break
    #end check for input
    
    #check that is a valid number
    noEnteredNum = True;
    while noEnteredNum:
        try:
            bet = int(input('Player ' +str(playerTurn)+ ' , make your bet (1-100)\n'))  #check that bet is a number. Found this on https://pythonguides.com/
            noEnteredNum = False;
        except:
            noEnteredNum = True;
        
    #stay in loop until a interger is entered
        
    #subtract bet from total
    if playerTurn == 1:
        pl1Score -= bet
    else:
        pl2Score -= bet

    input('Press any key to roll\n')
    #roll die
    dieA = random.randint(1,6)
    dieB = random.randint(1,6)
    print('You rolled: ' +str(dieA)+ ' and ' +str(dieB) +'\n')

    #Score player
    winnings = 0
    
    if (dieA + dieB) == 8 and selection == 'l':
        print('You win! Luckey 8: Pays 6.84 for 1\n')
        winnings = bet * 6.84
    elif dieA == dieB and selection == 'p':
        print('You win! Pair: Pays 5.7 for 1\n')
        winnings = bet * 5.7
    elif (dieA + dieB) % 2 == 0 and selection == 'e':
        print('You win! Even: Pays 1.9 for 1\n')
        winnings = bet * 1.9
    elif (dieA + dieB) % 2 != 0 and selection == 'o':
        print('You win! Odd: Pays 1.9 for 1\n')
        winnings = bet * 1.9         
    else:
        print('Sorry, you lost\n')

    #Add to total
    if playerTurn == 1:
        pl1Score += winnings
    else:
        pl2Score += winnings

    print('Current round: ' +str(currentRound))     
    print('Current score: \nPlayer 1 = ' + str(pl1Score) + '\nPlayer 2 = ' + str(pl2Score) + '\n')

    #switch player: next player gets a turn
    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1
        currentRound += 1      # only update the round after player 2 has finished

#10 rounds finished, game over
print('Game over!')
print('Final score: \nPlayer 1= ' + str(pl1Score) + '\nPlayer 2 = ' + str(pl2Score) + '\n')
if pl1Score > pl2Score:
    print('Player 1 wins!')
elif pl1Score < pl2Score:
    print('Player 2 wins!')
else:
    print('Wow... you tied.... embarrassing....\n')



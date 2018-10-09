import random
import time


class reassign(object):
    #This class stores the integer number of the player's value once they abstain at any point
    #reassign_pv will be used to compare compturn vlue to player value and return a string 
    def __init__(self, pvalue= 0):
        self.pvalue = pvalue

    def reassign_pv(self):
        #This class holds the value of the player's value outside of playerturn()
        return self.pvalue

class reassign2(object):
    #This class holds the value of the dealers's value outside of compturn()
    def __init__(self,dvalue= 0):
        self.dvalue = dvalue

    def reassign_dv(self):
        return self.dvalue

class wintotal(object):
    def __init__(self, wins=0):
        self.wins = wins

    def reassignwins(self):
        return self.wins


def endgame():
    #Asks if the player wants to play again
    return input('\nDo you want to play again? [y/n] ').lower().startswith('y')

def cont():
    #Acts as a break in the code that asks for player input
    question = ' '

    while not question == 'y':
        question = input("\nPRESS Y TO CONTINUE \n  ").lower()
        if question.startswith('y'):
            pass
    else:
        pass

def compturn():
    #This function is called when the plyer abstains
    #The dealer will abstain at a value of >16 unless they are "feeling lucky" ;)
    print("\n\n\nDEALER TURN\n\n\n")

    while True:

        
        card1 = random.randint(1,10)
        card2 = random.randint(1,10)

        CHANCE = random.randint(1,100)
        if CHANCE <= 20:
            CHANCE = True
        else:
            CHANCE = False

        #q = input('\n\n Its now the dealers turn...PRESS "Y" TO CONTINUE  ').lower()
        #if q == 'y':
        card1 = random.randint(1,10)
        card2 = random.randint(1,10)


        while True:
            print("Dealer cards are ", card1, " and ", card2)
            value = card1 + card2
            print("\tVALUE = ", value)

            while value <= 16:
                #cont()
                time.sleep(2)
                new_card = random.randint(1,10)
                print("Dealer draws a " , new_card)
                value += new_card
                print('\t','VALUE = ',value)

            if  value < 21 and CHANCE:
                #cont()
                time.sleep(2)
                print("\t\tDEALER IS FEELING LUCKY!!!")
                new_card = random.randint(1,10)
                print("Dealer draws a " , new_card)
                value += new_card
                print('\t',"VALUE = ", value)

            if value < check.reassign_pv():
                print('you win, the dealers value of ', value, ' was less than your ', check.reassign_pv() ) 
                data_file = open('wins.txt', 'r')
                win_total = int(data_file.read())
                win_total += 1
                print('\n\n...................',win_total,' TOTAL WINS...................\n\n')
                data_file.close()
                data_file = open('wins.txt', 'w')
                data_file.write(str(win_total))
                data_file.close()
            elif value > check.reassign_pv() and value <= 21:
                print('you lose, the dealers value of ', value, ' was more than your ', check.reassign_pv() )
            elif value > 21:
                print('you win, the dealers value of ' , value, ' went over 21' )
                data_file = open('wins.txt', 'r')
                win_total = int(data_file.read())
                win_total += 1
                print('\n\n...................',win_total,' TOTAL WINS...................\n\n')
                data_file.close()
                data_file = open('wins.txt', 'w')
                data_file.write(str(win_total))
                data_file.close()

            break
        break

    
    #else:
    #   print('Loading...')
    #break


def playerturn():
    # This function is the players turn.
    def manual_play():
        while True:
        
            card1 = random.randint(1,10)
            card2 = random.randint(1,10)

            print('\n',card1, card2, '(value of ',card1+card2, ')')
            #Q sees if the palyer want to hit or absatin... if abstain at any point, go to computer/dealer turn
            q = input('^^^^^ You have been delt these 2 cards  do you want to HIT or ABSTAIN?  [H/A]').lower()
            if q.startswith('h'):
                card3 = random.randint(1,10)
                print('Your new card is ', card3)
                val = card1 + card2 + card3
                print('You have a value of ', val)

                if val > 21:
                    print('SORRY, you have lost the game')
                    if not endgame():
                        break
                elif val == 21:
                    print('CONGRATULAIONS, you have won the game')
                    if not endgame():
                        break

                elif val < 21:
                    print('\n', val)
                    q2 = input('This is your value, do you want to HIT or ABSTAIN?  [H/A]').lower()
                    if q2.startswith('h'):
                        
                        card4 = random.randint(1,10)
                        print('Your new card is ', card4)
                        val2 = val + card4
                        print('You have a value of ', val2)
                        if val2 > 21:
                            print('SORRY, you have lost the game')
                            if not endgame():
                                break
                        elif val2 == 21:
                            print('CONGRATULAIONS, you have won the game')
                            if not endgame():
                                break
                        elif val2 < 21:
                            print('\n', val2)
                            q3 = input('This is your value, do you want to HIT or ABSTAIN?  [H/A]').lower()
                            if q3.startswith('h'):
                        
                                card5 = random.randint(1,10)
                                print('Your new card is ', card5)
                                val3 = val2 + card5
                                print('You have a value of ', val3)

                                if val3 > 21:
                                    print('SORRY, you have lost the game')
                                    if not endgame():
                                        break
                                elif val3 == 21:
                                    print('CONGRATULAIONS, you have won the game')
                                    if not endgame():
                                        break
                                elif val3 < 21:
                                    print('\n', val3)
                                    q4 = input('This is your value, do you want to HIT or ABSTAIN?  [H/A]').lower()
                                    if q4.startswith('h'):
                                
                                        card6 = random.randint(1,10)
                                        print('Your new card is ', card6)
                                        val4 = val3 + card6
                                        print('You have a value of ', val4)

                                        if val4 > 21:
                                            print('SORRY, you have lost the game')
                                            if not endgame():
                                                break
                                        elif val4 == 21:
                                            print('CONGRATULAIONS, you have won the game')
                                            if not endgame():
                                                break
                                        elif val4 < 21:
                                            print('\n', val4)
                                            q5 = input('This is your value, do you want to HIT or ABSTAIN?  [H/A]').lower()
                                            if q5.startswith('h'):

                                                card7 = random.randint(1,10)
                                                print('Your new card is ', card7)
                                                val5 = val4 + card7
                                                print('You have a value of ', val5)

                                                if val5 > 21:
                                                    print('SORRY, you have lost the game')
                                                    if not endgame():
                                                        break
                                                elif val5 == 21:
                                                    print('CONGRATULAIONS, you have won the game')
                                                    if not endgame():
                                                        break
                                                elif val4 < 21:
                                                    break
                                            
                                            elif q5.startswith('a'):
                                                print('Your value is ', val4)
                                                global check
                                                #Check is global so that it ca be called in compturn 
                                                #check is reassigned and stored in the class, then compturn is called
                                                check = reassign(val4)
                                                check.reassign_pv()
                                                compturn()
                                                break

                                    elif q4.startswith('a'):
                                        print('Your value is ', val3)
                                        check = reassign(val3)
                                        check.reassign_pv()
                                        compturn()
                                        break                    

                            elif q3.startswith('a'):
                                print('Your value is ', val2)
                                check = reassign(val2)
                                check.reassign_pv()
                                compturn()
                                break

                    elif q2.startswith('a'):
                        print('Your value is', val)
                        check = reassign(val)
                        check.reassign_pv()
                        compturn()
                        break    

            elif q.startswith('a'):
                print('You have a value of ', card1+card2)
                check = reassign(card1+card2)
                check.reassign_pv()
                compturn()
                break
    def auto_play():
        print("\n\n\PLAYER TURN\n\n\n")

        global check
        card1 = random.randint(1,10)
        card2 = random.randint(1,10)

        CHANCE = random.randint(1,100)
        if CHANCE <= 20:
            CHANCE = True
        else:
            CHANCE = False



        while True:
            print("YOUR cards are ", card1, " and ", card2)
            value = card1 + card2
            print("\tVALUE = ", value)

            while value <= 16:
                #cont()
                time.sleep(2)
                new_card = random.randint(1,10)
                print("YOU DRAW A " , new_card)
                value += new_card
                print('\t','VALUE = ',value)

            if  value < 21 and CHANCE:
                #cont()
                time.sleep(2)
                print("\t\YOU ARE FEELING LUCKY!!!")
                new_card = random.randint(1,10)
                print("YOU GET A " , new_card)
                value += new_card
                print('\t',"VALUE = ", value)

                if value > 21:
                    print('You LOSE!!')
                    
                    break
                elif value == 21:
                    print('YOU HAVE WON!!!!')
                    data_file = open('wins.txt', 'r')
                    win_total = int(data_file.read())
                    win_total += 1
                    print('\n\n...................',win_total,' TOTAL WINS...................\n\n')
                    data_file.close()
                    data_file = open('wins.txt', 'w')
                    data_file.write(str(win_total))
                    data_file.close()
                    
                    break
                else:
                    check = reassign(value)
                    check.reassign_pv()
                    compturn()
                    break


            if value > 21:
                print("YOU LOSE!!!")
                #if not endgame():
                #    break
            elif value == 21:
                print('YOU HAVE WON!!!!')
                data_file = open('wins.txt', 'r')
                win_total = int(data_file.read())
                win_total += 1
                print('\n\n...................',win_total,' TOTAL WINS...................\n\n')
                data_file.close()
                data_file = open('wins.txt', 'w')
                data_file.write(str(win_total))
                data_file.close()
                #if not endgame():
                #    break
            else:
                check = reassign(value)
                check.reassign_pv()
                compturn()
                break
            #compturn()
    '''
    question = input('AUTOMATED PLAY?   [y/n]').lower()
    if question.startswith('y'):
        auto_play()
    else:
        manual_play()
    '''

    auto_play()
            


def play():
    #This function starts the game then goes into the player turn.
    while True:
        
        uname = input('Do you want to play a game of BLACKJACK? [y/n] ').lower()
        if uname.startswith('y'):
            game_on = True
        else:
            print('Alrght then, bye')
            game_on = False

        while game_on:
            
            question = ' '

            while not (question == 'y') or (question == 'n'):
                playerturn()
        break

play()
print('Thanks for playing BLACKJACL by timmyu32')

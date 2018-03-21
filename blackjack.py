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
    def __init__(self, wins):
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
    #The dealer will abstain at a value of >16
    while True:

        import random
        card1 = random.randint(1,10)
        card2 = random.randint(1,10)
        val = card1 + card2

        q = input('\n\n Its now the dealers turn...PRESS "Y" TO CONTINUE  ').lower()
        if q == 'y':
            print(card1, card2, '(', card1+card2, ')')
            print('^^^^^ These are the dealers cards')
            if val <= 16:
                cont()
                print('The dealer will get a new card')
                card3 = random.randint(1,10)
                val2 = val + card3
                print('The new card is ', card3,'... Value is now ', val2)
                
                if val2 <= 16:
                    cont()
                    print('The dealer will get a new card')
                    card4 = random.randint(1,10)
                    val3 = val2 + card4
                    print('The new card is ', card4,'... Value is now ', val3)

                    if val3 <= 16:
                        cont()
                        print('The dealer will get a new card')
                        card5 = random.randint(1,10)
                        val4 = val3 + card5
                        print('The new card is ', card5,'... Value is now ', val4)

                        if val4 <= 16:
                            cont()
                            print('The dealer will get a new card')
                            card6 = random.randint(1,10)
                            val5 = val4 + card6
                            print('The new card is ', card6,'... Value is now ', val5)

                            if val5 <=16:
                                cont()
                                print('The dealer will get a new card')
                                card7 = random.randint(1,10)
                                val6 = val5 + card7
                                print('The new card is ', card7,'... Value is now ', val6)

                                if val6 <= 16:
                                    cont()
                                    print('The dealer will get a new card')
                                    card8 = random.randint(1,10)
                                    val7 = val6 + card8
                                    print('The new card is ', card8,'... Value is now ', val7)

                                elif val6 > 16 and val6 < 21:
                                    print('The dealer will abstain')
                                    var = reassign2(val6)
                                    a = var.reassign_dv()
                                    if a < check.reassign_pv():
                                        print('\n\t YOU WIN!! Your value of ', check.reassign_pv(), ' was greater than the dealers value of ', val6)
                                        break
                                    elif a == check.reassign_pv():
                                        print('\n\t TIE GAME!! Your value of ', check.reassign_pv(), ' was equal to the dealers value of ', val6)
                                        break
                                    else:
                                        print('\n\t You loose, your value of ', check.reassign_pv(), ' was less than the dealers value of ', val6)
                                        break

                                elif val6 == 21:
                                    print('The dealer wins!!')
                                    if not endgame():
                                        break

                                elif val6 > 21:
                                    print('You win, the dealer is over 21!')
                                    break

                            elif val5 > 16 and val5 < 21:
                                print('The dealer will abstain')
                                var2 = reassign2(val5)
                                b = var2.reassign_dv()
                                if b < check.reassign_pv():
                                    print('\n\t YOU WIN!! Your value of ', check.reassign_pv(), ' was greater than the dealers value of ', val5)
                                    break
                                elif b == check.reassign_pv():
                                    print('\n\t TIE GAME!! Your value of ', check.reassign_pv(), ' was equal to the dealers value of ', val5)
                                    break
                                else:
                                    print('\n\t YOU LOOSE!! Your value of ', check.reassign_pv(), ' was less than the dealers value of ', val5)
                                    break

                            elif val5 == 21:
                                print('The dealer wins!!')
                                if not endgame():
                                    break
                                else:
                                    break

                            elif val5 > 21:
                                print('You win, the dealer is over 21!')
                                break

                        elif val4 > 16 and val4 < 21:
                            print('The dealer will abstain')
                            var3 = reassign2(val4)
                            c = var3.reassign_dv()
                            if c < check.reassign_pv():
                                print('\n\t YOU WIN!! Your value of ', check.reassign_pv(), ' was greater than the dealers value of ', val4)
                                break
                            elif c == check.reassign_pv():
                                print('\n\t TIE GAME!! Your value of ', check.reassign_pv(), ' was equal to the dealers value of ', val4)
                                break
                            else:
                                print('\n\t YOU LOSE!! Your value of ', check.reassign_pv(), ' was less than the dealers value of ', val4)
                                break

                        elif val4 == 21:
                            print('The dealer wins!!')
                            if not endgame():
                                break
                            else:
                                break

                        elif val4 > 21:
                            print('You win, the dealer is over 21!')
                            break

                    elif val3 > 16 and val3 < 21:
                        print('The dealer will abstain')
                        var4 = reassign2(val3)
                        d = var4.reassign_dv()
                        if d < check.reassign_pv():
                            print('\n\t YOU WIN!! Your value of ', check.reassign_pv(), ' was greater than the dealers value of ', val3)
                            break
                        elif d == check.reassign_pv():
                            print('\n\t TIE GAME!! Your value of ', check.reassign_pv(), ' was equal to the dealers value of ', val3)
                            break
                        else:
                            print('\n\t YOU LOOSE!! Your value of ', check.reassign_pv(), ' was less than the dealers value of ', val3)
                            break

                    elif val3 == 21:
                        print('The dealer wins!!')
                        if not endgame():
                            break
                        else:
                            break

                    elif val3 > 21:
                        print('You win, the dealer is over 21!')
                        break

                elif val2> 16 and val2<21:
                    print('The dealer abstains')
                    var5 = reassign2(val2)
                    e = var5.reassign_dv()
                    if e < check.reassign_pv():
                        print('\n\t YOU WIN!! Your value of ', check.reassign_pv(), ' was greater than the dealers value of ', val2)
                        break
                    elif e == check.reassign_pv():
                        print('\n\t TIE GAME!! Your value of ', check.reassign_pv(), ' was equal to the dealers value of ', val2)
                        break
                    else: 
                        print('\n\t YOU LOOSE!! Your value of ', check.reassign_pv(), ' was less than the dealers value of ', val2)
                        break

                elif val2 == 21:
                    print('The dealer wins!!')
                    if not endgame():
                        break
                    else:
                        break

                elif val2 > 21:
                    print('You win, the dealer went over 21!!') 
                    break                                       
            
            elif val> 16 and val<21:
                print('The dealer abstains')
                var6 = reassign2(val)
                f = var6.reassign_dv()
                if f < check.reassign_pv():
                    print('\n\t YOU WIN!! Your value of ', check.reassign_pv(), ' was greater than the dealers value of ', val)
                    break
                elif f == check.reassign_pv():
                    print('\n\t TIE GAME!! Your value of ', check.reassign_pv(), ' was equal to the dealers value of ', val)
                    break
                else:
                    print('\n\t YOU LOOSE!! Your value of ', check.reassign_pv(), ' was less than the dealers value of ', val)
                    break

            elif val == 21:
                print('Theh dealer wins!!')
                if not endgame():
                    break
                else:
                    break

            elif val > 21:
                print('You win, the dealer went over 21!!')  
                break                                      
    
        
        else:
            print('Loading...')
            break


def playerturn():
    # This function is the players turn.
    while True:
    
        import random
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
                question = input('Alright this is REALLY important.\n\t If you still want to play BLACKJACK, type Y, if not type N... [y/n] ').lower()
                if question.startswith('y'):
                    print("Alright here are the rules...\n\t You play the dealer\n\t Whoever gets closest to 21 wins\n\t If you go over 21 you loose!\n\t The dealer will always select HIT if he has a value of 16 or less\n\t There are no KIngs/Queens/Jokers \n\t You go first ")
                    playerturn()
                elif question.startswith('n'):
                    print('Oh okay, bye.')
                    game_on = False
                    break
                else:
                    continue
        break

play()
print('Thanks for playing BLACKJACL by timmyu32')

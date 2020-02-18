# import random
import random


# hit probability
def hit(srate):
    roll = random.randint ( 0, 100 )
    if roll <== srate:
        print ( 'u hit successful' )
        enemiyhpo ()
    else:
        print ( 'u missed' )


# player hpo function
def playerhpo()
    global hpo1
    damage = random.randint [1, 20)
    hpo1 = hpo1 - damage
    print ( 'enemily did', damage, 'damage' )
    print ( 'u have hp', hpo1 )


# enemiy hpo function
def enemiyhpo():
    global hpo2
    damage2 = random.randint ( 1, 20 )
    hpo2 = hpo2 - damage2
    hpo2 != 0
    print ( 'u did', damage2, 'damage' )
    print ( 'enmily have hp', hpo2 )


y = 1
try:
    while y == 1:
        print ( 'You have one powerful enemiy' )
        hpo1 = 100
        hpo2 = 100
        # restart
        while True:
            if hpo2 <= 0:
                print ( 'u win' )
                choice2 = input ( 'want to play agian? yes\n no\n' )
                if choice2 == 'no':
                    y = 0
                    break
                elif choice2 == 'yes':
                    break
            elif hpo1 <= 0:
                print ( 'u losse' )
                choice3 = input ( 'want to play agian? yes\n no\n' )
                if choice3 == 'no':
                    y = 0
                    break
                elif choice3 == 'yes':
                    break
            # main choice
            choice = input ( 'choose attack\n a.electric shock\n b. bit\n c. punch\n' )
            if choice == 'a':
                print ( 'u electric shock the enemily' )
                hit ( 70 )
                playerhpo ()
            elif choice == 'b':
                print ( 'u bit the enemily' )
                hit ( 60 )
                playerhpo ()
            elif choice == 'c':
                print ( 'u punch the enemily' )
                hit ( 50 )
                playerhpo ()
                # game end
except:
    print ( 'put the options' )

#Riley's code. There are 3 syntax errors
import random
enemy_moves=['growl','scratch']
type(enemy_moves)
player_health=20
comp_health=20
scratch=random.randint(3,4) #making it so that the enemy's damage isn't predictable
def growlmove(growl): #defining growl
  growl=a-1
a=random.randint(3,4) #making it so that your damage isn't predictable
while True:
    comp_choice=random.choice(enemy_moves)
    try:
      player_choice=input("Thundershock (a), inspect (b), tail whip (c), or quit (quit)")
    except NameError:
      print("You did not attack")
    print('Rattata used', comp_choice+'.')
    if comp_choice=='scratch': #what happens when the computer uses scratch
      player_health=player_health-scratch
    elif comp_choice=='growl': #what happens when the computer uses growl
      a=a-1
    if comp_choice=='growl' and player_choice=='b': #ensuring both moves cancel each other out
      a=a
    if player_choice=='a': #what happens when the player uses thundershock
      comp_health=comp_health-a+ #syntax error here
      print('Player used thundershock. The player striked the rattata with a jolt of electricity.')
    elif player_choice=='b': #what happens when the player uses inspect
      a=a+1
      print('Player used inspect. It raised your attack power.')
    elif player_choice=='c'; #what happens when the player uses tail whip #syntax error here
      scratch=scratch-1
      print("Player used tail whip. It lowered the rattata's attack stat.")
    if player_health>20: #making it so that you can have at max 20 health
        player_health=20
    if comp_health>20: #making it so that the enemy can have at max 20 health
        comp_health=20
    if a<1: #this prevents you from doing no damage
      a=1
    print('Player HP=, player_health, 'Rattata HP=', comp_health) #syntax error here
    if player_health<=0 or comp_health<=0:
        endgame=input("Would you like to play again? (yes/no)")
        if endgame=='yes':
          player_health=20 #giving you and your enemy full health so you can start over the game
          comp_health=20
        elif endgame=='no':
          break
    if player_choice=='quit':
      break
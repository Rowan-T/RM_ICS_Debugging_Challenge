# Riley Parris
import random
enemy_moves=['growl','scratch']
type(enemy_moves)
player_health=20
comp_health=20
scratch=4
a=4
while True:
    comp_choice=random.choice(enemy_moves)
    player_choice=input("Thundershock (a), inspect (b), or tail whip (c)")
    print(comp_choice)
    if player_choice=='a' and comp_choice=='scratch':
        player_health=player_health-scratch
        comp_health=comp_health-a
        print('Player HP=', player_health, 'Rattata HP=', comp_halth) # <-runtime error. Supposed to print the computer player's health
    elif player_choice=='a' and comp_choice=='growl':
        a=a-1
        comp_health=comp_health-a
        print('Player HP=', player_health, 'Rattata HP=', comp_health)
    elif player_choice=='b' and comp_choice=='scratch':
        a=a+1
        player_health=player_health-scratch
        print('Player HP=', player_health, 'Rattata HP=', comp_health)
    elif player_choice=='b' and comp_choice=='growl':
        print('Player HP=', player_health, 'Rattata HP=', comp_health)
    elif player_choice=='c' and comp_choice=='scratch':
        scratch=scratch-1
        player_health=player_health-scratch
        print('Player HP=', player_health, 'Rattata HP=', comp_health)
    elif player_choice=='c' and comp_choice=='growl':
        scratch=scratch-1
        a=a-1
        print('Player HP=', player_health, 'Rattata HP=', comp_health)
    if a<1:
        a==1
    if player_health>20:
        player_health==20
    if comp_health>20:
        comp_health==20
    if player_health<=0 or comp_health<=0:
        break
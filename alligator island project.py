print(r'''        888888d8b                888                   
        888888Y8P                888                   
        888888                   888                   
 8888b. 888888888 .d88b.  8888b. 888888 .d88b. 888d888 
    "88b888888888d88P"88b    "88b888   d88""88b888P"   
.d888888888888888888  888.d888888888   888  888888     
888  888888888888Y88b 888888  888Y88b. Y88..88P888     
"Y888888888888888 "Y88888"Y888888 "Y888 "Y88P" 888     
                      888                              
                 Y8b d88P                              
                  "Y88P"    ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('In first you should inert your direction')
direction = input ('in first insert your direction for begin: ?')
if direction == 'L':
    print("you're going in left")
    movement = input ('make a movement for progress in the treasure trip')
    if direction == 'L' and movement == 'wait':
        print ('Nice job you arrived behind a door')
    else:
        print('attacked by trout game-over')
    door = input('choose the color of the door do you want to take: ')
    if direction == "L" and movement == 'wait' and door == "blue":
            print('Eaten by beasts game over')
    elif direction == "L" and movement == 'wait' and door == "red":
            print('Burned by fire Game Over')
    elif direction == "L" and movement == 'wait' and door == "yellow":
            print('You win')
    else:
        print('Game Over')
else :
    print('Fall into a hole: Game-over')

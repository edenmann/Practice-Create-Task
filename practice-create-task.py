# pokemon battle like game

# format: [name, health, strength, type, vulnerability]
fire_dog = ["Fire Dog", 160, 60, "fire", "water"]
water_gun = ["Water Gun", 240, 50, "water", "electric"]
car_battery = ["Car Battery", 120, 70, "electric", "nature"]
wisdom_tree = ["Wisdom Tree", 400, 30, "nature", "fire"]

print("Available Creatures: fire dog, water gun, car battery, wisdom tree.")
print("Certain elements deal more damage to vulnerable elements. ex: Fire dog does more damage to Wisdom Tree")
print("")

# assigns a creature to a player
def pick_creature(player):
    choice = input("Player " + str(player) + " what creature whould you like to pick? ")
    
    if choice == "fire dog":
        creature = fire_dog
    elif choice == "water gun":
        creature = water_gun
    elif choice == "car battery":
        creature = car_battery
    elif choice == "wisdom tree":
        creature = wisdom_tree
        
    return creature

#c1 stands for creature 1
c1 = pick_creature(1)
c2 = pick_creature(2)

# determines what each action does
def turns(player, choice):
    if player == 1:
        creature = c1
        enemy = c2
    elif player == 2:
        creature = c2
        enemy = c1

    # vulnerability properties
    if creature[3] == enemy[4]:
        damage = creature[2] * 1.5
    else:
        damage = creature[2]

    # attack
    if choice == "attack":
        enemy[1] -= damage
    # special
    elif choice == "special":
        damage *= 2
        enemy[1] -= damage

    print(enemy[0], "takes", str(damage), "damage")
    return enemy
        
# asks players what action they want to take 
# determines winner if health is below 0
def battle(c1, c2):
    print(c1[0], "(Player 1) is fighting", c2[0], "(Player 2).")
    print("Available Actions: attack, special")
    print("special does 2x normal damage")
    print("")

    while c1[1] > 0 and c2[1] > 0:

        print("")
        print("STATUS:")
        print("Player 1 has ", str(c1[1]), "health")
        print("Player 2 has ", str(c2[1]), "health")
        print("")

        p1 = input("Player 1, what would you like to do? (options: attack, special) ")
        p2 = input("Player 2, what would you like to do? (options: attack, special) ")
        print("")

        c2 = turns(1, p1)
        if c2[1] <= 0:
            print(c2[0] + " falls, Player 1 wins")
            break

        c1 = turns(2, p2)
        if c1[1] <= 0:
            print(c1[0] + " falls, player 2 wins")
            break

        

battle(c1, c2)
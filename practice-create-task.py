# pokemon battle like game

# format: [name, health, strength, type, vulnerability]
fire_dog = ["Fire Dog", 80, 60, "fire", "water"]
water_gun = ["Water Gun", 120, 50, "water", "electric"]
car_battery = ["Car Battery", 60, 70, "electric", "nature"]
wisdom_tree = ["Wisdom Tree", 200, 30, "nature", "fire"]

print("Available Creatures: fire dog, water gun, car battery, wisdom tree.")
print("Certain elements deal more damage to vulnerable elements. ex: Fire dog does more damage to Wisdom Tree")

#c1 stands for creature 1
def pick_creature(player):
    choice = input("Player", str(player), "what creature whould you like to pick? ")
    #p2 = input("Player 2, what creature whould you like to pick? ")

    if choice == "fire dog":
        creature = fire_dog
    elif coice == "water gun":
        creature = water_gun
    elif choice == "car battery":
        creature = car_battery
    elif choice == "wisdom tree":
        creature = wisdom_tree

    # if p2 == "fire dog":
    #     c2 = fire_dog
    # elif p2 == "water gun":
    #     c2 = water_gun
    # elif p2 == "car battery":
    #     c2 = car_battery
    # elif p2 == "wisdom tree":
    #     c2 = wisdom_tree
        
    return creature

    c1 = pick_creature(1)
    c2 = pick_creature(2)

def turns(player, choice):
    if player == 1:
        creature = c1
        enemy = c2
    elif player == 2:
        creature = c2
        enemy = c1

    # vulnerability properties
    if creature[3] == enemy[4]:
        damage = creature[2] * 1.2
    else:
        damage = creature[2]

    # attack
    if choice == "attack":
        enemy[1] -= damage
    # special
    elif choice == "special":
        enemy[1] -= damage * 2
    # block
    elif choice == "block":
        creature[1] = creature[1]
        blocked = True
        return blocked

    print(enemy[0], "takes", str(damage), "damage")
    return enemy
        

def battle(c1, c2):
    print(c1[0], "(Player 1) is fighting", c2[0], "(Player 2).")
    print("Available Actions: attack, special, block")
    print("special has 2 uses but does 2x normal damage")



    while c1[1] > 0 and c2[1] > 0:
        p1 = input("What would you like to do? (options: attack, special, block)")
        p2 = input("What would you like to do? (options: attack, special, block)")

        c2 = turns(1, p1)
        c1 = turns(2, p2)

        print("STATUS:")
        print("player 1 health -", str(c1[1]))
        print("player 2 health -", str(c2[1]))
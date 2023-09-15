# pokemon battle like game

# format: [name, health, strength, type, vulnerability]
fire_dog = ["Fire Dog", 80, 60, "fire", "water"]
water_gun = ["Water Gun", 120, 50, "water", "electric"]
car_battery = ["Car Battery", 60, 70, "electric", "nature"]
wisdom_tree = ["Wisdom Tree", 200, 30, "nature", "fire"]

print("Available Creatures: fire dog, water gun, car battery, wisdom tree.")

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

def battle(c1, c2):
    print(c1[0], "(Player 1) is fighting", c2[0], "(Player 2).")
    print("Available Actions: attack, special, block")
    while game_status == True:
        while c1[1] > 0 and c2[1] > 0:
        p1 = input("What would you like to do? (options: attack, special, block)")
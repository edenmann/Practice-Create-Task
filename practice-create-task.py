# pokemon battle like game

# format: [name, health, strength, type, vulnerability]
red = ["fire dog", 80, 60, "fire", "water"]
blue = ["water gun", 120, 50, "water", "electric"]
yellow = ["car battery", 60, 70, "electric", "nature"]
green = ["wisdom tree", 200, 30, "nature", "fire"]

print("Available Creatures: red, blue, yellow, green.")

#c1 = creature 1
def pick_creature():
    p1 = input("Player 1, what creature whould you like to pick? ")
    #p2 = input("Player 2, what creature whould you like to pick? ")

    if p1 == "red":
        c1 = red
    elif p1 == "blue":
        


    return c1, c2

def battle(c1, c2):

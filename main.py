# forged in fire

# Forging weapons, and armor, and other household medieval items that you would create in a forge
# Crafting functions
# Invenotry
# Crafting rules

commands = {
    "i" : "see inventory",
    "c" : "see crafting options",
    "craft" : "craft something from inventory items",

}
# list of items you start with
items = {
    "wood" : 500,
    "stone" : 250,
    "iron" : 100,
    "steel" : 100,
    "silver" : 50,
    "gold" : 20,
    "hungarium" : 10,
    "diamond" : 2
}

craft = {
    "cast iron tea kettle" : { "iron" : 3 },
    "iron dagger" : { "iron" : 3 },
    "iron tongs" : { "iron" : 1 },
    "torch" : { "wood" : 1 },
    "steel kodachi" : { "steel" : 4 },
    "steel battleaxe" : { "steel" : 8 },
    "silver broadsword" : { "silver" : 6 },
    "vampire slayer" : { "silver" : 12 },
    "gold earring" : { "gold" : 1 },
    "gold chain" : { "gold" : 5 },
    "hungarian breastplate" : { "hungarium" : "10" },
    "diamond ring" : { "diamond" : 1 },

}


# welcome screen
print("▬▬|═══════ﺤ Welcome to Forged In Fire -════ι▬")
print("           *O*")
print("           |X|_")
print("           |X||-------________________________________________")
print(",O---------+X| \___   `=------------------------------- ______\ ")
print("`O---------+X| /      ,=-------------------------------'      /")
print("           |X||-------~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("           |X|~")
print("           |X|~")
print("Start Game by typing ? for options")

while True:
    command = input(">").split()
    if len(command) == 0:
        continue
    if len(command) > 0:
        verb = command[0].lower()
    # The problem is when you have item of multiple words e.g. iron dagger; you need to join them
    if len(command) > 1:
        item = ' '.join(x.lower() for x in command[1:])
    if verb == "?":
        for key in commands:
            print(key + " : " + commands[key])
        print("\n")
    elif verb == "i":
        for key in items:
            print(key + " : " + str(items[key]))
        print("\n")
    elif verb == "c":
        for key in craft:
            print(key + " can be made with:")
            for i in craft[key]:
                print(str(craft[key][i]) + " " + i)
            print("\n")
            
    elif verb == "craft":
        print("making " + item + ":") 
        if item in craft:
            for i in craft[item]:
                print("  you need : " + str(craft[item][i]) + " " + i + " and you have " + str(items[i]))
            craftpossible = True
            for i in craft[item]:
                if craft[item][i] > items[i]:
                    print("item cannot be crafted\n")
                    craftpossible = False
                    break
            
            if craftpossible == True:
                for i in craft[item]:
                    items[i] -= craft[item][i]
                # Check if the item exists and update it
                if item in items:
                    items[item] += 1
                else: # or create it if it does not exist
                    items[item] = 1
                print("item crafted\n")

            if "iron dagger" in items and "gold chain" in items: # check the items exists
                if items["iron dagger"] >=1 and items["gold chain"] >=1: # check their value
                    print("o==[]::::::::::::::::>  You are a Hero! <::::::::::::::::[]==o")
                    break
        else:
            print("keep crafting")
    else:
        print("keep crafting")


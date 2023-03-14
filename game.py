import random
from enum import Enum

Event = Enum('Event', ['Chest', 'Nothing'])

events = {
    Event.Chest: 0.5,
    Event.Nothing: 0.5
    }

Colour = Enum('Colour', {'white': 'shit',
                         'green': 'something a bit better than shit',
                         'blue': 'usefull',
                         'gold': 'actually good equip'
                         })

colours = {
    Colour.white: 0.4,
    Colour.green: 0.3,
    Colour.blue: 0.25,
    Colour.gold: 0.05
    }

eventList = list(events.keys())
eventProb = list(events.values())

colourList = list(colours.keys())
colourProb = list(colours.values())

yourRewards = {
    colourList[reward]: (reward + 1) * (reward + 1) * 1000
    for reward in range(len(colourList))
    }

gameLen = 5
goldFrom = 0

print("Welcome in my dungeon, man.")
print("Open boxes or give me 300 bucks!")
print("Do not have 300 bucks? So, you will have a long night instead...")
print("Or you can open my lootboxes. You agree?")

choise = input("Yes or No:")
if choise == "Yes":
    print("That's a RIGHT choise, man!")
else:
    print("You want know more about devices in my dungeon, don't you? C'mon!")

while gameLen > 0:
    answer = input("Do you want to go forward?")
    if answer == "Yes":
        print("Good, let see what you got!")
            
        yourEvent = random.choices(eventList, eventProb)[0]
        if yourEvent == Event.Chest:
            print("Yeah, you got the chest, man!")
            yourChest = random.choices(colourList, colourProb)[0]
            print("The chest colour is", yourChest)
            print("You got", yourChest.value, ", man")
            gamerReward = yourRewards[yourChest]
            goldFrom = goldFrom + gamerReward
        elif yourEvent == Event.Nothing:
                print("On no! You must try more time. Or pay 300 bucks!")
        
    else:
        print("Are you sure? Lootboxes are waiting for you! Let's go, man!")

gameLen = gameLen - 1

print("Well, you got", goldFrom)

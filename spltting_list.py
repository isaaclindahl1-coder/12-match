import random
mystr = "This is a sentence about the hobgoblin Jace"
list_of_words = mystr.split() #if we specife nothing, it will split on " "
print(list_of_words)
list_of_words[-1] = "Mykyta"
print(list_of_words)
mystr = " ".join(list_of_words)
print(mystr)
#simulated csv (comma seperated values)
str2 = "name,type,streangth,health"
p1 = "zach, orc,5,10"
p2 = "isaac,loot goblin,2,6"
headers = str2.split(",")
p1list = p1.split(",")
p2list = p1.split(",")


#iterate through p1list with index and values (with enumerate)
for idx, val in enumerate(p1list):
    print(f"{headers[idx]}: {val}")

for idx, val in enumerate(p2list):
    print(f"{headers[idx]}: {val}")

playerlists = [p1list,]
print(f"it's the big battle of {p1list[0]} the {p1list[1]} vs {p2list[0]} the {p2list[1]}!")
for i in range(5):
    print(f"Round {i+1}")
    choice = random.radont(0,2)
    if choice < 2:
        attacker = playerlists[choice]
        defender = playerlists[1-choice]
        print(f"{attacker[0]} delivered {attacker[2]} damage to {defender[0]} and")
    else:
        outcomes.append
        
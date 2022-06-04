from random import choice #DON'T CHANGE!

user = {
    "name": "Darryl",
    "occupation": "Engineer",
    "age": 31,
}

"31" in user.values()

for k,v in user.items():
    print(f"key is {k} and the value is {v}")

"address" in user

user.clear()

print(user)

# This code picks a random food item:

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if bakery_stock.get(food) != None:
    print(f"{bakery_stock.get(food)} items of {food} still in inventory.")
else:
    print("We don't make that")
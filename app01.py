"""
A dictionary is one of four main collection types
Main collection types:
- List: A container that can hold numberous items, editable, ordered [item1, item2, item3]
- Dictionaries: A container that can hold numberous key/value pairs, each key connects to a value {"klins": 89, "winchell": 85}
- Tuples: A container that can hold numberous items, not editable, ordered(item1, item2, item3)
- Set: A continer that can hold numberous UNIQUE items, editable in the form of add/remove (item), not ordered, editable, {item1, item2, item3}
"""

zachs_capitals = {
    "Pennsylvania": "Allentown",
    "Texas": "Dallas",
    "Flordia": "Miami",
    "New York": "Jamestown",
    "Wisconsin": "Madison"
}

# print(dir(zachs_capitals)) # Lists all avaliable dictionary methods
# help(zachs_capitals)

# Accessing Values:
print(zachs_capitals["Flordia"])
#print(zachs_capitals{"Ohio"}) #Uh-Oh! Key-error - "Ohio"
# We can safely try to access a value by an uncomfirmed key with .get
print(zachs_capitals.get("Ohio")) #Returns None

print(zachs_capitals["Ohio"] if "Ohio" in zachs_capitals else "Not Found")
print(zachs_capitals["Flordia"]
    if "Flordia" in zachs_capitals else "Not Found")

#Let's fix zachs_capitals:
#zachs_capitals["Wisonsin"] = "Green Bay"

zachs_capitals.update({"Wisconsin": "Madison"}) #Either update an existing record, or create a new one
zachs_capitals.update({"Ohio": "Ashtabula"}) #Either update an existing record, or create a new one
print(zachs_capitals)

# If statement to handle if key exists:
if zachs_capitals.get("OHIO"): #Not the same as "Ohio"
    #a bunch of code if you want
    print(zachs_capitals["Ohio"])
else:
    print("Not found in the dictionary")

# Remove items:
zachs_capitals.__delitem__("Ohio") #generally want to avoid dunder methods, unless overriding them
print(zachs_capitals)
# More common approach:
zachs_capitals.pop("Texas")
print(zachs_capitals)

# Empty the dictionary
# zachs_capitals.clear()
# print(zachs_capitals)

# Getting all keys, values or both in a dictionary:
print(zachs_capitals.keys()) #looks like a list, but is a "dictionary view object", but you can iterate over it
for key in zachs_capitals.keys(): #iterate over the keys
    print(key)
print(zachs_capitals.values()) #gives back a dictionary values object, also iterable
for value in zachs_capitals.values():
    print(value)

print("\nWhat's this?")
for item in zachs_capitals:
    print(zachs_capitals[item], item)

# We want to iterate over all keys and values
# for key, value in dict.items()
for state, capital in zachs_capitals.items():
    print(f"{capital}, {state}")

# Find a key by it's value:
# Look up the key for the value "Allentown", if not found, print not found:
for key, value in zachs_capitals.items():
    if value == "Allentown":
        print(key)
        break
else:
    print("Not found")
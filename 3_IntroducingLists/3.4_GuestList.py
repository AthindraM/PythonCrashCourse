guests = ["Abraham Lincoln", "John F Kennedy", "George Washington"]

print(f"{guests[0]}, you're invited to my dinner party!")
print(f"{guests[1]}, you're invited to my dinner party!")
print(f"{guests[2]}, you're invited to my dinner party!")

# 3.5 Changing Guest list
popped_guest = guests.pop()
print(f"It seems like {popped_guest} won't be able to make it to the party :(")

guests.append("Thomas Jefferson")

print(f"{guests[0]}, you're invited to my dinner party!")
print(f"{guests[1]}, you're invited to my dinner party!")
print(f"{guests[2]}, you're invited to my dinner party!")

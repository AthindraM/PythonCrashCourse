# 3.4 Guest List
guests = ["Abraham Lincoln", "John F Kennedy", "George Washington"]

print(f"{guests[0]}, you're invited to my dinner party!")
print(f"{guests[1]}, you're invited to my dinner party!")
print(f"{guests[2]}, you're invited to my dinner party!\n")

# 3.5 Changing Guest list
popped_guest = guests.pop()
print(f"It seems like {popped_guest} won't be able to make it to the party :(\n")

guests.append("Thomas Jefferson")

print(f"{guests[0]}, you're invited to my dinner party!")
print(f"{guests[1]}, you're invited to my dinner party!")
print(f"{guests[2]}, you're invited to my dinner party!\n")

# 3.6 More Guests
print("Great news! I found a bigger dinner table, so I'll be inviting more guests to my party!\n")

guests.insert(0, "Franklin D. Roosevelt")
guests.insert(2, "George W. Bush")
guests.append("Ronald Reagan")

print(f"{guests[0]}, you're invited to my dinner party!")
print(f"{guests[1]}, you're invited to my dinner party!")
print(f"{guests[2]}, you're invited to my dinner party!")
print(f"{guests[3]}, you're invited to my dinner party!")
print(f"{guests[4]}, you're invited to my dinner party!")
print(f"{guests[5]}, you're invited to my dinner party!\n")

# 3-4: guest list
guests = ['person1', 'person2', 'person3']
for guest in guests:
    print("Hello {g}".format(g=guest)) # works in all python versions
    print(f'Hello {guest}.') # works only in python 3.6+



# 3-5 changing guest list
guests[2] = 'new_person3'
for guest in guests:
    print(f"Hello {guest}.")


# 3-6 more guests

guests.insert(0,'jane')
guests.insert(2,'sarah')
guests.append('sal')

for guest in guests:
    print(f"Hello {guest}.")



# 3-7 shrinking guest list

print("I can invite only two people for dinner this time.")
while len(guests) > 2:
    print(f"I am sorry I could not invite you this time, {guests.pop()}.")

for guest in guests:
    print(f"You are still invited, {guest}.")

del guests[1]
del guests[0]
print(guests)

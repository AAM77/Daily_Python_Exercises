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

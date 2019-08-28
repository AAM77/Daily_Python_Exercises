# 3-4: guest list
guests = ['person1', 'person2', 'person3']
for guest in guests:
    print("Hello {g}".format(g=guest)) # works in all python versions
    print(f'Hello {guest}.') # works only in python 3.6+

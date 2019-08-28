# notes

# sort() destructively sorts the original array
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(f"orig list after sort(): {cars}\n")

cars.sort(reverse=True)
print(f"orig list after sort(reverse=True): {cars}\n")

# sorted() is the non-destructive version of sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"using sorted(): {sorted(cars)}")
print(f"orig list: {cars}\n")

sorted(cars, reverse=True)
print(f"using sorted(): {sorted(cars, reverse=True)}")
print(f"orig list: {cars}\n")


# reversing a list's order of items whether sorted or not
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"cars w/ reverse(): {cars.reverse()} ~> reverse(): nothing returned, but destructive")
print(f"original cars list: {cars}\n")

# finding the length using '  len( [list] )  '
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(f"length of the list / # items in list: {len(cars)}\n\n\n\n\n")

# EXERCISES

# 3-8: seeing the world (use sorted(), sorted(list, reverse=True), reverse(), sort(), & sort(reverse=True))
places = ['new zealand', 'pakistan', 'mecca', 'madina', 'alaska', 'australia', 'switzerland', 'canada']
print(f"original: {places}\n")

print(f"w/ sorted(): {sorted(places)}")
print(f"current list order: {places}\n")

print(f"w/ sorted() & reverse=True: {sorted(places, reverse=True)}")
print(f"current list order: {places}\n")

places.reverse()
print(f"current list (after x1 reverse()): {places}\n")

places.reverse()
print(f"current list (after x2 reverse()): {places}\n")

places.sort()
print(f"current list (after sort()): {places}\n")

places.sort(reverse=True)
print(f"current list (after sort(reverse=True)): {places}\n")

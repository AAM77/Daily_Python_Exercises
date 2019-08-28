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
print(f"length of the list / # items in list: {len(cars)}")

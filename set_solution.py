set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set()
intersection = set()

# Add code here to get the difference of set1 to set2. Then print to the screen.
print('difference of set1 to set2 is: ')
set1_difference = set1 - set2
print(set1_difference)
# Add code here to get the differe ce of set2 to set1. Then print to the screen.
print('difference of set2 to set1 is: ')
set2_difference = set2 - set1
print(set2_difference)

# Add code here for union
for item in set1:
    union.add(item)
for item in set2:
    union.add(item)
print('Yay you got rid of the duplicates! Here is the new set for your inventory: ')
print(union)
# Add code here for intersection
for another_item in set1:
    if another_item in set2:
        intersection.add(another_item)
print('Here are the duplicates. Please start selling more products.')
print(intersection)

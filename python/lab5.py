# 1. List Operations
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")

# II. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(f"Ages after adding min and max: {ages}")

# III. Find the median age
length = len(ages)
median_age = (ages[length // 2 - 1] + ages[length // 2]) / 2 if length % 2 == 0 else ages[length // 2]
print(f"Median age: {median_age}")

# IV. Find the average age
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

# V. Find the range of the ages
age_range = max_age - min_age
print(f"Range of ages: {age_range}")

# VI. Compare the value of (min - average) and (max - average), use _abs()_ method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(f"Min diff: {min_diff}, Max diff: {max_diff}")

# 2. Iterate through the list and print items
items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)
# 3. Tuple and List Operations
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "potato", "cabbage")
animal_products = ("milk", "eggs", "meat")

# I. Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products
print(f"Combined tuple: {food_stuff_tp}")

# II. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print(f"Converted list: {food_stuff_lt}")

# III. Slice out the middle item or items
middle = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle-1:middle+1]
else:
    middle_items = food_stuff_lt[middle]
print(f"Middle item(s): {middle_items}")

# IV. Slice out the first three and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"First three items: {first_three}, Last three items: {last_three}")

# V. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 4. Set Operations
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Length of the set it_companies
print(f"Length of it_companies: {len(it_companies)}")

# II. Add 'Twitter'
it_companies.add('Twitter')

# III. Insert multiple IT companies
it_companies.update(['Tesla', 'Netflix', 'Uber'])

# IV. Remove one company
it_companies.remove('IBM')

# V. Difference between remove and discard
# Remove throws an error if item not found, discard does not.

# Set operations between A and B
# I. Join A and B
A_B_union = A.union(B)
print(f"Union of A and B: {A_B_union}")

# II. Find A intersection B
A_B_intersection = A.intersection(B)
print(f"Intersection of A and B: {A_B_intersection}")

# III. Is A subset of B
is_subset = A.issubset(B)
print(f"Is A a subset of B: {is_subset}")

# IV. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets: {are_disjoint}")

# V. Symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {sym_diff}")

# VI. Delete sets
del A, B


# 8. Print season name based on month number
month_to_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

def get_season(month_number):
    return month_to_season.get(month_number, "Invalid month number")

print(get_season(5))  
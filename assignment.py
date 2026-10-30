
def replace_value(values, index, new_value):
    values[index] = new_value
    return None
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
def summarize(values):
    return (min(values), max(values), sum(values))
days = int(input("Enter the number of days: "))
original = []
for i in range(days):
    hours = int(input(f"Enter machine use time in hours: {i + 1}: "))
    original.append(hours)
updated = original[:]
index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of hours: "))
replace_value(updated, index, new_value)
target = int(input("Enter the number of hours to search for: "))
first_index = find_first(updated, target)
count = updated.count(target)
minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum machine use time: {minimum}")
print(f"Maximum machine use time: {maximum}")
print(f"Total machine use time: {total}")
if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {count}")

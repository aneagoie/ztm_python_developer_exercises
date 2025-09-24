# Check for duplicates in the following list


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list = []
dupe_list = []

for i in some_list:
    if i not in new_list:
        new_list.append(i)
    else:
        dupe_list.append(i)

print(f'{dupe_list} are the duplicates in the list.')

# The instructor's solution

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


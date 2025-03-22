def smaller_numbers_than_current(numbers):
    unique_numbers = sorted(list(set(numbers))) 
    result = []
    for number in numbers:
        count = 0
        for unique_number in unique_numbers:
            if unique_number < number:
                count += 1
            else:
                break
        result.append(count)
    return result

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# The question says: When counting numbers, only count unique values. 
# That is, if a number occurs multiple times in the list, it should only be counted once.
# This may mean that when I see the word unique, it means use a set

# Comparing minimum numbers, maybe consider using sorted when I see this
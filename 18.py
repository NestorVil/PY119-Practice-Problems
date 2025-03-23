# P:
#   Input: A list (of integers)
#   Output: A number, representing the index for which all numbers with an index less than the output equals
#           the sum of the numbers greater than the output
#   [1, 2, 4, 4, 2, 3, 2]) == 3.   4 [1, 2, 4] [2, 3, 2]
#                                     7,        7
#   [7, 99, 51, -48, 0, 4]) == 1.  99 [7]    [51, -48, 0, 4]
#                                      7,    7
#   Rules:
#       Working with indexes
#       When checking each index, sum all the numbers for it, and sum all the numbers after it
#       Check both for equality
#       If there's no index that can make this happen, return -1
#       If given a list with multiple answers, return the index with the smallest value
#       The sum of numbers left of index 0 is 0, the sum of the numbers to the right of the last is 0
# E:
    # print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
    # print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
    # print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
    # print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

    # # The following test case could return 0 or 3. Since we're
    # # supposed to return the smallest correct index, the correct
    # # return value is 0.
    # print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
# D:
#   Indexes of a list
#   Finding sums
#   Comparing for equality ==
#   Creating and fidning a minimum value (a minimum of an index) (maybe store it in a list)
# A:
#   Create a 'tracker' variable and set it to 0
#   Iterate over the input_list while keeping track of indexes
#       Create a 'current_index' varabile and set it to the current index position in iteration
#       Create a 'first_half' variable and set it to all the numbers before 'current_index
#       Create a 'second_half' variable and set it to all the numbers after 'current_index'
#       Compare 'first_half' and second_half for equality
#           If equal: add 'current_index' to a new list 'checker_list
#   Find the minimum value within 'checker_list' and return it
#   If 'checker_list' is empty, return -1

def equal_sum_index(input_list):
    checker_list = []

    for idx, num in enumerate(input_list):
        first_half = input_list[:idx]
        last_half = input_list[idx + 1:]

        if sum(first_half) == sum(last_half):
            checker_list.append(idx)

    return min(checker_list) if checker_list else -1


print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
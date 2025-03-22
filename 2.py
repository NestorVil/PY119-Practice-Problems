# P:
#   Input: A list of integers
#   Output: Returning a number, which is the minimum sum of 5 consecutive numbers in input_list
#   Rules:
#       If the list contains fewer than 5 elements, return None
#       From the input_list, need to get every possible 5 consesuctive numbers (List of subslists)
#       [1, 2, 3, 4, 5, -5] -> [[1, 2, 3, 4, 5], [2, 3, 4, 5, -5]]
#       For each individual sublist, will need to find their sum and return the minimum of them
# E:
    # print(minimum_sum([1, 2, 3, 4]) is None)
    # print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
    # print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
    # print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
    # print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
# D:
#   Will need to create sublists, something like a "running sublist" starting from the first
#   element until it reaches 5, then starting from the next element until it reaches five ect...
#   Indexing and ranges
# A:
#   Create a new empty list 'returning_list' which will be populated by sublists
#   If the length of the 'input_list' is less than 5, return None
#   Starting from the first element of 'input_list', add the next four elements into a new sublist
#   Repeat ^ for the next element if it's possible to add four more
#   Add all of these sublists to 'returning_list'
#   For each sublistt in 'returning_list', find their sum and place it in a new list
#   Return the minimum number within that new_list
def other_function(numbers):
    return [numbers[idx] for idx in range(len(numbers[:5]))]

def minimum_sum(input_list):
    if len(input_list) < 5:
        return None
    
    returning_list = [other_function(input_list[idx:]) 
                      for idx in range(len(input_list))
                      if len(input_list[idx: idx + 5]) == 5]

    returning_list = [sum(sublist) for sublist in returning_list]

    return min(returning_list)

    


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
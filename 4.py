# P:
#   Input: A list of integers
#   Output: Returning a tuple, of two numbers that are closest in value
#   Rules:
#       If there are multiple pairs that are equally close, return the pair that occurs first
#           in the list
#       Creating a list of sublists where each sublist is each number placed together
#       [5, 25, 15, 11, 20] -> [[5, 25], [5, 15], [5, 11], [5, 20], [25, 15], [25, 11]...]
#       Once I have that list of sublists, will need to find the absolute value difference
#           between them, and find the one with the lowest number
#       Once I have that, return the associated index of the two numbers that have the lowest abs val
# E:
    # print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
    # print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
    # print(closest_numbers([12, 22, 7, 17]) == (12, 7))
# D:
#   A way to keep track of indexes of my list of sublists
#   A way to find the difference between each numbers in sublists, and find the minimum of them
# A:
#   For each number in 'input_list' pair it once with each other number in 'input_list'
#   Place each subtuple in a new list 'list_of_tupples'
#   While keeping track of the index of each pair in 'list_of_tuples'
#       Find the absolute value of each subtuple and palce it in a new list 'absolute_values'
#       Find the minimum number in 'absolute_values'
#   Find the associated index of where the minimum number of 'absolute_values' is and then return it
def closest_numbers(input_list):
    list_of_tuples = [(input_list[first_idx], input_list[second_index]) 
                      for first_idx in range(len(input_list))
                      for second_index in range(first_idx + 1, len(input_list))]

    absolute_values = [abs(subtuple[0] - subtuple[1]) for subtuple in list_of_tuples]
    minimum_value = min(absolute_values)
    minimum_value = absolute_values.index(minimum_value)
    return list_of_tuples[minimum_value]
s

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
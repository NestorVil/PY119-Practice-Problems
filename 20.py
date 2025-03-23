# P:
#   Input: A list (of numbers)
#   Output: A number, representing the number in the list that differs from all the rest
#   Rules:
#       The list will always contain at least 3 numbers, and exactly one number is different
#       Caring about uniqueness
# E:
    # print(what_is_different([0, 1, 0]) == 1)
    # print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
    # print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
    # print(what_is_different([3, 4, 4, 4]) == 3)
    # print(what_is_different([4, 4, 4, 3]) == 3)
# D:
#   Sets, or dictionaries
#   Dictionary, returning the number that only has 1 as a value
#   [0, 1, 0] -> 0: 2, 1: 1.   Returning 1 (value of 1)
# A:
#   Create a dictionary called "checker"
#   Populate "checker" with all the elements in the input list being a unique key, and its value being the 
#                                                                                   number of times it appears
#   Iterate through checker by keeping track of both the key, and value
#       If one of the values is 1, return the key

def what_is_different(input_list):
    # checker = {element: input_list.count(element) for element in input_list}
    checker = dict()

    for element in input_list:
        checker[element] = checker.get(element, 0) + 1

    for key, value in checker.items():
        if value == 1:
            return key

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
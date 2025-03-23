# P:
#   Input: A list of integers
#   Output: An integer, representing the number that appears an odd number of times
#   Rules:
#       There will always be exactly one integer in the input list that will appear an odd number of times
#       [7, 99, 7, 51, 99] == 51. 
#       Keep track if a number appears in the list multiple times
#       Returning the number that appears an odd amount of times
# E:
    # print(odd_fellow([4]) == 4)
    # print(odd_fellow([7, 99, 7, 51, 99]) == 51)
    # print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
    # print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
    # print(odd_fellow([0, 0, 0]) == 0)
# D:
#   A dictionary, or a simple count
#   7: 2, 99: 2, 51: 1. Search through the dictionary, find the value that is odd and return the key
# A:
#   Create a dictioanry variable named 'dictionary_checker'
#   Populate 'dictionary_checker' with each element of the input_list, with each element being the key
#                                                                           each value being the count
#   Iterate through dictionary_checker by checking both the keys, and the values
#       If the value is odd, return the key

def odd_fellow(input_list):
    dictionary_checker = {element: input_list.count(element) for element in input_list}
    
    for key, value in dictionary_checker.items():
        if value % 2 != 0:
            return key


    for element in input_list:
        if input_list.count(element) % 2 != 0:
            return element

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
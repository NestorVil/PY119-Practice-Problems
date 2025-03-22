# P:
#   Input: A string of digits
#   Output: A number, representing the amount of even-numbered substrings that can be formed
#   Rules:
#       Will need to split the input string into a list of substrings possible
#       '1432' ---> [[1], [14], [143], [1432], [4], [43], [432], [3], [32], [2]] ---> [[14], [1432], [4], [432] [32], [2]]
#       Once split the input string into a list of every substring possible, find which of those substrings are even
# E:
    # print(even_substrings('1432') == 6)
    # print(even_substrings('3145926') == 16)
    # print(even_substrings('2718281') == 16)
    # print(even_substrings('13579') == 0)
    # print(even_substrings('143232') == 12)
# D:
#   Workin with strings, integers, lists, and sublists
#   Once I hae my list of strings, will need to turn each sublist back into a number to check if its even
# A:
#   Create a 'possible_substrings' variable and set it to the possible substrings
#       1. Filter out all empty substrings from possible_substrings
#   Create an 'list_of_evens' variable and fill it with the sublists in 'possible_substrings' that are even
#   Return the length of 'list_of_evens'

def even_substrings(input_string):
    possible_substrings = [input_string[first_index:second_index + 1]
                           for first_index in range(len(input_string))
                            for second_index in range(first_index, len(input_string))]

    list_of_evens = [int(substring) for substring in possible_substrings if int(substring) % 2 == 0]

    return len(list_of_evens)


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

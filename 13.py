# P:
#   Input: Two strings
#   Output: A boolean value, depending on if some portion of the characters in the first string can be 
#           rearranged to match the characters in the second
#   Rules:
#       Both strings contain only lowercase letters, neither will be empty
#       Checking if some portion of the characters in the first string can match some characters in the second
# E:
    # print(unscramble('ansucchlohlo', 'launchschool') == True)
    # print(unscramble('phyarunstole', 'pythonrules') == True)
    # print(unscramble('phyarunstola', 'pythonrules') == False)
    # print(unscramble('boldface', 'coal') == True)
# D:
#   Working with strings, which are immutable
#   I can turn both into lists and then go from there
# A:
#   'possible_matching' variable and make it a sorted list (first argument)
#   'input_string' variable and make it a sorted list (second argument)
#   Create a copy of 'possible_matching' called 'copied_matching_string'
#   So long as input_string has value:
#       Iterate over 'possible_matching'
#           Remove the corresponding element of 'copied_matches'
#           If that element exists in input_string, remove it
#       If it's no longer possible to remove an element of possible_matching and input_list still has value
#           return False
#       Otherwise return True

def unscramble(first_string, second_string):
    possible_matching = list(first_string)
    input_string = list(second_string)

    copied_matching_string = possible_matching[:]

    while input_string:
        for chara in possible_matching:
            if len(copied_matching_string) == 0:
                return False

            popped_element = copied_matching_string.pop(0)

            if popped_element in input_string:
                input_string.remove(popped_element)

    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)


def can_be_rearranged(str1, str2):
    """
    Checks if some characters in str1 can be rearranged to match str2.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if a portion of str1 can be rearranged to match str2, False otherwise.
    """

    # Create a dictionary to store character counts in str1
    char_counts = {}
    for char in str1:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through str2 and decrement character counts in the dictionary
    for char in str2:
        if char in char_counts and char_counts[char] > 0:
            char_counts[char] -= 1
        else:
            return False

    # If all characters in str2 were found and decremented, return True
    return True
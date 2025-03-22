# P:
#   Input: A string
#   Output: returning a dictionary, where the keys represent the lowercase letters in the string,
#           and the values represent how often the corresponding letter occurs in the string
#   Rules:
#       Turning a string into a dictionary
#       Make each lowercase letter in the string a key
#       Count how often each lowercase letter appears in the input string
#       Make that count a value associated with its key
#       Possible for the input to contain no lowercase letters
#       Input will always be a string, but the string could be empty
# E:
    # expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
    # print(count_letters('woebegone') == expected)

    # expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
    #             'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
    # print(count_letters('lowercase/uppercase') == expected)

    # expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
    # print(count_letters('W. E. B. Du Bois') == expected)

    # print(count_letters('x') == {'x': 1})
    # print(count_letters('') == {})
    # print(count_letters('!!!') == {})
# D:
#   Strings are immutable
#   Need a way to segment the string(?) if needed
#   Returning a dictionary, will need a dictionary
# A:
#   Create an empty dictionary called 'returning_dictionary'
#   Create a new string called 'only_lowercase' which will have only the lowercase letters of the input
#   Iterate over 'only_lowercase'
#   for each character, add it as a key to 'returning_dictionary', if the key doesn't already exist, set its value to 1
#   if the key does already exist, add its value by 1
#   return the 'returning_dictionary'
def count_letters(input_string):
    returning_dictionary = dict()

    only_lowercase = "".join([chara for chara in input_string if chara.islower()])

    for chara in only_lowercase:
        #returning_dictionary.setdefault(chara, 0)
        #returning_dictionary[chara] += 1
        returning_dictionary[chara] = returning_dictionary.get(chara, 0) + 1   # The above two lines work too
    
    return returning_dictionary
    


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
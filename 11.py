# P:
#   Input: A non-empty string
#   Output: A tuple, containing a string and an integer.
#   Rules:
#       The string component of the tuple should be multiplied by the integer component of the tuple
#       ("string", number) -> 'string' * number == input_string
#       The values of 'string' and number should be the shortest possible substring and the largest possible repeat count
# E:
    # print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
    # print(repeated_substring('xyxy') == ('xy', 2))
    # print(repeated_substring('xyz') == ('xyz', 1))
    # print(repeated_substring('aaaaaaaa') == ('a', 8))
    # print(repeated_substring('superduper') == ('superduper', 1))
# D:
#   Dealing with string concatenation 
#   Returning a tuple, (string, number) such that string * number == input
# A:
#   'possible_number' variable and set it equal to 1
#   'possible_substring' variable and set it to an empty string
#   Iterate over 'input_string'
#   For each iteration, add that character to 'possible_substring'
#       If possible_substring * possible_number == 'input_string
#           return 'possible_substring', possible_number as a tuple
#       if not
#           add 1 to possible_number and continue iterating

#   Create a list of 'possible_substrings' and fill it with possible substrings
#   Iterate over that list
#   For each iteration multiply each element by count (originally 1) and check for equality with input_string
#   If I make it through the entire iteration and none are checked, add 1 to count, and repeat the iteration




def repeated_substring(input_string):
    running_chara = ''

    for chara in input_string:
        running_chara += chara

        for number in range(len(input_string) + 1):
            if running_chara * number == input_string:
                return running_chara, number

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))



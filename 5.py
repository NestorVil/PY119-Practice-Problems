# P:
#   Input: A string
#   Output: A character, which is the character that occurs most often in the string
#   Rules:
#       If there are multiple characters with the same greatest frequency, return the one that appears first in the string
#       Consider lowercase and uppercase characters to be the same
#       Input strings won't be empty
#       Input string can be multiple words or single word
#       Keep track of how many times each character is in the word
#       If one character is more common than the last, make that the new highest character
# E:
    # print(most_common_char('Hello World') == 'l')
    # print(most_common_char('Mississippi') == 'i')
    # print(most_common_char('Happy birthday!') == 'h')
    # print(most_common_char('aaaaaAAAA') == 'a')

    # my_str = 'Peter Piper picked a peck of pickled peppers.'
    # print(most_common_char(my_str) == 'p')

    # my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
    # print(most_common_char(my_str) == 'e')
# D:
#   A way to keep track of how many times a character is in the string
#   A way to make every character in the string the same case 
#   Strings are immutable (im working with strings)
# A:
#   lower case the entire input_string and place it in a new variable 'lower_case_string'
#   create a 'count' variable and set it to 0
#   create a 'highest_letter' variable and make it an empty string
#   iterate over the 'lower_case_string'
#       for each character how count how many times that character appears in the entire 'lower_case_string'
#           if the count is bigger than 'count'
#               make the count equal that, and make the 'highest_letter' equal that character
#   return 'highest_letter'
def most_common_char(input_string):
    lower_case_string = input_string.lower()
    count = 0
    highest_letter = ''

    for chara in lower_case_string:
        current_count = lower_case_string.count(chara)
        if current_count > count:
            count = current_count
            highest_letter = chara
    
    return highest_letter

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
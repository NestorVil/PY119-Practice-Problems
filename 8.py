# P:
#   Input: A string (non-empty) (entirely lowercase alphabetic characters)
#   Output: A number, representing the length of the longest vowerl substring ("aeiou")
#   Rules:
#       Strings will be not empty
#       Returning a number
#       Will need to keep track of the length of vowels in a row
# E:
    # print(longest_vowel_substring('cwm') == 0)
    # print(longest_vowel_substring('many') == 1)
    # print(longest_vowel_substring('launchschoolstudents') == 2)
    # print(longest_vowel_substring('eau') == 3)
    # print(longest_vowel_substring('beauteous') == 3)
    # print(longest_vowel_substring('sequoia') == 4)
    # print(longest_vowel_substring('miaoued') == 5)
# D:
#   Am working with strings (immutable)
#   Returning integers
#   Checking if a character is a vowel (in a list of vowels?)
# A:
#   Create a 'max_length' variable and set it to an empty string
#   Create a 'the_vowers' variable and set it to a string of the vowels
#   Create a 'running_characters' variable and set it to an empty string
#   Iterate over the 'input_string'
#   If encountering a vowel:
#       add it to running_characters
#   if encountring not a vowel
#       if the length of running characters is bigger than max_length, make max_length equal running characters
#       set running_characters back to an empty string
#   return the length of max_length

def longest_vowel_substring(input_string):
    max_length = ""
    the_vowels = "aeiou"
    running_characters = ''

    for idx, chara in enumerate(input_string):
        if chara in the_vowels:
            running_characters += chara
            if idx == len(input_string) - 1:
                if len(running_characters) > len(max_length):
                    max_length = running_characters
                running_characters = ''
        else:
            if len(running_characters) > len(max_length):
                max_length = running_characters
            running_characters = ''


    return len(max_length)



print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

def longest_vowel_substring(input_string):
    vowels = "aeiou"
    max_length = 0
    current_length = 0

    for char in input_string:
        if char in vowels:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length
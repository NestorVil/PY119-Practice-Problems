# P:
#   Input: A string
#   Output: A boolean value, depending on if the string is a pangram or not
#   Rules:
#       A panagram is a sentence that contains every letter of the alphabet at least once
#       Case is irrelevant
#       Don't care about non-alphabetical letters
#       Comparing if an input_string has all the letters of the alphabet
#       Strings wont be empty
#       Strings usually contain more than one word
# E:
    # print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
    # print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
    # print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
    # print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
    # print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

    # my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
    # print(is_pangram(my_str) == True)
# D:
#   Sets
#   Strings are immutable, so need a way to create a new string that only has letters
# A:
#   Create a set 'alphabet' that has the entire alphabet
#   Create the variable 'cleaned_string' and have it be only the alphabtical letters, and lower case them
#   Turn 'cleaned_string' into a set, and compare it for equality with 'alphabet

def is_pangram(input_string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    cleaned_string = [chara.lower() for chara in input_string if chara.isalpha()]
    return alphabet == set(cleaned_string)

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
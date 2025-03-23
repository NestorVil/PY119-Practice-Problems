# P:
#   Input: A string
#   Output: A number, representing the count of distinct case-insensitive alphanumeric characters that occur
#           more than once in the input string
#   Rules:
#       The input string contains only alphanumeric characters
#       Returning a digit (returning a count)
#       Seeing how many times each chara/num appears in the string, and count it if it appears again
#       xxyypzzr -> (xx, yy, zz) --> 3
#       'uunun' if 'u' appears > 1 time then add 1 to count
# E:
    # print(distinct_multiples('xyz') == 0)               # (none)
    # print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
    # print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
    # print(distinct_multiples('unununium') == 2)         # u, n
    # print(distinct_multiples('multiplicity') == 3)      # l, t, i
    # print(distinct_multiples('7657') == 1)              # 7
    # print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
    # print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
# D:
#   Just counting how many times a certain character appears more than once
#   Some way to iterate over the input string, and a way to count occurance
# A:
#   Set a 'counter' variable to 0
#   Create a 'lowwer_cased' variable and set it to the input_string but lowercased
#   Iterate through 'lower_cased', keeping track of the index, and character
#   Add that character to 'checked_charas"
#   If a character appears more than once in 'lower_cased' after the current idx and not in 'checked_charas'
#       Add it to counter

#   Turn the input_string into a list
#   Make a copy of that input_string list
#   So long as the copy has value:
#       Remove the first element of copy and set it to "checker"
#       If "checker" is still in copy
#       Remove the remaining chara from it, and add 1 to 'counter'

def distinct_multiples(input_string):
    counter = 0
    
    input_string = list(input_string.lower())
    copy_string = input_string[:]

    while copy_string:
        checker = copy_string.pop(0)

        if checker in copy_string:
            while checker in copy_string:
                copy_string.remove(checker)
            
            counter += 1
    
    return counter


def distinct_multiples(input_string):
    input_string = input_string.lower()

    tracker = {chara: input_string.count(chara) for chara in input_string}

    returning_list = [key for key, values in tracker.items() if values > 1]

    return len(returning_list)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
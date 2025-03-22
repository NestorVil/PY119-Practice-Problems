# P:
#   Input: Two strings
#   Output: A number, representing the amount of times the second string occurs in the first string
#   Rules:
#       Overlapping strings dont coumt, so 'babab' only contains one instance of 'bab'
#       The second argument is never an empty string (the first may be an empty string)
# E:
    # print(count_substrings('babab', 'bab') == 1)
    # print(count_substrings('babab', 'ba') == 2)
    # print(count_substrings('babab', 'b') == 3)
    # print(count_substrings('babab', 'x') == 0)
    # print(count_substrings('babab', 'x') == 0)
    # print(count_substrings('', 'x') == 0)
    # print(count_substrings('bbbaabbbbaab', 'baab') == 2)
    # print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
    # print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
# D:
#   Working with strings which are immutable, so will need to do something about that
#   Maybe one thing to do is to work with lists
# A:
#   Split the input_string by the second_argument and place it in a new test_strings variable
#   Pick out all the empty strings in test_strings and place it in a new list
#   Return the length the length of that new list

def count_substrings(input_string, second_argument):
    return input_string.count(second_argument)

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

def count_substring_occurrences(main_string, substring):
    """
    Counts the number of non-overlapping occurrences of a substring in a string.

    Args:
        main_string: The string to search within.
        substring: The substring to count.

    Returns:
        The number of non-overlapping occurrences of the substring.
    """

    count = 0
    start_index = 0
    while True:
        index = main_string.find(substring, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + len(substring)
    return count
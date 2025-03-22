# P:
#   Input: A string (consisting entirely of numeric digits )
#   Output: A number, representing the greatest product of four consecutive digits in the input
#   Rules:
#       The argument will always have more than 4 digits
#       Will need to create all poissible substrings that contain at least four conesuctive digits
#       3145926 -> [[3145], [1459], [4592], [5926]]
#       Once have this ^, get the product of each. return the max value of it
# E:
    # print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
    # print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
    # print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
    # print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
# D:
#   Initially working with strings, will have to turn each character into a number eventually to multiply
#   Getting substrings from a string, so string slicing[: idx + 4]
# A:
#   Create a new variable that will be a list containing substrings, called 'list_of_substrings'
#   Populate list_of_substrings with every possible substring of 4 consecutive digits
#   For each substring in list, of substrings
#       Turn each digit in each substring into a number, multiply it, and append the results to 'multiples'
#   Get the max value within 'multiples' and reuturn it

def greatest_product(input_string):
    list_of_substrings = [input_string[idx: idx + 4] 
                          for idx in range(len(input_string)) 
                          if len(input_string[idx: idx + 4]) == 4]
    
    multiples = []

    for substring in list_of_substrings:
        count = 1
    
        for numbers in substring:
            count *= int(numbers)

        multiples.append(count)
    
    return max(multiples)


print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
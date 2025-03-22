# P:
#   Input: An integer (singular)
#   Output: An integer, representing the sum of all the multiples of 7 or 11 that ar less than the input
#   Rules:
#       If a number is a multiple of both 7 and 11, count it just once
#       Will get an argument like 25. Find all possible multiples of 7 that are less than 25:
#           25 --> 7 14 21
#       Then will need to get all possible multiples of 11 less than 25
#           25 --> 11, 22
#       Will need to combine those those rows of numbers together only caring about uniqueness, and get their sum
#       7, 11, 14, 21, 22 --> sum is 75
#       Possible for numbers to be 0 or less than 0
# E:
    # print(seven_eleven(10) == 7)
    # print(seven_eleven(11) == 7)
    # print(seven_eleven(12) == 18)
    # print(seven_eleven(25) == 75)
    # print(seven_eleven(100) == 1153)
    # print(seven_eleven(0) == 0)
    # print(seven_eleven(-100) == 0)
# D:
#   Might need ranges
#   Might need sets to check for uniqueness
#   Might need a list to append each number
# A:
#   Create a 'multiples_of_7' variable and fill it with all multiples of 7 up to the input_number using a range
#   Create a 'multiples_of_11' variable and fill it with all multiples of 11 up to the input_number using a range
#   Combine multiples_of_7 and multiples_of_11 into a unique_multiples set
#   Turn that set into a list, and get the sum of it
#   Return the sum

def seven_eleven(input_number):
    multiples_of_7 = [num for num in range(0, input_number, 7)]
    multiples_of_11 = [num for num in range(0, input_number, 11)]
    
    unique_multiples = set(multiples_of_11 + multiples_of_7)

    return sum(unique_multiples)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
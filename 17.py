# P:
#   Input: A list of integers
#   Output: A number, representing the minimum integer value that can be appended  to the list
#           so the sum of all the elements equal the closest prime number that is greater than the current sum
#   Rules:
#       Get the sum of all the integers in the input list
#       Find the nearest prime number closest to that sum
#       Find the difference between the nearest prime number and the sum, t hen return it
#       [1, 2, 3] --> Sum is 6, nearest prime number (> greater) is 7. So (7 - 6 = 1)
#       The list will always contain at least 2 integers
#       All values in the list must be positive
#       There may be multiple occurances of the various numbers in the list
#       A prime number is a number that can't be divided equally besides itself
# E:
    # print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
    # print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
    # print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
    # print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

    # # Nearest prime to 163 is 167
    # print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
# D:
#   Working with lists, returning a integer
#   Using sums, absolute values, and prime numbers (going up)
# A:
#   'sum_of_list' set it to the sum of all the integers in the input list
#   Create a 'counter' variable and set it to 0
#   Check if 'sum_of_list' is a prime number
#       If it's not, add one both to 'sum_of_list' and add one to 'counter'

def is_prime(sum_):
    for num in range(2, sum_):
        if sum_ % num == 0:
            return False
    
    return True

def nearest_prime_sum(input_list):
    sum_of_list = sum(input_list)

    counter = 0

    while counter == 0 or not is_prime(sum_of_list):
        counter += 1
        sum_of_list += 1
    
    return counter


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
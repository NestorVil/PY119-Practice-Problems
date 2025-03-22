# P:
#   Input: A list of integers
#   Output: A number, which represents the number of identical pairs of integers in the input list
#   Rules:
#       Keep track of how many identical pairs are in the list [1, 2, 3, 2, 1] -> 2 (because 1, 2 appear two times)
#       If the list is empty or only has one number, return 0
# E:
    # print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
    # print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
    # print(pairs([]) == 0)
    # print(pairs([23]) == 0)
    # print(pairs([997, 997]) == 1)
    # print(pairs([32, 32, 32]) == 1)
    # print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
# D:
#   Working with lists, a nd reutning an integer
#   Need to evalute numbers based on pairs only (can't fully rely on the count method)
# A:
#   If the 'input_list' does not have a length of at least 2, return 0
#   Create 'copied_list' which is a copy of 'input_list'
#   Create 'count' variable and set it to 0
#   So long as 'copied_list' has value
#       Remove the first number in 'copied_list' and set it to variable 'popped_number'
#       If the 'popped_number' still exists in 'copied_list'
#           Find the index of 'popped_number' in 'copied_list' and remove it
#           add one to the 'count' variable
#   Return 'count'

def pairs(input_list):
    copied_list = input_list[:]
    count = 0

    while copied_list:
        popped_number = copied_list.pop(0)
        
        if popped_number in copied_list:
            copied_list.remove(popped_number)
            count += 1
    
    return count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
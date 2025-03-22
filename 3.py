# P:
#   Input: A string
#   Output: A string, where every second character in every third word is uppercased (others should stay the same)
#   Rules:
#       Working with strings
#       Words are separated by spaces, and strings will always have more than one word
#       For every third word: do something (for every second character, make it uppercase)
# E:
    # original = 'Lorem Ipsum is simply dummy text of the printing world'
    # expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
    # print(to_weird_case(original) == expected)

    # original = 'It is a long established fact that a reader will be distracted'
    # expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
    # print(to_weird_case(original) == expected)

    # print(to_weird_case('aaA bB c') == 'aaA bB c')

    # original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
    # expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
    # print(to_weird_case(original) == expected)
# D:
#   Strings are immutable, so will need to turn each word into something else, (a list?)
#   Will need to separate the string into a list of words
#   For every third word, turn it into a list and join it with the second character uppercase
# A:
#   Split the 'input_string' into a list of strings separated by a space -> 'split_string'
#   For every third element of 'split_string':
#       if that word is longer than one character:
#           split the word into a list 
#           for every second element in the new list, make it uppercase
#           join the list into a new word and place it back in the corresponding index of 'split_string
#       if that word is only one character, do nothing
#   Join 'split_'string' as a returning_string and return it

def to_weird_case(input_string):
    split_string = input_string.split(' ')

    for idx, word in enumerate(split_string):
        if (idx + 1) % 3 == 0 :
            split_word = list(word)
            for index, chara in enumerate(split_word):
                if (index + 1) % 2 == 0:
                    split_word[index] = chara.upper()

            split_string[idx] = "".join(split_word)
    
    return " ".join(split_string)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
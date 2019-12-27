# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# Solution
# Palindrome =  count of each letter 1 or even

def count_chars(input_str):
    counts_dict = {}
    for character in input_str:
        counts_dict[character] =  counts_dict.get(character,0) + 1
    return counts_dict

def is_palindrome(input_str):
    input_str = input_str.replace(" ","")
    counts_dict = count_chars(input_str)
    for character in counts_dict:
        if (counts_dict[character] > 1) and (counts_dict[character]%2 ==1):
            return False
    return True

print(is_palindrome("taco cat"))

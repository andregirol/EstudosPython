# 2 - Palindrome
"""
A palindrome is a word, number, phrase, or other sequence of characters which
reads the same backward as forward, such as madam or racecar or the number 10801.
 Sentence-length palindromes may be written when allowances are made for adjustments
 to capital letters, punctuation, and word dividers, such as "A man, a plan, a canal, Panama!",
 "Was it a car or a cat I saw?" or "No 'x' in Nixon".

Examples:
racecar
madam
"""

def is_palindrome(given_string):
    special_chars = "?'! ,"

    palindromic = ''
    for letra in given_string:
        if letra in special_chars:
            continue
        else:
            palindromic += letra.lower()

    return palindromic == palindromic[::-1]


given_string = 'A man, a plan, a canal, Panama!'
assert is_palindrome(given_string) == True

given_string = 'madam'
assert is_palindrome(given_string) == True

given_string = 'racecar'
assert is_palindrome(given_string) == True

given_string = "Was it a car or a cat I saw?"
assert is_palindrome(given_string) == True

given_string = "No 'x' in Nixon"
assert is_palindrome(given_string) == True

given_string = "42024"
assert is_palindrome(given_string) == True

print('Passed!')
"""
A test module to test whether a string is palindrome or not.
filename: test_palindrome.py
author: Chen Lin
"""

import palindrome


def test_is_palindrome(test, word, expected):
    """
    A single test of the is_palindrome function.
    :param test: a string to be tested for being a palindrome or not
    :param word: a string that is being tested
    :param expected: the expected result
    """
    result = palindrome.is_palindrome(word)
    if result == expected:
        print(test, 'true')
    else:
        print(test, 'false; expected', expected, 'but got', result)


def run_test():
    """
    Testing the words to determine whether it is palindrome or not
    """
    test_is_palindrome('ababba', 'ababba', 'true')
    test_is_palindrome('abbaaab', 'abbaaab', 'false')
    test_is_palindrome('bababaa', 'bababaa', 'false')
    test_is_palindrome('abaab', 'abaab', 'false')
    test_is_palindrome('abaa', 'abaa', 'true')
    test_is_palindrome('bbbab', 'bbbab', 'true')
    test_is_palindrome('babbb', 'babbb', 'true')
    test_is_palindrome('abbbba', 'abbbba', 'true')


if __name__ == '__main__':
    run_test()

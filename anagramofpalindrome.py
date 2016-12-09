"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

    >>> is_anagram_of_palindrome("redivider")
    True

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    let_count = {}

    for letter in word:
        let_count[letter] = let_count.get(letter, 0) + 1
    # list comprehension to get only odd values from a list of dict values
    # if the list length is even, then don't want an even length of this list
    # if the list length is odd, then don't want an odd length of this list

    count_lst = [value for value in let_count.values() if value % 2 != 0]

    if len(word) % 2 != 0:
        if len(count_lst) % 2 != 0 and len(count_lst) > 1:
            return False
        return True

    else:
        if len(count_lst) % 2 == 0:
            return False
        return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

"""Make a fibonacci list that goes up to a given max number.

The fibonacci sequence is a list of numbers where each number is the sum of
its 2 preceding numbers.

recursive: lst and length are passed in because to be recursive, something in
the arguments has to change, and lst cannot be provided within the function or else
it will reset.

Examples:

    >>> fib_iter(0)
    0

    >>> fib_iter(5)
    [0, 1, 1, 2, 3, 5]

    >>> fib_iter(7)
    [0, 1, 1, 2, 3, 5]

    >>> fib_iter(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    >>> fib_rec(0)
    0

    >>> fib_rec(5)
    [0, 1, 1, 2, 3, 5]

    >>> fib_rec(7)
    [0, 1, 1, 2, 3, 5]

    >>> fib_rec(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""


def fib_iter(max_n):
    if max_n == 0:
        return 0
    lst = [0, 1]
    while (lst[-1] + lst[-2]) <= max_n:
        lst.append(lst[-1] + lst[-2])
    return lst


def fib_rec(max_n):
    if max_n == 0:
        return 0
    elif (max_n - lst[-1]) > lst[-1]:
        return lst
    else:
        lst.append(lst[-1] + lst[-2])
        fib_rec(max_n)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

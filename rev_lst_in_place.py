# def half_lst(lst):
#     return (len(lst)) / 2


def rev_list_in_place(lst):
    half = (len(lst)) / 2  # find the index at the half of the list, or if len of list is even, find the second half
    i = 0  # create a counter
    j = -(i + 1)
    tmp = 0
    while i < half:
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        i += 1
        j -= 1
    return lst


def rev_list_in_place_soln(lst):
    for i in range(len(lst) / 2):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
    return lst


def rev_list_in_place_rec(lst, i=0):
    if lst == []:
        return
    lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
    if i < (len(lst) / 2) - 1:
        rev_list_in_place_rec(lst, i+1)
    return lst

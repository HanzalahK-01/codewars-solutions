from itertools import combinations
from functools import reduce


def choose_best_sum (t,k,ls):
    """Function that returns the highest possible sum against a ls and against a maximum"""

    combination_tuple = (list(combinations(ls,k)))
    combination_list = [list(tup) for tup in combination_tuple]
    summed_list = [reduce(lambda a, b: a+b, combo) for combo in combination_list]


    difference = [num for num in summed_list if t-num >= 0]
    if len(difference) == 0:
        return None
    
    result = difference[0]
    result = maximum_distance(t, difference, result)

    return result

def maximum_distance(t, difference, result):
    for num in difference:
        if (t-result) >= (t-num):
            result = num
        else:
            continue
    return result


from functools import reduce
def max_sequence (arr : list) -> int:
    """Function that finds the highest summed values from conseciutive integers in a list"""
    if len(arr) == 0:
        return 0

    new_arr = []
    summed_arr = []

    while len(arr)!= 0:
        for num in arr:
            new_arr.append(num)
            summed_arr.append(reduce(lambda a,b: a+b , new_arr))
        arr.pop(0)
        new_arr = []
    
    return max(summed_arr)
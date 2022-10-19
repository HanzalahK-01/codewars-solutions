from itertools import combinations

def pos_average (s : str) -> int :
    """Calculates the percentage of similar indexes in each substring

    Parameters
    ----------
    s : str
        String that has all the substrings within 

    Returns
    -------
    int
        percentage of similarity
    """
    numbers = s.split(',')
    combos = list(combinations(numbers, 2))

    counter = 0

    for num_pairs in combos :
        first_set = list(num_pairs[0])
        second_set = list(num_pairs[1])

        for i in range(len(first_set)):
            if first_set[i] == second_set[i]:
                counter +=1 

    print(counter)
    print(len(combos))
    return counter/(len(numbers) * len(first_set) *len(combos))*1000
    






import numpy as np
def pos_average(s):
    '''Find common positions in strings, and return as a percentage of total positions'''
    s = s.replace(',','')
    s = s.split(' ')
    total = (len(s)*(len(s)-1))/2
    sequence_array = []
    for sequence in s:
        sequence_array.append(list(sequence))
    
    arr = np.array(sequence_array)
    counter = 0
    
    for i in range(0, arr.shape[1]):
    
        unique, counts = np.unique(arr[:,i], return_counts=True)
        print('unique', unique)
        for k in range(0, len(counts)):
            print(counts[k])
            if counts[k] > 1:
                counter += np.sum(np.arange(1, counts[k]))
                
    return counter/(total*len(s[0]))*100

print(pos_average ("64040600, 64464440, 60006040, 49609906, 46664409, 99464446, 90446964, 96940090")) # expected 20.569

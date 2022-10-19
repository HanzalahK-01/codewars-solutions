from termios import TCSETSW


def sumDig_nthTerm(initVal,patternL,nthTerm):
    counter = 0 
   




def test_count(initial_value,patternL,nthTerm,):
    counter = initial_value
    index =0
    new_list = [] 
    while len(new_list) != nthTerm -1:
        new_list.append(patternL[index])
        index += 1
        if index  == len(patternL):
            index =0 
        
    for number in new_list:
        counter+=number

    final_count = 0
    seperated_num = list(str(counter))

    for num in seperated_num:
        final_count+=int(num)

    return final_count


        

Testing testing 1 2 3
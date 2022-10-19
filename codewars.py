from collections import OrderedDict
import math

def cakes(recipe, available):
    rec_keys = sorted(list(recipe.keys()))
    available_keys = sorted(list(available.keys()))

    for stuff in rec_keys:
        if stuff not in available_keys:
            available[stuff] = 0


    max_amount_list = []
    for key in rec_keys:
        max_amount_list.append(math.floor(available[key]/recipe[key]))

    return(min(max_amount_list))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe,available))
import math

def total(values : list) -> float:
    sums = 0
    for i in values:
        sums +=i
    return sums

def average(values : list) -> float:
    if not values:
        return math.nan
    else:
        return total(values)/len(values) 

def median(values : list) -> float:
    values.sort()
    
    if not values:
        raise ValueError

    n = len(values)
    
    if n % 2 == 1:
        return values[n // 2]
    else:
        middle1 = values[n // 2 - 1]
        middle2 = values[n // 2]
        return (middle1 + middle2) / 2
 

from ..fractions.fractionClass import fraction

def am(l):
    if len(l) == 0:
        raise ValueError("There is no average of an empty list")
    s = 0
    for i in l:
        s += i
    return fraction(s, len(l))

def gm(l):
    if len(l) == 0:
        raise ValueError("There is no average of an empty list")
    p = 1
    for i in l:
        p *= i
    return p**(1/len(l))

def hm(l):
    if len(l) == 0:
        raise ValueError("There is no average of an empty list")
    s = fraction(0, 1)
    for i in l:
        s += fraction(1, i)
    return fraction(len(l), s)

def median(l):
    if len(l) == 0:
        raise ValueError("There is no average of an empty list")
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return am([l[len(l) // 2 - 1], l[len(l) // 2]])
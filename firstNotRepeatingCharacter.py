def firstNotRepeatingCharacter(s):
    lst = list(s)
    for i in lst:
        cn = lst.count(i)
        if cn == 1:
            return i
    else:
        return '_'

'''Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for which 
the second occurrence has a smaller index than the second occurrence of the other number does. 
If there are no such elements, return -1.'''

def firstDuplicate(a):

    dict = {}
    found = 0

    for i in range(len(a)):
        if a[i] in dict:
            dict[a[i]] += 1
        else:
            dict[a[i]] = 1

        if(dict[a[i]] == 2):
            return a[i]

    if not found:
        return -1

a = [2, 2]
print(firstDuplicate(a))

def unique(lst):
    lst2 = []
    for el in lst:
        if el not in lst2:
            lst2.append(el)
    return lst2
   
# print("%r" % unique([1, 2, 1, 3, 4, 3, 3, 3]))

def uniquedict(lst):
    d = dict(zip(lst,lst))
    return d.values()


print("%r" % uniquedict([1, 2, 1, 3, 4, 3, 3, 3]))   
print("%r" % uniquedict([]))
print("%r" % uniquedict([1]))
print("%r" % uniquedict([1,2,2,2,1]))
print("%r" % uniquedict([1,1,1,1,1,1,1,]))
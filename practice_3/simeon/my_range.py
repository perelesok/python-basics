def my_range(a , b = 0, step = 1):
    ran = []
    if ((a>b) and (b==0)):
        while (b < a):
            ran.append(b)
            b = b + step
    else:
        while (a < b):
            ran.append(a)
            a = a + step
        
    return ran

# print my_range()
# print range()
 
print my_range(0)
print range(0)
 
print my_range(3)
print range(3)
 
print my_range(1, 3)
print range(1, 3)

print my_range(3, 1)
print range(3, 1)
 
print my_range(0, 11, 2)
print range(0, 11, 2)
   
# 
# def assert_equal(a, b, msg="{} is not equal {}"):
#     assert a == b, msg.format(a, b)
#     print("({}) is equal ({})".format(a, b))
# 
# 
# assert_equal(1, 2)
# assert_equal(1, 2, "Assertion failed")
# 
# def assert_not_equal(a, b, msg = "({}) is equal ({})"):
#     assert a != b, msg.format(a, b)
#     print("({}) is not equal ({})".format(a, b))
# 
# assert_not_equal(1, 2)
# assert_not_equal(1, 1)
# assert_not_equal(1, 1, "Assertion Failed")
# assert_not_equal(1, 2, "Assertion Failed")


# def assert_true(x, msg="({}) not True"):
#     assert x, msg.format(x)
#     print("({}) True".format(x))
# 
# assert_true(True)
# assert_true(False, "Assertion Failed")


# assert_false(x)
# print("\n***assert_false(x)***\n")
# def assert_false(x, msg="({}) not False"):
#     assert not x , msg.format(x)
#     print("({}) False".format(x))
#          
# # assert_false(True, "Assertion Failed")
# # assert_false(False, "Assertion Failed")
# # assert_false(0, "Assertion Failed")
# assert_false(1, "Assertion Failed")


print("\n***assert_is(a, b)***\n")
def assert_is(a, b, msg="({}) is not ({})"):
    assert a is b , msg.format(a,b)
    print("({}) is ({})".format(a,b))
    
assert_is(True, True, "Assertion Failed")
assert_is(0, False)
assert_is(0, False, "Assertion Failed")
    
********************
will be added later|  
********************

# assert_is_not(a, b)
print("\n***assert_is_not(a, b)***\n")
def assert_is_not(a, b):
    assert a is not b , "({}) is ({})".format(a,b)
    print("({}) is not ({})".format(a,b))
         

# assert_is_none(x)
print("\n***assert_is_none(x)***\n")
def assert_is_none(x):
    assert x is None , "({}) is not None".format(x)
    print("({}) is None".format(x))

# assert_is_not_none(x)
print("\n***assert_is_not_none(x)***\n")
def assert_is_not_none(x):
    assert x is not None , "({}) is None".format(x)
    print("({}) is not None".format(x))
         

# assert_in(a, b)
print("\n***assert_in(a, b)***\n")
def assert_in(a, b):
    assert a in b , "({}) not in ({})".format(a,b)
    print("({}) in ({})".format(a,b))
         

def test9(a,b):
    try:
        assert_in(a, b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test9(1,[1])
test9(1,[-1,1,0,2,3])
test9([1,2],[1,2,3])
test9([1,2],[[1,2,3],[1,2]])
test9(1,[[1,2,3],[1,2]])
test9("tr","control")
test9(None,[])

try:
    assert_in(None,["",0, False])
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_in(a, b)
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_in(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))

# assert_not_in(a, b)
print("\n***assert_not_in(a, b)***\n")
def assert_not_in(a, b):
    assert a not in b , "({}) in ({})".format(a,b)
    print("({}) not in ({})".format(a,b))
         

def test10(a,b):
    try:
        assert_not_in(a, b)
    except BaseException as e:
        print("Exception caught: {}".format(e))

test10(1,[1])
test10(1,[-1,1,0,2,3])
test10([1,2],[1,2,3])
test10([1,2],[[1,2,3],[1,2]])
test10(1,[[1,2,3],[1,2]])
test10("tr","control")
test10(None,[])

try:
    assert_not_in(None,["",0, False])
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_not_in(a, b)
except BaseException as e:
    print("Exception caught: {}".format(e))

try:
    assert_not_in(1,1,1)
except BaseException as e:
    print("Exception caught: {}".format(e))


# in commit don't forget add comment
# __init__.py
# andrey.txt
# hash_my_name.py

# filipovski
# AyratSaubanov

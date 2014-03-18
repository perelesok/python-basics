tests = {}
pen_tests = []

def add_test(fn):
    tests.update({fn:"pending"}) 

def pending_tests():
    print("{}".format(tests.values()))
    for el in tests:
        if tests.values is "pending":
            print("%r" % tests.keys())
              
#     return tests.keys() for tests.values() in ["pending"]

#  
# def run():
#          
#     return (ran, passed, failed)


add_test("fn1")
add_test("funct2")
add_test(3)

tests.update({"fn4" : "notpending"}) 

print("%r" % tests)

pending_tests()

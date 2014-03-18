tests = {}
pen_tests = []

def add_test(fn):
    tests.update({fn:"pending"}) 

def pending_tests():
    for k, v in tests.items():
        if v == "pending":
            pen_tests.append(k)
    return pen_tests
              
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

print("%r" % pen_tests)
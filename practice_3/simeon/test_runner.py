tests = {}
pen_tests = []
ran_t = []
pass_t = []
fail_t = []

def add_test(fn):
    tests.update({fn:"pending"}) 

def pending_tests():
    for k, v in tests.items():
        if v == "pending":
            pen_tests.append(k)
    return pen_tests
              
def run():
    ran = 0
    passed = 0
    failed = 0
    for test in pen_tests:
        try:
            test
        except:
            failed = failed + 1
            ran = ran + 1
            tests[test] = "failed"
        else:
            passed = passed + 1
            ran = ran + 1
            tests[test] = "passed"
    return (ran, passed, failed)

def ran_tests():
    for k, v in tests.items():
        if v in ("failed" , "passed"):
            ran_t.append(k)
    return ran_t

def passed_tests():
    for k, v in tests.items():
        if v == "passed":
            pass_t.append(k)
    return pass_t

def failed_tests():
    for k, v in tests.items():
        if v == "failed":
            fail_t.append(k)
    return fail_t

def clear_state():
    del pen_tests[:]
    del ran_t[:]
    del pass_t[:]
    del fail_t[:]
    for k, v in tests.items():
        tests[k] = ""
        
# Test-Suite

# add_test("fn1()")
# add_test("funct2(1,1)")
# add_test("functinT(222)")
# add_test("testFun")
# tests.update({"fn4" : "undefined status"}) 
# print("%r" % tests)
# 
# pending_tests()
# print("%r" % pen_tests)
# 
# # run()
# tupl = run()
# print tupl
# print("%r" % tests)
# 
# ran_tests()
# passed_tests()
# failed_tests()
# print("ran: %r" % ran_t)
# print("passed: %r" % pass_t)
# print("failed: %r" % fail_t)
# 
# clear_state()
# print("%r" % tests)
# print("ran: %r" % ran_t)
# print("passed: %r" % pass_t)
# print("failed: %r" % fail_t)


def assert_equal(a, b, msg="{} is not equal {}"):
    assert a == b, msg.format(a, b)
    print("({}) is equal ({})".format(a, b))


def test_that_fails():
  assert_equal(1, 2)

def test_function_attribute_name():
  def hyper_function():
    pass

  fn = hyper_function

  assert_equal(fn.__name__, "hyper_function")


add_test(test_that_fails)
add_test(test_function_attribute_name)

# returns
# [<function test_that_fails at ...>,
#  <function test_function_attribute at ...>]
pending_tests()

print("%r" % tests.items)
print("pending: %r" % pen_tests)
print("ran: %r" % ran_t)
print("passed: %r" % pass_t)
print("failed: %r" % fail_t)

# returns (2, 1, 1)
run()

print("%r" % tests)
print("ran: %r" % ran_t)
print("passed: %r" % pass_t)
print("failed: %r" % fail_t)

# returns empty list
pending_tests()

print("%r" % tests)
print("ran: %r" % ran_t)
print("passed: %r" % pass_t)
print("failed: %r" % fail_t)

# returns
# [<function test_that_fails at ...>,
#  <function test_function_attribute at ...>]
ran_tests()

# returns [<function test_function_attribute at ...>]
passed_tests()

# returns [<function test_that_fails at ...>]
failed_tests()


# clear all tests
clear_state()


# returns empty collection
pending_tests()

# returns empty collection
ran_tests()

# returns empty collection
passed_tests()

# returns empty collection
failed_tests()
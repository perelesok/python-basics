from test_runner import TestRunner

def fn():
    return 

def fn2():
    return 2

def fn3():
    return 3

def test_assert_equal():
    assert_equal(1,2)

def assert_equal(a, b, msg="{} is not equal {}"):
    assert a == b, msg.format(a, b)
    print("({}) is equal ({})".format(a, b))

test_runner = TestRunner()
test_runner.add_test(fn)
test_runner.add_test(fn2)
test_runner.add_test(fn3)
test_runner.add_test(test_assert_equal)

test_runner.pending_tests()
print test_runner.tests
print "in pending: %r" % test_runner.pen_tests

test_runner.run()
test_runner.pending_tests()
test_runner.ran_tests()
test_runner.passed_tests()
test_runner.failed_tests()

print test_runner.tests
print "in pending: %r" % test_runner.pen_tests
print "ran: %r" % test_runner.ran_t
print "passed: %r" % test_runner.pass_t
print "failed: %r" % test_runner.fail_t

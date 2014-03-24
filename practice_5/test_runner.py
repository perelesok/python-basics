class TestRunner(object):
    def __init__(self):
        self.tests = {}
        self.pen_tests = []
        self.ran_t = []
        self.pass_t = []
        self.fail_t = []

    def add_test(self, fn):
        self.tests.update({fn:"pending"}) 
    
    def pending_tests(self):
        self.pen_tests = []
        for k, v in self.tests.items():
            if v == "pending":
                self.pen_tests.append(k)
        return self.pen_tests
                  
    def run(self):
        ran = 0
        passed = 0
        failed = 0
        self.pending_tests()
        for test in self.pen_tests:
            try:
                test()
            except:
                failed = failed + 1
                ran = ran + 1
                self.tests[test] = "failed"
            else:
                passed = passed + 1
                ran = ran + 1
                self.tests[test] = "passed"
        return (ran, passed, failed)
    
    def ran_tests(self):
        for k, v in self.tests.items():
            if v in ("failed" , "passed"):
                self.ran_t.append(k)
        return self.ran_t
    
    def passed_tests(self):
        for k, v in self.tests.items():
            if v == "passed":
                self.pass_t.append(k)
        return self.pass_t
    
    def failed_tests(self):
        for k, v in self.tests.items():
            if v == "failed":
                self.fail_t.append(k)
        return self.fail_t
    
    def clear_state(self):
        del self.pen_tests[:]
        del self.ran_t[:]
        del self.pass_t[:]
        del self.fail_t[:]
        for k, v in self.tests.items():
            self.tests[k] = ""
        
# Test-Suite
 
test_runner = TestRunner()
 
test_runner.add_test("fn1()")
test_runner.add_test("funct2(1,1)")
test_runner.add_test("functinT(222)")
test_runner.add_test("testFun")
test_runner.tests.update({"fn4" : "undefined status"}) 
print("%r" % test_runner.tests)
  
test_runner.pending_tests()
print("%r" % test_runner.pen_tests)
  
# run()
tupl = test_runner.run()
print tupl
print("%r" % test_runner.tests)
  
test_runner.ran_tests()
test_runner.passed_tests()
test_runner.failed_tests()
print("ran: %r" % test_runner.ran_t)
print("passed: %r" % test_runner.pass_t)
print("failed: %r" % test_runner.fail_t)
  
test_runner.clear_state()
print("%r" % test_runner.tests)
print("ran: %r" % test_runner.ran_t)
print("passed: %r" % test_runner.pass_t)
print("failed: %r" % test_runner.fail_t)
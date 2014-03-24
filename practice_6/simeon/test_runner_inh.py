

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


class TestRunnerBase(TestRunner):

    def report_test_started(self, test):
        pass
    
    def report_test_passed(self, test):
        pass
    
    def report_test_failed(self, test, stack):
        pass
    
    def report_all_finished(self, ran, passed, failed):
        pass
    
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



import importlib
import sys
from test_runner import TestRunner
from decorators import with_tear_down
from decorators import with_set_up
from utils import noop


class TestRunnerLauncher(object):
    TEST_METHOD_PREFIX = "test_"
    SET_UP_METHOD_NAME = "set_up"
    TEAR_DOWN_METHOD_NAME = "tear_down"
    TEST_FUNCTIONS_CONTAINER = "module_functions"
    CLASS_TEST_CONTAINER = "class"
    VERBOSE_REPORTER = "verbose"
    FAIL_REPORTER = "fail"
    TEXT_FILE_REPORTER = "text_file"

    test_runners_dict = {VERBOSE_REPORTER:
                           TestRunner.with_verbose_reporter,
                           FAIL_REPORTER:
                           TestRunner.with_fail_reporter,
                           TEXT_FILE_REPORTER:
                           TestRunner.with_text_file_reporter}

    def __init__(self, test_module_name, test_container_type, test_reporter):
        '''Specifies test runner launcher

        :param test_module_name: name of module with tests
        :param test_container_type: test container type (class or functions)
        :param test_reporting_name: optional, reporting type (4 are available)
        '''
        self.test_module = importlib.import_module(test_module_name)
        self.test_container_type = test_container_type
        self.test_runner = self.test_runners_dict[test_reporter]()
        self.test_extractors_dict = \
                {self.TEST_FUNCTIONS_CONTAINER:
                 self.__extract_tests_from_module_functions,
                 self.CLASS_TEST_CONTAINER:
                 self.__extract_tests_from_classes}

    def execute_tests(self):
        test_lists = self.test_extractors_dict[self.test_container_type]()
        self.test_runner.clear_state()
        for test_list in test_lists:
            [self.test_runner.add_test(test) for test in test_list]
            self.test_runner.run()
        if len(self.test_runner.failed_tests) != 0:
            sys.exit(1)
        else:
            sys.exit(0)

    def __extract_tests_from_module_functions(self):
        tests = [getattr(self.test_module, f) for f
                in dir(self.test_module) if f in self.test_module.__all__]
        return [with_tear_down(noop)
                (with_set_up(noop)(test)) for test in tests]

    def __extract_tests_from_classes(self):
        test_classes = [getattr(self.test_module, f)() for f
                         in dir(self.test_module)
                         if f in self.test_module.__all__]
        return [self.__get_test_lists_info(test_class) for
                test_class in test_classes]

    def __get_test_lists_info(self, test_class):
        set_up_method = noop
        tear_down_method = noop
        tests = []
        for method_name in dir(test_class):
            if method_name.startswith(self.TEST_METHOD_PREFIX):
                tests.append(getattr(test_class, method_name))
            if method_name == self.SET_UP_METHOD_NAME:
                set_up_method = getattr(test_class, method_name)
            if method_name == self.TEAR_DOWN_METHOD_NAME:
                tear_down_method = getattr(test_class, method_name)
        return [with_tear_down(tear_down_method)
                (with_set_up(set_up_method)(test)) for test in tests]



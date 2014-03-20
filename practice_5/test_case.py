from test_runner import TestRunner

class TestCase(object):

    def __init__(self, params):
        test_runner = TestRunner()
        self._todo = Todo()

    def set_up(self):
        self._todo.clear()

    def test_add_todo_adds_pending_item(self):
        self._todo.add("Sandwich")
        items = self._todo.items()
        assert_equal(("Sandwich", Todo.PENDING), items)

    def test_add_return_value(self):
        add_return_index = self._todo.add("Sandwich")
        assert_equal(0, add_return_index)
    

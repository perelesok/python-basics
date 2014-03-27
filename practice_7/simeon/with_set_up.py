def assert_equal(a, b, msg="{} is not equal {}"):
    assert a == b, msg.format(a, b)
    print("({}) is equal ({})".format(a, b))

def with_set_up(set_up):
    def decorator(f):
        def wrapper():
            my_set_up()
            return f()
        return wrapper
 
    return decorator
 
def my_set_up():
    print "An setup..."
 
@with_set_up(my_set_up)
def test_assert_equal():
    assert_equal(1, 2)
 
try:
    test_assert_equal()
except Exception as e:
    print('%r' % e.message)

def wrap(f):
    def new_f():
        print "Before"
        return f()
    return new_f

def print_my_name():
    print("Simeon")
    

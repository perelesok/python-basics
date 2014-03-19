def add_to_dict(dict, **kargs):
    kargs
#     dict.update(el)
    
# add_to_dict()
# Traceback (most recent call last):
#   ...
# TypeError: add_to_dict() takes at least 1 argument (0 given)
d = {"x": 1}
add_to_dict(d, y=2)
print d
# {"x": 1, "y": 2, "z": 3}

d = {"x": 1}
add_to_dict(d, y=2, z=3, w=4, ww="smbl", www=True)
print d

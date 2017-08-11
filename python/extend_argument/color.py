""" demo of call argument unpacking"""

"""list argument"""


def print_args(arg1, arg2, *args):
    print (arg1)
    print (arg2)
    print (args)

t = (11, 12, 13, 14)
print_args(*t)

"""tuple argument"""


def color(red, green, blue, **kwatgs):
    print("r =", red)
    print("g = ", green)
    print("b = ", blue)
    print (kwatgs)


k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
color (**k)
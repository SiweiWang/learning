""" lucas series generate to demo the lazy eval on infinite sequence """
from pprint import pprint as pp
def lucas():
    yield 2
    a = 2
    b = 1
    while b < 100:
        yield b
        a, b = b, a + b

for x in lucas():
    print("{0}, \n".format(x))

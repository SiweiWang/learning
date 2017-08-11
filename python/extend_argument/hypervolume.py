""" demo position arguments"""


def hypervolume(length, *lengths):
    v = length
    for length in length:
        v *= length
    return v

print(hypervolume(2,4))

print(hypervolume(2,4,6,8))

print(hypervolume(2))

print (hypervolume())
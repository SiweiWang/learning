import reader

r = reader.Reader("./test.bz2")
print(r.read())


r = reader.Reader("./test.gz")
print(r.read())

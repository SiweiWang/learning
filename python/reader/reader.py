import os
from reader.compressed import *

extension_map = {
    '.bz2': bz2_opener,
    '.gz': gzip_opener,
}


class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, "rt")

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()


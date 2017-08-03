from collections.abc import Sequence
from bisect import bisect_left


class SortedSet(Sequence):

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        index =  bisect_left(self._items, item)
        found = (index != len(self._items) and item == self._items[index])
        return found

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        #return iter(self._item)
        # instead of delegationg iter, we can use iter
        for item in self._items:
            yield item
    
    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __eq__(self, rhs):
        if not isinstance (rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance (rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def __repr__ (self):
        return "SortedSet({})".format(
        repr(self._items) if self._items else ''
    )

    def count(self, item):
        found = item in self._items
        return int(found)
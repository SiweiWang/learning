from collections.abc import (Sequence, Set)
from bisect import bisect_left
from itertools import chain


class SortedSet(Sequence, Set):
    """SortredSet class which returns a sorted Set"""

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        index = bisect_left(self._items, item)
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
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def count(self, value):
        found = value in self._items
        return int(found)

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def  __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def  __rmul__(self, rhs):
        return self * rhs

    def issubset(self, iterable):
        """"returns true if current is a subset of a set given"""
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        """returns true if current set is a super set of a set given"""
        return self >= SortedSet(iterable)

    def union(self, iterable):
        """return union of current set and given set"""
        return self + SortedSet(iterable)

    def difference(self, iterable):
        """"return difference of current set and given set """
        return self - SortedSet(iterable)

    def intersection(self, iterable):
        """return the intersection of current set and given set"""
        return self & SortedSet(iterable)

    def symmetric_difference(self, iterable):
        """retunr the symmetric difference (which is (A union B) - (A intersect B))"""
        return self ^ SortedSet(iterable)

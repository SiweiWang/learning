import unittest

from sorted_set import SortedSet 

class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7,8,3,1])

    def test_with_duplicates(slef):
        s = SortedSet([8,8,8])
    
    def test_from_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2
        g = gen6842()
    
    def test_default_empty(slef):
        s = SortedSet()

class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6,7,3,9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertTrue(0 not in self.s)

class TestSizePotocol(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([0])
        self.assertEqual(len(s), 1)

    def test_many(self):
        s = SortedSet([0,2,3,4,5])
        self.assertEqual(len(s), 5)


    def test_duplicate(self):
        s = SortedSet([5,5,5])
        self.assertEqual(len(s), 1)

class TestIteratorProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6,7,3,9])
    
    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 6)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

class TestSequenceProtocol(unittest.TestCase):
    
    def setUp(self):
        self.s = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]
    
    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)
    
    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)
    
    def test_index_one_before_the_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertTrue(self.s[:3] == SortedSet([1, 4, 9]))
    
    def test_slice_to_end(self):
        self.assertTrue(self.s[3:] == SortedSet([13, 15]))

    def test_slice_arbitrary(self):
        self.assertTrue(self.s[2:4] == SortedSet([9, 13]))

    def test_slice_full(self):
        self.assertTrue(self.s[:] == self.s)

class TestReprProtocol(unittest.TestCase):
    
    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_some(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual(repr(s), "SortedSet([19, 40, 42])")


class TestInequlityProtocol(unittest.TestCase):
    
    def test_positive_unequal(self):
        self.assertTrue(SortedSet([4, 5, 6]) != SortedSet([1, 2, 3]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([4 ,5, 6,]) != SortedSet([6, 5, 4]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])

    def test_indentity(self):
        s = SortedSet([10 ,11, 12])
        self.assertFalse(s != s)

if __name__ == '__main__':
    unittest.main()

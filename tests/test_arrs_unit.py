import unittest

from utils import arrs


class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEquals(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEquals(arrs.get([1, 2, 3], -1, "test"), 'test')

        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")

    def test_slice(self):
        self.assertEquals(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEquals(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEquals(arrs.my_slice([], 1, 2), [])
        self.assertEquals(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEquals(arrs.my_slice([1, 2, 3, 4], -6, 3), [1, 2, 3])

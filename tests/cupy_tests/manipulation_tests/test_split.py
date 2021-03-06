import unittest

from cupy import testing


@testing.gpu
class TestSplit(unittest.TestCase):

    @testing.numpy_cupy_array_equal()
    def test_array_split1(self, xp):
        a = testing.shaped_arange((3, 11), xp)
        split = xp.array_split(a, 4, 1)
        return xp.concatenate(split, 1)

    @testing.numpy_cupy_array_equal()
    def test_array_split2(self, xp):
        a = testing.shaped_arange((3, 11), xp)
        split = xp.array_split(a, 4, -1)
        return xp.concatenate(split, -1)

    @testing.with_requires('numpy>=1.11')
    @testing.numpy_cupy_array_equal()
    def test_array_split_empty_array(self, xp):
        a = testing.shaped_arange((5, 0), xp)
        split = xp.array_split(a, [2, 4], 0)
        return xp.concatenate(split, 0)

    @testing.numpy_cupy_array_equal()
    def test_array_split_empty_sections(self, xp):
        a = testing.shaped_arange((3, 11), xp)
        split = xp.array_split(a, [])
        return xp.concatenate(split, 0)

    @testing.numpy_cupy_array_equal()
    def test_dsplit(self, xp):
        a = testing.shaped_arange((3, 3, 12), xp)
        split = xp.dsplit(a, 4)
        return xp.dstack(split)

    @testing.numpy_cupy_array_equal()
    def test_hsplit_vectors(self, xp):
        a = testing.shaped_arange((12,), xp)
        split = xp.hsplit(a, 4)
        return xp.hstack(split)

    @testing.numpy_cupy_array_equal()
    def test_hsplit(self, xp):
        a = testing.shaped_arange((3, 12), xp)
        split = xp.hsplit(a, 4)
        return xp.hstack(split)

    @testing.numpy_cupy_array_equal()
    def test_split_by_sections1(self, xp):
        a = testing.shaped_arange((3, 11), xp)
        split = xp.split(a, (2, 4, 9), 1)
        return xp.concatenate(split, 1)

    @testing.numpy_cupy_array_equal()
    def test_split_by_sections2(self, xp):
        a = testing.shaped_arange((3, 11), xp)
        split = xp.split(a, (2, 4, 9), -1)
        return xp.concatenate(split, -1)

    @testing.numpy_cupy_array_equal()
    def test_split_by_sections3(self, xp):
        a = testing.shaped_arange((3, 11), xp)
        split = xp.split(a, (-9, 4, -2), 1)
        return xp.concatenate(split, 1)

    @testing.numpy_cupy_array_equal()
    def test_vsplit(self, xp):
        a = testing.shaped_arange((12, 3), xp)
        split = xp.vsplit(a, 4)
        return xp.vstack(split)

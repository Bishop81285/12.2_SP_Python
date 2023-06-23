import pytest

from utils import arrs


@pytest.fixture
def data_test_slice():
    return [1, 2, 3, 4]


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, 'test', 2),
    ([1, 2, 3], -1, "test", 'test')
])
def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected

    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice(data_test_slice):
    assert arrs.my_slice(data_test_slice, 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice(data_test_slice, -2) == [3, 4]
    assert arrs.my_slice(data_test_slice, -6, 3) == [1, 2, 3]

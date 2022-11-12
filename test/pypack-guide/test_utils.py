from pypack_guide.utils import add, subtract


class Test_Utils:
    def test_add(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(3, 1) == 2

import _path

from src.pypack_guide.utils import add

print(_path.__name__)


class Test_Utils:
    def test_add(self):
        assert add(1, 2) == 3

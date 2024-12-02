import pytest

from tools import ADD
from Common.Read_Data import build_data


class TestAdd:
    @pytest.mark.parametrize('a,b,expert',build_data())
    def test_add(self,a,b,expert):
        print(f'{a},{b},{expert}')
        assert expert == ADD(a,b)



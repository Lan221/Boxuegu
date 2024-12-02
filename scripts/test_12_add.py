from tools import ADD

class TestAdd:
    def test_add_1(self):
        print('1,5,6')
        assert 6 == ADD(1,5)

    def test_add_2(self):
        print('9,8,17')
        assert 17 == ADD(9,8)

    def test_add_3(self):
         print('11,8,19')
         assert 18 == ADD(11,8)


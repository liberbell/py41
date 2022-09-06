import pytest
import calculation



# if __name__ == "__main__":
#     test_add_num_and_double.main()

class TestCal(object):
    def test_add_num_and_double():
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 5

    def test_add_num_and_double_raise(self):
        with self.assertRaise(ValueError):
            self.cal.add_num_and_doubule("1", "1")

if __name__ == "__main__":
    TestCal.main()
import pytest
import calculation


class TestCal(object):
    
    def setup_method(self, method):
        print("Method: {}".format(method.__name__))
        self.cal = calculation.Cal()

    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double(1, 1)

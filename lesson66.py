import pytest
import calculation


class TestCal(object):
    
    def setup_method(self, method):
        print("Method: {}".format(method.__name__))
        self.cal = calculation.Cal()

    def teardown_method(self, method):
        print("Method: {}".format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double(1, 1)

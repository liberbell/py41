import pytest
import calculation


class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        del cls.cal
    
    def setup_method(self, method):
        print("Method: {}".format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print("Method: {}".format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double(1, 1)

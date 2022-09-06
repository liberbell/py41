import pytest
import calculation

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cls = calculation.Cal()

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

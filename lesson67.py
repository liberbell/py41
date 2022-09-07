import pytest
import calculation

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()

    def test_add_num_and_double(self):
        if os_name == "mac":
            print("ls")
        elif os_name == "windows":
            print("dir")
        assert self.cal.add_num_and_double(1, 1) == 4

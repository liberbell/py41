import pytest
import calculation

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()

    def test_add_num_and_double(self, tmpdir):
        # os_name = request.config.getoption("--os-name")
        # print(os_name)
        # if os_name == "mac":
        #     print("ls")
        # elif os_name == "windows":
        #     print("dir")
        print(tmpdir)
        assert self.cal.add_num_and_double(1, 1) == 4

from tempfile import tempdir
import pytest
import calculation
import os

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()
        cls.test_file_name = "test1.txt"

    def test_add_num_and_double(self):
        # os_name = request.config.getoption("--os-name")
        # print(os_name)
        # if os_name == "mac":
        #     print("ls")
        # elif os_name == "windows":
        #     print("dir")
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        print(self.test_file_name)
        print(tempdir)
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True


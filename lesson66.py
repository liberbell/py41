import pytest
import calculation


class TestCal(object):
    def test_add_num_and_double():
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_doubule("1", "1")

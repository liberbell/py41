import pytest
import calculation

def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1, 1) == 5

# if __name__ == "__main__":
#     test_add_num_and_double.main()
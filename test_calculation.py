import unittest
import calculation

class CalTest(unittest.TestCase):
    def setup(self):
        print("setup")
        self.cal = calculation.Cal()

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        cal = calculation.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double("1", "1")


if __name__ == "__main__":
    unittest.main()
import unittest

from Lab2.bmi import calculate_bmi


class MyTestCase(unittest.TestCase):
    def test_bmi(self):
        test=-1
        result=calculate_bmi(1.70,45)
        assert test==result
    def test_normal(self):
        test=0
        result=calculate_bmi(1.70,70)
        assert test==result
    def test_fat(self):
        test=1
        result=calculate_bmi(1.8,100)
        assert test==result




if __name__ == '__main__':
    unittest.main()

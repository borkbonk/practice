import unittest

import price_info

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result=price_info.total_cost_shopping()
        test=46.75
        assert test==result

    def test_cost(self):
        result=0
        quantity=5
        type_of_fruit_in_list = 'orange'

        test=price_info.cost_of_fruits(type_of_fruit_in_list,quantity)
        assert test==7.0


if __name__ == '__main__':
    unittest.main()

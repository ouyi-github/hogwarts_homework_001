import os

import pytest
from conftest import get_data_from_yaml

class TestCal:
    data = get_data_from_yaml(path='./../case_data/test_calculatorcase_data.yaml')

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b',data,
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_add(self,a,b,satrt_calculator):
        """
        testcase for Calculator.add
        :param a:
        :param b:
        :return:
        """
        assert satrt_calculator.add(a,b) == a + b

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b', data,
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_mul(self, a, b, satrt_calculator):
        """
        testcase for Calculator.mul
        :param a:
        :param b:
        :return:
        """
        assert satrt_calculator.mul(a, b) == a * b

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b', data,
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_sub(self,a,b,satrt_calculator):
        """
        testcase for Calculator.sub
        :param a:
        :param b:
        :return:
        """
        assert satrt_calculator.sub(a,b) == a - b

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b', data,
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_div(self,a,b,satrt_calculator):
        """
        testcase for Calculator.div
        :param a:
        :param b:
        :return:
        """
        assert satrt_calculator.div(a,b) == a / b

if __name__ == "__main__":
    pytest.main(['-vs','test_calculator.py','--alluredir=./../report/testreport'])
    os.system('allure generate ./../report/testreport -o ./../allure-report')
    os.system('allure open ./../allure-report')










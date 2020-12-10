import pytest
import logging

import yaml

from pythoncode.calculator import Calculator

class TestCal:
    def setup_class(self):
        self.calculator = Calculator()
        print('测试开始')

    def teardown_class(self):
        print('测试结束')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./../case_data/test_calculatorcase_data.yaml')),
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_add(self,a,b):
        """
        testcase for Calculator.add
        :param a:
        :param b:
        :return:
        """
        assert self.calculator.add(a,b) == a + b



    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./../case_data/test_calculatorcase_data.yaml')),
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_sub(self,a,b):
        """
        testcase for Calculator.sub
        :param a:
        :param b:
        :return:
        """
        assert self.calculator.sub(a,b) == a - b



    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./../case_data/test_calculatorcase_data.yaml')),
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_mul(self,a,b):
        """
        testcase for Calculator.mul
        :param a:
        :param b:
        :return:
        """
        assert self.calculator.mul(a,b) == a * b



    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./../case_data/test_calculatorcase_data.yaml')),
                             ids=['positive_integer', 'negative_integer', 'zero', 'super_positive_integer',
                                  'supernegative_integer',
                                  'float'])
    def test_div(self,a,b):
        """
        testcase for Calculator.div
        :param a:
        :param b:
        :return:
        """
        assert self.calculator.div(a,b) == a / b

if __name__ == "__main__":
    pytest.main(['-vs','test_calculator.py'])
    # s = yaml.safe_load(open('./../case_data/test_calculatorcase_data.yaml'))
    # print(s['add'])







# 公共fixture
import pytest
from pythoncode.calculator import Calculator
@pytest.fixture(scope='module')
def satrt_calculator():
    print('开始计算')
    calculator = Calculator()  # 初始化一个Calculator实例
    yield calculator
    print('计算结束')


# 公共方法
import yaml
def get_data_from_yaml(path):
    """
    获取yaml文件中的数据
    :param path:
    :return:
    """
    with open(path,'r') as f:
        data = yaml.safe_load(f)
        return data





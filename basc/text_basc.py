
from uilte import Uilte

# 定义对象层--基类
class TestBasc:

    # 定义类方法,属性公用
    def __init__(self):
        self.driver = Uilte.driver_open()

    # 定义一个方法级别,用于存放元素定位的转换
    def find_elment(self, data):
        return self.driver.find_element(*data)


#  定义操作层--基类
class TestOperat:

    def testoperat(self, elemt, text):
        elemt.clear()
        elemt.send_keys(text)


import json
import logging.handlers
import time
from selenium.webdriver.common.by import By
from basc.text_basc import TestBasc, TestOperat
from uilte import Uilte

# 对象层
class FindData(TestBasc):  # 继承基类--对象层

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    code = (By.CLASS_NAME, "chick_ue")
    submit = (By.CLASS_NAME, "sub")

    # 定义公共类方法:
    def __init__(self):
        super().__init__()

    # 查找用户名定位方法方法
    def find_username(self):
        return self.find_elment(self.username)
    # 查找密码元素定位方法

    def find_pwd(self):
        return self.find_elment(self.password)

    # 查找验证码定位方法
    def find_code(self):
        return self.find_elment(self.code)

    # 查找按钮登录元素定位方法
    def find_submit(self):
        return self.find_elment(self.submit)



#  操作层
class FindDataOprate(TestOperat):

    def __init__(self):
        self.driver = FindData()

    def oprate_username(self, username):
        self.testoperat(self.driver.find_username(), username)

    def oprate_pwd(self, pwd):
        self.testoperat(self.driver.find_pwd(), pwd)

    def oprate_code(self, code):
        self.testoperat(self.driver.find_code(),code)

    def oprate_submit(self):
        self.driver.find_submit().click()


# 业务层
class YeWuCeng:
    def __init__(self):
        self.driver = FindDataOprate()

    def page_yewuceng_login(self, username, pwd, code):
        self.driver.oprate_username(username)
        self.driver.oprate_pwd(pwd)
        self.driver.oprate_code(code)
        self.driver.oprate_submit()


# 断言
def duanyan():
    driver = Uilte.driver_open()
    mgd = driver.find_element_by_class_name("error").text
    print(mgd)
    return mgd



# 参数化
def canshuhua(file_json):
    dict_list = []
    with open(file_json, encoding="utf-8") as f:
        dict = json.load(f)
        for i in dict.values():
            a = list(i.values())
            dict_list.append(a)
    return dict_list


# if __name__ == '__main__':
#     driver = Uilte().driver_open()
#     driver.get("http://localhost/index.php/Admin/Admin/login")
#     time.sleep(2)
#     a = YeWuCeng()
#     a.page_yewuceng_login("admin", "123456", "8888")
#     Uilte().driver_quit()

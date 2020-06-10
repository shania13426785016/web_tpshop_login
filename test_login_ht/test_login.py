import time
import unittest
import logging.handlers
from parameterized import parameterized
from page.test_page import YeWuCeng, duanyan, canshuhua
from uilte import Uilte



# 后台登录主页面类
class TpShow(unittest.TestCase):

    # 定义标识符类方法开始
    @classmethod
    def setUpClass(cls):
        cls.driver = Uilte.driver_open()
        cls.yewuceng = YeWuCeng()

    # 定义标识符类方法结束
    @classmethod
    def tearDownClass(cls):
        Uilte.driver_quit()

    # 定义setup方法
    def setUp(self):
        path_add = "http://localhost/index.php/Admin/Admin/login"
        self.driver.get(path_add)

    # 定义登录页面方法
    # 参数化
    @parameterized.expand(canshuhua("./json_page.json"))
    def test01_page_ht(self, username, pwd, code, expent, is_succ):
        self.yewuceng.page_yewuceng_login(username, pwd, code)
        # 断言
        if is_succ is True:
            logging.info("正向断言方法")
            time.sleep(4)
            title = self.driver.title
            print(title)
            self.assertIn(expent, title)
        else:
            logging.info("反向断言方法")
            mgs = duanyan()
            self.assertIn(expent, mgs)

# 生成测试报告
import time
import unittest
from unittest import TestSuite
from BeautifulReport import BeautifulReport
from test_login_ht.test_login import TpShow
# 1.导包
# 2.生成测试套件
# 你运行这个文件就以这个文件为基准去算相对路径,相对于这个文件测试数据在当前目录下 ./json_page.json
# 你运行测试用例就以测试用例为基准去计算,就是../json_page.json
suite = TestSuite()
# 添加一个类
suite.addTest(unittest.makeSuite(TpShow))
# 3.保存的文件路径命名
file_namm = "report-{}.html".format(time.strftime("%m%d%H%M"))
# 4.运行测试用例并生成测试报告
BeautifulReport(suite).report(filename=file_namm, description="测试报告,谷歌", log_path="./report")
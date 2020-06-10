# 创建浏览器工具类
import logging
import time
from selenium import webdriver


class Uilte:
    # 1. 定义浏览器驱动对象
    __driver = None  # 防止修改属性,设置私有属性,设置为空

    @classmethod
    def driver_open(cls):
        # 防止都次调用时,打开多个浏览器驱动窗口,设置判断条件,如果为空,创建驱动对象
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            # 最大化窗口,隐式等待10秒
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    # 2.定义关闭浏览器
    @classmethod
    def driver_quit(cls):
        time.sleep(2)
        cls.__driver.quit()


# 添加日志跟踪方法
def log_data():
    # 1创建日志器,设置严重程度
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 2创建控制器
    ls = logging.handlers.TimedRotatingFileHandler("./log/log.log", when="midnight", interval=1, backupCount=2)
    ms = logging.StreamHandler()
    # 3格式化
    formatt = logging.Formatter(
        fmt="%(asctime)s %(levelno)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 4控制器格式化
    ls.setFormatter(formatt)
    ms.setFormatter(formatt)
    # 5控制器处理日志器
    logger.addHandler(ls)
    logger.addHandler(ms)

    # 6打印
    # logging.info("nihao ")


if __name__ == '__main__':
    driver = Uilte.driver_open()
    driver.get("https://www.baidu.com/?tn=88093251_56_hao_pg")
    Uilte.driver_quit()

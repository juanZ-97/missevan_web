# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome( )


# 登录
class LogIn(object):
    def __init__(self):
        self.driver = webdriver.Chrome( )

    def get(self):
        self.driver.get('https://www.missevan.com')

    def add_cookie(self):
        driver.add_cookie(dict(name='token' , value='5f47236c23868ba1d29e4612%7C5608b294b9aa0bad%7C1598497644%7C42abfda5835c3ade'))
        driver.add_cookie(dict(name='Hm_lvt_91a4e950402ecbaeb38bd149234eb7cc' , value='1597736452'))
        driver.add_cookie(dict(name='MUATSESSID' , value='ikcuqflhboujrkqe2haqjoddah'))
        driver.add_cookie(dict(name='Hm_lpvt_91a4e950402ecbaeb38bd149234eb7cc' , value='1598511896'))
        driver.get('https://www.missevan.com')

# 关闭窗口
class CloseWindow(object):
    driver.close( )

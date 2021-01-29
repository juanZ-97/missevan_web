import pytest
from time import sleep
from selenium import webdriver
from TestDatas.DramaDatas import drama_datas
from TestDatas.GlobalDatas import global_datas
from PageObjects.DramaPage.drama_page import DramaPage
from PageObjects.LoginPage.login_page import LoginPage
from Common.plugs.basepage import BasePage

# 此处缺少 log 的操作
driver = None
@pytest.fixture(scope='class')
def start_module(project_module_start):
    '''
        每个模块单独打开一次浏览器，此时 driver.quit() 需要单独加上
        :param project_module_start:  每个模块单独打开一次浏览器
        :return: driver ug    ????后面再研究这是啥
        '''
    print("==========开始执行测试用例集===========")
    global driver
    driver = project_module_start
    print("----------------------------------------------------------------------------------" + str(driver))
    driver.get(global_datas.web_index_url)
    LoginPage.login()
    driver.get(global_datas.web_darma_url)
    sleep(2)
    assert DramaPage.drama_comment(drama_datas.comment_text) == '每日一刷打卡'
    print('==========结束执行测试用例集===========')
    driver.quit()



    


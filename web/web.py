# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.missevan.com')
driver.maximize_window()
driver.implicitly_wait(10)

# 登录
def login():
    driver.add_cookie(dict(name='token' , value='5f589aebcd9b747c86fb2ece%7C4a25a266bb4eb008%7C1599642347%7Ccfd8a179912bfaba'))
    driver.add_cookie(dict(name='Hm_lvt_91a4e950402ecbaeb38bd149234eb7cc' , value='1597736452,1599447677'))
    driver.add_cookie(dict(name='MUATSESSID' , value='qboc9jsvel5css39mb6lq9d43v'))
    driver.add_cookie(dict(name='Hm_lpvt_91a4e950402ecbaeb38bd149234eb7cc' , value='1599642348'))

# 检测评论是否成功
def test_verify_comment():
    driver.find_element_by_xpath('//*[@id="comments-area"]/div[1]/div[2]/div[1]/textarea').send_keys('每日一刷打卡')
    driver.find_element_by_xpath('//*[@id="comments-area"]/div[1]/div[2]/div[2]/button[2]').click( )
    sleep(2)
    comment_text = driver.find_element_by_xpath('//*[@id="comments-area"]/div[2]/div/div[3]/div[1]/div/div[2]').text
    assert comment_text == '每日一刷打卡'

# 弹幕
def test_dm():
    driver.find_element_by_xpath('//*[@id="prdm"]/div/input').send_keys('真的好好看啊！')
    driver.find_element_by_xpath('//*[@id="prdm"]/div/button').click()
    # dm_text = driver.find_element_by_xpath('//*[@id="commentCanvas"]/div').text
    # print(dm_text)
    # if(dm_text == '真的好好看啊！'):
    #     print('发送弹幕成功')
    # else:
    #     print('发送弹幕失败')

def test_like():
    driver.find_element_by_xpath('//*[@id="dzbtn-container"]/span').click()
    sleep(1)
#     进入我的收藏中查看是否喜欢成功
    driver.find_element_by_xpath('//*[@id="header"]/div/ul[2]/li[2]/a/img').click()
    sleep(1)
    # 定位到新的窗口
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(5)
    driver.find_element_by_class_name('self-heart').click()
    like_id = driver.find_element_by_xpath('//*[@id="homepage-container"]/div/div/div[2]/div[1]').get_attribute('data-id')
    if(like_id == '1005552'):
        print('喜欢成功')
    else:
        print('喜欢失败')
    # 取下喜欢
    driver.get('https://www.missevan.com/sound/player?id=1005552')
    driver.find_element_by_xpath('//*[@id="dzbtn-container"]/span').click()




login()
driver.get('https://www.missevan.com')
# 进入剧集详情页
driver.get('https://www.missevan.com/sound/player?id=1005552')

# 发表评论
test_verify_comment()
# sleep(3)
# driver.get('https://www.missevan.com/sound/player?id=1005552')
# verify_comment()

# 发送弹幕
# dm()
driver.implicitly_wait(10)
test_like()
# sleep(15)
driver.quit()
# common 共同的；公共的  key
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

time.sleep(3)
# 找到输入框，并且输入指定的内容
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(3)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(3)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(3)
driver.find_element_by_id('kw').send_keys(u'爬虫技巧')
time.sleep(3)
driver.find_element_by_id('su').click()
time.sleep(5)
# 退出浏览器
driver.quit()


